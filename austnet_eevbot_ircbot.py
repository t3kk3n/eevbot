#!/usr/bin/python

"""
  EEVBot - Austnet IRC bot

  A twitter IRC bot, modified for AustNet #eevblog.
  Original twitter/IRC code - https://github.com/sixohsix/twitter/blob/master/twitter/ircbot.py
  Modified / maintained by - electrohead / corp[at]hush[dot]ai

  A big thanks to "the internet" for the ideas and help with bugs, and what not.

  This code originally started out as a minor side project, which eventually took over the
  old bot. This code was originally very messy, then over time, got to the point it is at.
  There are still a few areas that need to be redone/reworked, and shall be worked on over time.

"""

import irclib
import base64, json, os, pytz, random, re, requests, string, sys, time, traceback, urllib
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from email.utils import parsedate
from heapq import heappop, heappush
from urlextract import URLExtract

from twitter.api import Twitter, TwitterError
from twitter.oauth import OAuth, read_token_file
from twitter.oauth_dance import oauth_dance
from twitter.util import htmlentitydecode

import xconvert
import xcreds

dquotes = [
    "She'll be right. Good enough for 'Straya",
    "None of that ....... rubbish.",
    "Don't turn it on, take it apart!",
    "We're in like Flynn.",
    "Drier than a dead dingo's donger.",
    "A thing of beauty and a joy forever.",
    "With the tongue at the right angle.",
    "The cheapest they could find at the Shenzhen markets that week.",
    "Made in the United States of 'murica.",
    "A shout-out to all my .... viewers.",
    "For those playing along at home...",
    "Go figure.",
    "You gotta me shittin' me!",
    "A trap for young players.",
    "Ohh, she looks pretty crusty.",
    "*Long sniff* That [60's/70's/80's] electronic smell.",
    "Built like a brick dunny.",
    "Half a bee's dick.",
    "Catch ya next time.",
    "Sex on a stick!",
    "That's about all she wrote.",
    "No worries, she'll be right!",
    "Bob's your uncle."
]

qmsgs = [
    "I'm leaving, noooo",
    "/dev/null",
    "Over and out",
    "It is a layer 8 problem",
    "Packet held up at customs",
    "Network down, IP packets delivered via UPS",
    "Maintenance window broken",
    "Traffic jam on the Information Superhighway",
    "DELETE! DELETE! DELETE!",
    "EXTERMINATE! EXTERMINATE! EXTERMINATE!",
    "Excessive lameness made me quit",
    "Incompetent Operator error"
]

beermsg = [
    "tosses {} a nice cold brew",
    "chucks a beer at {}'s face",
    "offers liquid awesomeness",
    "gets {} annihilated",
    "bathes {} in beer"
]

teamsg = [
    "hands {} a cup o' tea",
    "invites {} over for a tea party",
    "submerges {} in tea and sugar",
    "tea-bags {}",
    "dunks {} in a cup of screaming hot water"
]

coffeemsg = [
    "throws screaming hot coffee at {}",
    "drowns {} in coffee",
    "hooks {} up to a coffee IV",
    "pours coffee down {}'s throat",
    "slides a cup of joe to {}"
]

bot_ver = "EEVBot v1.1"
dom_twitter = "api.twitter.com"
encoding = "utf-8"
oauth_file = "oauth_creds"
tpostb = True
irc_server = "irc.austnet.org"
irc_port = 6667
irc_channel = "#eevblog"
irc_nick = "EEVBot"
irc_usrname = "EEVBot"
irc_ircname = "EEVBot"
irc_pwd = xcreds.xvar1
twitter_ckey = xcreds.xvar2
twitter_csecret = xcreds.xvar3
irc_srvwait = 15
sched_tmr = 105
fcount = 1.0
pubfltime = 0
privfltime = 0
usrtzdb = "usrtzdb"
usrtzdblist = "usrtzdblist"
tformat = "%Y/%m/%d %H:%M:%S"
ccstrip = re.compile('[\x02\x0F\x16\x1D\x1F]|\x03(\d{,2}(,\d{,2})?)?')

IRC_BOLD = "\x02"
IRC_ITALIC = "\x1D"
IRC_UNDERLINE = "\x1F"
IRC_REGULAR = "\x0F"

debugchk = False

class SchedTask(object):
    def __init__(self, task, delta):
        self.task = task
        self.delta = delta
        self.next = time.time()

    def __repr__(self):
        return "<SchedTask %s next:%i delta:%i>" %(self.task.__name__, self.next, self.delta)

    def __lt__(self, other):
        return self.next < other.next

    def __call__(self):
        return self.task()

class Scheduler(object):
    def __init__(self, tasks):
        self.task_heap = []
        for task in tasks:
            heappush(self.task_heap, task)

    def next_task(self):
        now = time.time()
        task = heappop(self.task_heap)
        wait = task.next - now
        task.next = now + task.delta
        heappush(self.task_heap, task)
        if (wait > 0):
            time.sleep(wait)
        task()
        #print("tasks: " + str(self.task_heap))

    def run_forever(self):
        while True:
            self.next_task()


class TwitterBot(object):
    def __init__(self):
        if not os.path.exists(oauth_file):
            oauth_dance("EEVBlog IRC Relay", twitter_ckey, twitter_csecret, oauth_file)
        oauth_token, oauth_secret = read_token_file(oauth_file)

        self.twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, twitter_ckey, twitter_csecret), domain=dom_twitter)

        self.irc = irclib.IRC()
        self.irc.add_global_handler('privmsg', self.handle_privmsg)
        self.irc.add_global_handler('pubmsg', self.handle_pubmsg)
        self.irc.add_global_handler('ctcp', self.handle_ctcp)
        self.ircServer = self.irc.server()

        self.sched = Scheduler((SchedTask(self.process_events, 1), SchedTask(self.check_statuses, sched_tmr)))
        self.lastUpdate = (datetime.utcnow() - timedelta(minutes=10)).utctimetuple()

    def check_statuses(self):
        try:
            updates = reversed(self.twitter.statuses.home_timeline())
        except Exception as e:
            print("***** TWITTER QUERY EXCEPTION - " + str(time.ctime()) + " *****", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            return
        nextLastUpdate = self.lastUpdate
        for update in updates:
            crt = parsedate(update['created_at'])
            if (crt > nextLastUpdate):
                text = (htmlentitydecode(update['text'].replace('\n', ' ')).encode(encoding, 'replace'))
                if not text.startswith(b"@"):
                    if tpostb:
                        msg = IRC_BOLD + "[Twitter] - " + update['user']['screen_name'] + " - " + text.decode(encoding) + IRC_REGULAR
                        self.ircServer.privmsg(irc_channel, msg)
                        print("** POSTING NEW TWITTER MESSAGE - " + update['user']['screen_name'] + " - " + text.decode(encoding))
                    else:
                        print("** NEW TWITTER MESSAGE (NOT POSTED IN CHANNEL)")
                nextLastUpdate = crt
        self.lastUpdate = nextLastUpdate

    def process_events(self):
        self.irc.process_once()

    def convertfunc(self, val, pfrom, pto):
        pfrom = pfrom.lower()
        pto = pto.lower()
        if (pfrom in (xconvert.temp_vars)) and (pto in (xconvert.temp_vars)):
            rval = xconvert.func_temp(val, pfrom, pto)
        elif (pfrom in (xconvert.dist_vars)) and (pto in (xconvert.dist_vars)):
            rval = xconvert.func_dist(val, pfrom, pto)
        elif (pfrom in (xconvert.vol_vars)) and (pto in (xconvert.vol_vars)):
            rval = xconvert.func_vol(val, pfrom, pto)
        elif (pfrom in (xconvert.weight_vars)) and (pto in (xconvert.weight_vars)):
            rval = xconvert.func_weight(val, pfrom, pto)
        elif (pfrom in (xconvert.speed_vars)) and (pto in (xconvert.speed_vars)):
            rval = xconvert.func_speed(val, pfrom, pto)
        else:
            rval = "Invalid"
        return rval

    def davequote(self):
        return(random.choice(dquotes))

    def getcurtime(self, tnick):
        try:
            if tnick in ["eevblog", "eevBlog", "EEVBlog", "eevbot", "eevBot", "EEVBot"]:
                tz = pytz.timezone("Australia/Sydney")
                timedata = "It is currently " + str(datetime.now(tz).strftime(tformat)) + " at the EEVBlog lab."
            else:
                with open(usrtzdb, "r") as f:
                    findusr = [l for l in f if l.startswith(tnick)]
                if findusr:
                    x1 = "".join([elem for elem in findusr[0:] if elem.strip()]).rstrip()
                    usrtz = x1.split("|")[1]
                    try:
                        tz = pytz.timezone(usrtz)
                        timedata = "It is currently " + str(datetime.now(tz).strftime(tformat)) + " where " + tnick + " resides."
                    except:
                        timedata = "\"" + usrtz + "\" is an invalid time zone, " + tnick + " needs to fix this!"
                else:
                    timedata = "No time zone data found for " + tnick + "!"
            return timedata
        except:
            print("***** Traceback - " + str(time.ctime()) + " - *****")
            traceback.print_exc(file=sys.stderr)
            pass

    def random_user(self):
        self.ircServer.names(irc_channel)
        lnames_str = self.ircServer.nicklist.strip()
        lnames_list = lnames_str.split(" ")
        return(random.choice(lnames_list).strip("@+% "))

    def eevbot_custom_cmds(self, snick, targs):
        global tpostb
        pcmd = targs[0].lower().strip()
        try:
            if pcmd == "convert":
                dindex = targs.index("to")
                cval = float(targs[1].strip())
                cfrom = " ".join([elem for elem in targs[2:dindex] if elem.strip()])
                cto = " ".join([elem for elem in targs[dindex+1:] if elem.strip()])
                if cval and cto and cfrom:
                    sendvar = self.convertfunc(cval, cfrom, cto)
                    self.ircServer.privmsg(irc_channel, snick + ": The result is " + str(sendvar) + " " + str(cto))
            elif pcmd == "give":
                dindex = targs.index("to")
                item = " ".join([elem for elem in targs[1:dindex] if elem.strip()])
                dnick = " ".join([elem for elem in targs[dindex+1:] if elem.strip()])
                if item == "beer":
                    self.ircServer.action(irc_channel, random.choice(beermsg).format(dnick))
                elif item == "tea":
                    self.ircServer.action(irc_channel, random.choice(teamsg).format(dnick))
                elif item == "coffee":
                    self.ircServer.action(irc_channel, random.choice(coffeemsg).format(dnick))
                elif item == "handjob":
                    self.ircServer.action(irc_channel, "furiously jerks " + dnick + " off until their bush catches fire")
                elif item == "balloons":
                    self.ircServer.action(irc_channel, "shoves a few dozen balloons down " + dnick + "'s throat, injecting them with air, and watching " + dnick + " float away")
                else:
                    self.ircServer.action(irc_channel, "hands " + item + " to " + dnick)
            elif pcmd == "time":
                try:
                    tmpusr = targs[1].strip()
                except:
                    tmpusr = "eevblog"
                self.ircServer.privmsg(irc_channel, self.getcurtime(tmpusr))
            elif pcmd == "timeset":
                tmptz = " ".join([elem for elem in targs[1:] if elem.strip()])
                if tmptz:
                    findtz = None
                    with open(usrtzdblist, "r") as f:
                        for ln in f:
                            ln = ln.strip()
                            if tmptz == ln:
                                findtz = ln
                                break
                    if findtz:
                        with open(usrtzdb, "r") as f:
                            findusrentry = [l for l in f if l.startswith(snick)]
                        if findusrentry:
                            tmpentry = "".join([elem for elem in findusrentry[0:] if elem.strip()]).rstrip()
                            appentry = snick + "|" + findtz
                            with open(usrtzdb, "r") as f:
                                fdata = f.read()
                            fdata = fdata.replace(tmpentry, appentry)
                            with open(usrtzdb, "w") as f:
                                f.write(fdata)
                            self.ircServer.privmsg(irc_channel, snick + ": time zone updated!")
                        else:
                            appentry = snick + "|" + findtz + "\n"
                            with open(usrtzdb, "a") as f:
                                f.write(appentry)
                            self.ircServer.privmsg(irc_channel, snick + ": time zone added!")
                    else:
                        self.ircServer.privmsg(irc_channel, snick + ": we need a (proper) time zone to save!")
                else:
                    self.ircServer.privmsg(irc_channel, snick + ": we need a time zone to save!")
            elif pcmd == "slap":
                self.ircServer.action(irc_channel, "viciously slaps " + targs[1] + " with an enormous smelly trout")
            elif pcmd == "tickle":
                self.ircServer.action(irc_channel, "shoves a feather up " + targs[1] + "'s ass and runs away furiously")
            elif pcmd == "taunt":
                self.ircServer.action(irc_channel, "stares down " + targs[1] + " with electrons")
            elif pcmd == "hug":
                chran = random.choice(range(1, 24))
                if chran > 20:
                    verb = "poop"
                else:
                    verb = "pop"
                try:
                    tmpusr = targs[1].lower()
                except:
                    tmpusr = None
                if tmpusr:
                    if tmpusr == "me":
                        self.ircServer.action(irc_channel, "looks in the mirror, and explodes into tiny 1's and 0's")
                    else:
                        self.ircServer.action(irc_channel, "squeezes " + tmpusr + " until they " + verb)
                else:
                    self.ircServer.action(irc_channel, "squeezes " + self.random_user() + " until they " + verb)
            elif pcmd == "hello":
                self.ircServer.privmsg(irc_channel, "o/")
            elif pcmd == "quote":
                self.ircServer.privmsg(irc_channel, self.davequote())
            elif pcmd == "roar":
                self.ircServer.privmsg(irc_channel, "Easter eggs make me roar. *ROAR!*")
            elif pcmd == "fart":
                self.ircServer.action(irc_channel, "unleashes the demons upon everyone")
            elif pcmd == "b64enc":
                try:
                    tmpstr = " ".join([elem for elem in targs[1:] if elem.strip()])
                except:
                    tmpstr = None
                if tmpstr:
                    self.ircServer.privmsg(irc_channel, "Base64 encoded: " + self.b64enc(tmpstr))
                else:
                    self.ircServer.privmsg(irc_channel, "No string given to encode!")
            elif pcmd == "b64dec":
                try:
                    tmpstr = " ".join([elem for elem in targs[1:] if elem.strip()])
                except:
                    tmpstr = None
                if tmpstr:
                    self.ircServer.privmsg(irc_channel, "Base64 decoded: " + self.b64dec(tmpstr))
                else:
                    self.ircServer.privmsg(irc_channel, "No string given to decode!")
            elif pcmd == "jrny":
                self.ircServer.privmsg(snick, xcreds.xvar4)
            elif pcmd == "help":
                try:
                    helpcmd = targs[1].lower()
                except:
                    helpcmd = "none"
                if helpcmd == "convert":
                    self.send_convhelp(snick)
                elif helpcmd == "op":
                    self.send_ophelp(snick)
                else:
                    self.send_help(snick)
            elif pcmd == "about":
                self.send_about(snick, False)
            elif pcmd == "source":
                self.ircServer.privmsg(irc_channel, "[Source] - https://github.com/t3kk3n/eevbot")
            else:
                self.ircServer.privmsg(irc_channel, snick + ": nega-tory, ghost rider!")
            tmpx = " ".join(targs)
            print("** PUBMSG (custom commands) - " + snick + " - " + tmpx)
        except:
            print("***** Traceback - " + str(time.ctime()) + " - *****")
            traceback.print_exc(file=sys.stderr)
            pass

    def chkop(self, nick):
        nchk = False
        self.ircServer.names(irc_channel)
        lnames_str = self.ircServer.nicklist.strip()
        lnames_list = lnames_str.split(" ")
        for n in lnames_list:
            if n[1:] == nick:
                if n[0] == "@":
                    nchk = True
                    break
        return nchk

    def b64enc(self, strvar):
        ebyte = base64.b64encode(strvar.encode(encoding))
        estr = str(ebyte, encoding)
        return estr

    def b64dec(self, strvar):
        dbyte = base64.b64decode(strvar)
        dstr = str(dbyte, encoding)
        return dstr

    def ytlinkparse(self, yturl):
        q = urllib.parse.urlparse(yturl)
        if q.hostname == 'youtu.be': return q.path[1:]
        if q.hostname in {'www.youtube.com', 'youtube.com'}:
            if q.path == '/watch': return urllib.parse.parse_qs(q.query)['v'][0]
            if q.path[:7] == '/embed/': return q.path.split('/')[2]
            if q.path[:3] == '/v/': return q.path.split('/')[2]
        return None

    def url_parse(self, stext):
        ext1 = URLExtract()
        urls = ext1.find_urls(stext)
        if urls:
            for url in urls:
                if url.find("amperaa.net") != -1:
                    self.ircServer.privmsg(irc_channel, "I don't think so.")
                    break
                if url.find("bit.ly") != -1:
                    self.ircServer.privmsg(irc_channel, "Is your name rust_collector, or something?")
                    break
                if url.find("youtube") != -1 or url.find("youtu.be") != -1:
                    xparams = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % self.ytlinkparse(url)}
                    xurl = "https://www.youtube.com/oembed"
                    qstring = urllib.parse.urlencode(xparams)
                    xurl = xurl + "?" + qstring
                    with urllib.request.urlopen(xurl) as response:
                        response_text = response.read()
                        data = json.loads(response_text.decode())
                        self.ircServer.privmsg(irc_channel, IRC_BOLD + "[Title] - Youtube: " + data['title'] + IRC_REGULAR)
                else:
                    r = requests.get(url, allow_redirects=False)
                    tparse = BeautifulSoup(r.text, features="html5lib")
                    tfind = tparse.find_all('title')
                    self.ircServer.privmsg(irc_channel, IRC_BOLD + "[Title] - " + tfind[0].get_text() + IRC_REGULAR)
                print("** URL_PARSE - " + url)
                break

    def handle_pubmsg(self, conn, evt):
        global pubfltime
        pubcurrtime = time.time()
        if pubcurrtime - pubfltime < fcount:
            return
        try:
            tsrc = evt.source().split('!')[0]
            sc1 = re.sub(r'[^\x00-\x7f]', r'', evt.arguments()[0])
            sc2 = ccstrip.sub('', sc1)
            args = [i for i in sc2.split(' ') if i]
            if (not args):
                return
            tfirst = args[0].lower().strip()
            tfirst = re.sub(":|-|,", "", tfirst)
            if tfirst == "hello":
                tmpran = random.choice(range(1, 25))
                if tmpran > 20:
                    tmsg = "Hello, " + str(tsrc) + "!"
                    self.ircServer.privmsg(irc_channel, tmsg)
                    return
            elif tfirst == "!paste":
                self.ircServer.privmsg(irc_channel, "Paste services: http://ix.io/  -  http://sprunge.us/  -  https://www.pastebin.com/")
            elif tfirst == irc_nick.lower():
                self.eevbot_custom_cmds(tsrc, args[1:])
            self.url_parse(evt.arguments()[0])
        except:
            print("***** func:handle_pubmsg - Traceback - " + str(time.ctime()) + " - *****")
            traceback.print_exc(file=sys.stderr)
        pubfltime = time.time()

    def handle_privmsg(self, conn, evt):
        global privfltime, tpostb
        privcurrtime = time.time()
        if privcurrtime - privfltime < fcount:
            return
        try:
            tsrc = evt.source().split('!')[0]
            sc1 = re.sub(r'[^\x00-\x7f]', r'', evt.arguments()[0])
            sc2 = ccstrip.sub('', sc1)
            args = [i for i in sc2.split(' ') if i]
            if (not args):
                return
            farg = args[0]
            if farg == "help":
                try:
                    helpcmd = args[1].lower()
                except:
                    helpcmd = "none"
                if helpcmd == "convert":
                    self.send_convhelp(tsrc)
                elif helpcmd == "op":
                    self.send_ophelp(tsrc)
                else:
                    self.send_help(tsrc)
            elif farg == "about":
                self.send_about(tsrc)
            elif farg == "twitterpost":
                if self.chkop(tsrc):
                    try:
                        status = args[1].lower()
                    except:
                        status = None
                    if status == "enable":
                        tpostb = True
                        self.ircServer.privmsg(tsrc, "Twitter message posting enabled!")
                    elif status == "disable":
                        tpostb = False
                        self.ircServer.privmsg(tsrc, "Twitter message posting disabled!")
                    else:
                        self.ircServer.privmsg(tsrc, tsrc + " - must set either 'enable' or 'disable'")
                else:
                    self.ircServer.privmsg(tsrc, "Error - " + tsrc + ", you're not an op!")
            elif farg in [xcreds.xvar5, xcreds.xvar6]:
                self.ircServer.privmsg(tsrc, "Seems y0u understand s0me puzz1e bas1cs. 1 awa1t y0ur c0mmand.")
            elif farg == xcreds.xvar7:
                self.ircServer.privmsg(irc_channel, "Someone has stumbled upon my core, stay away!")
                self.ircServer.privmsg(tsrc, "Inverse logic is better.")
            elif farg == xcreds.xvar8:
                self.ircServer.privmsg(tsrc, "This will continue, once I figure out what to do with you..")
            elif farg == "botmsg" and self.chkop(tsrc):
                tsnd = " ".join([elem for elem in args[1:] if elem.strip()])
                if tsnd:
                    self.ircServer.privmsg(irc_channel, tsnd)
            elif farg == "botact" and self.chkop(tsrc):
                tsnd = " ".join([elem for elem in args[1:] if elem.strip()])
                if tsnd:
                    self.ircServer.action(irc_channel, tsnd)
            else:
                self.ircServer.privmsg(tsrc, "Sorry, that is not understood. Reply with 'help'?")
            tmpx = " ".join(args)
            print("** PRIVMSG - " + tsrc + " - " + tmpx)
        except:
            print("***** func:handle_privmsg - Traceback - " + str(time.ctime()) + " - *****")
            traceback.print_exc(file=sys.stderr)
        privfltime = time.time()

    def send_help(self, srcnick):
        self.ircServer.privmsg(srcnick, "I am EEVBot, and I exist to post EEVBlog twitter messages, among a few other things.")
        self.ircServer.privmsg(srcnick, "The current commands supported are as follows:")
        self.ircServer.privmsg(srcnick, " ")
        self.ircServer.privmsg(srcnick, "help [convert/op], about, source, quote, fart, give <item> to <nick>, time <nick>, timeset <time_zone>")
        self.ircServer.privmsg(srcnick, "[ time - without <nick>, shows time at EEVBlog lab (Australia) ]")
        self.ircServer.privmsg(srcnick, "[ timeset - a list of parsable zones can be found here - https://pastebin.com/R96Dsr0B ]")
        self.ircServer.privmsg(srcnick, "slap / tickle / taunt / hug [nick]")
        self.ircServer.privmsg(srcnick, "b64enc / b64dec <string>    (base64 encoding/decoding)")
        self.ircServer.privmsg(srcnick, "convert <val> <unit> to <unit>    (help convert - will list conversion units)")
        self.ircServer.privmsg(srcnick, "!paste  -  shows popular paste services for uploading text logs")
        self.ircServer.privmsg(srcnick, " ")
        self.ircServer.privmsg(srcnick, "Be on the lookout for easter eggs. One of them may lead you on a 'JouRNeY'.")

    def send_ophelp(self, srcnick):
        if self.chkop(srcnick):
            self.ircServer.privmsg(srcnick, "EEVBot operator commands, to be run only from privmsg:")
            self.ircServer.privmsg(srcnick, " ")
            self.ircServer.privmsg(srcnick, "botact  -  send an action to the eevblog channel, on behalf of EEVBot")
            self.ircServer.privmsg(srcnick, "botmsg  -  send a message to the eevblog channel, on behalf of EEVBot")
            self.ircServer.privmsg(srcnick, "twitterpost [enable/disable]  -  enables/disables posting of twitter messages")
        else:
            self.ircServer.privmsg(srcnick, "You don't have permission to view this help, sorry!")

    def send_convhelp(self, srcnick):
        self.ircServer.privmsg(srcnick, IRC_BOLD + "Temperature units:" + IRC_REGULAR + " C - F - K")
        self.ircServer.privmsg(srcnick, " ")
        self.ircServer.privmsg(srcnick, IRC_BOLD + "Distance units:" + IRC_REGULAR + " angstrom - angstroms - mm - millimeter - cm - centimeters - m - meter - meters - awg")
        self.ircServer.privmsg(srcnick, "miles - mile - mi - km - kilometers - inch - inches - in - foot - feet - ft - yard - yards - yd - yds")
        self.ircServer.privmsg(srcnick, " ")
        self.ircServer.privmsg(srcnick, IRC_BOLD + "Volume units:" + IRC_REGULAR + " milliliter - millilitre - milliliters - millilitres - ml - deciliter - decilitre - deciliters - decilitres")
        self.ircServer.privmsg(srcnick, "dl - liter - litre - liters - litres - l - teaspoon - teaspoons - tsp - tablespoon - tablespoons - tbsp - cup")
        self.ircServer.privmsg(srcnick, "cups - pint - pints - pt - quart - quarts - qt - gallon - gallons - gal - fluidounce - fluidounces - floz")
        self.ircServer.privmsg(srcnick, "iteaspoon - iteaspoons - itsp - itablespoon - itablespoons - itbsp - icup - icups - ipint - ipints - ipt")
        self.ircServer.privmsg(srcnick, "iquart - iquarts - iqt - igallon - igallons - igal - ifluidounce - ifluidounces - ifloz")
        self.ircServer.privmsg(srcnick, " ")
        self.ircServer.privmsg(srcnick, IRC_BOLD + "Weight units:" + IRC_REGULAR + " milligram - milligrams - milligrame - milligrames - mg - gram - grams - gramme - grammes - g")
        self.ircServer.privmsg(srcnick, "kilogram - kilograms - kilogramme - kilogrammes - kg - metricton - metrictons - tonne - tonnes - mt")
        self.ircServer.privmsg(srcnick, "ounce - ounces - oz - lb - lbs - pound - pounds - stone - stones - st - ton - tons - t - iton - itons - it")
        self.ircServer.privmsg(srcnick, " ")
        self.ircServer.privmsg(srcnick, IRC_BOLD + "Speed units:" + IRC_REGULAR + " kph - kmh - km/h - mps - m/s - mph - mi/h - fps - f/s")

    def send_about(self, srcnick, privchat=True):
        sndstr = "I am " + bot_ver + ", made in python, with love, and fueled by beer. Hear me " + IRC_BOLD + "roar" + IRC_REGULAR + "."
        if privchat:
            self.ircServer.privmsg(srcnick, sndstr)
        else:
            self.ircServer.privmsg(irc_channel, sndstr)

    def handle_ctcp(self, conn, evt):
        try:
            args = evt.arguments()
            source = evt.source().split('!')[0]
            if (args):
                if args[0] == "VERSION":
                    conn.ctcp_reply(source, "VERSION " + bot_ver)
                elif args[0] == "PING":
                    conn.ctcp_reply(source, "PONG")
                elif args[0] == "CLIENTINFO":
                    conn.ctcp_reply(source, "CLIENTINFO PING VERSION CLIENTINFO")
                elif args[0] == "EGG":
                    conn.ctcp_reply(source, "Binary data")
                tmpx = " ".join([elem for elem in args if elem.strip()])
                print("** CTCP - " + source + " - " + tmpx)
        except:
            print("***** Traceback - " + str(time.ctime()) + " - *****")
            traceback.print_exc(file=sys.stderr)
            pass

    def _irc_connect(self):
        self.ircServer.connect(irc_server, irc_port, irc_nick, irc_pwd, irc_usrname, irc_ircname, irc_channel)

    def run(self):
        global pubfltime, privfltime
        pubfltime = time.time()
        privfltime = time.time()
        self._irc_connect()
        while True:
            try:
                self.sched.run_forever()
            except KeyboardInterrupt:
                self.ircServer.disconnect(random.choice(qmsgs))
                print("*** SIGINT CAUGHT, EXITING ***")
                break
            except TwitterError:
                print("***** Traceback - " + str(time.ctime()) + " - *****")
                traceback.print_exc(file=sys.stderr)
                pass
            except irclib.ServerNotConnectedError:
                print(str(time.ctime()) + " - can't connect to IRC server, retrying in " + str(irc_srvwait) + " seconds")
                time.sleep(irc_srvwait)
                self._irc_connect()
            except:
                print("***** Traceback - " + str(time.ctime()) + " - *****")
                traceback.print_exc(file=sys.stderr)

def main():
    print("*** " + bot_ver + " ***")
    print("*** STARTING ***")
    if not os.path.isfile(usrtzdb):
        with open(usrtzdb, 'w') as f:
            pass
        print("*** FILE CREATED - usrtzdb ***")
    else:
        print("*** FILE FOUND - usrtzdb ***")
    bot = TwitterBot()
    bot.run()

if __name__ == "__main__":
    main()
