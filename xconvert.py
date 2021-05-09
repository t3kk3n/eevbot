import math

temp_vars = ("c", "f", "k")

dist_vars = ("angstrom", "angstroms", "mm", "millimeter", "cm", "centimeters", "m", "meter", "meters", "km", "kilometers",
    "awg", "inch", "inches", "in", "foot", "feet", "ft", "yard", "yards", "yd", "yds", "miles", "mile", "mi")

vol_vars = ("milliliter", "millilitre", "milliliters", "millilitres", "ml", "deciliter", "decilitre", "deciliters", "decilitres",
    "dl", "liter", "litre", "liters", "litres", "l", "teaspoon", "teaspoons", "tsp", "tablespoon", "tablespoons", "tbsp", "cup",
    "cups", "pint", "pints", "pt", "quart", "quarts", "qt", "gallon", "gallons", "gal", "fluidounce", "fluidounces", "floz",
    "iteaspoon", "iteaspoons", "itsp", "itablespoon", "itablespoons", "itbsp", "icup", "icups", "ipint", "ipints", "ipt", "iquart",
    "iquarts", "iqt", "igallon", "igallons", "igal", "ifluidounce", "ifluidounces", "ifloz")

weight_vars = ("milligram", "milligrams", "milligrame", "milligrames", "mg", "gram", "grams", "gramme", "grammes", "g", "kilogram",
    "kilograms", "kilogramme", "kilogrammes", "kg", "metricton", "metrictons", "tonne", "tonnes", "mt", "ounce", "ounces", "oz", "lb",
    "lbs", "pound", "pounds", "stone", "stones", "st", "ton", "tons", "t", "iton", "itons", "it")

speed_vars = ("kph", "kmh", "km/h", "mps", "m/s", "mph", "mi/h", "fps", "f/s")

#time_vars = ("nanosecond", "nanoseconds", "ns", "microsecond", "microseconds", "us", "millisecond", "milliseconds", "ms", "sec", "secs",
#    "second", "seconds", "minute", "minutes", "min", "mins", "hour", "hours", "hr", "hrs", "day", "days", "week", "weeks", "year", "years")

#power_vars = ("joule", "joules", "j", "kilowatthour", "kilowatthours", "kwh", "kw/h", "kcal", "kcalorie", "kcalories", "kilocalorie",
#    "kilocalories", "calorie", "calories", "britishthermalunit", "britishthermalunits", "btu", "btus", "electronvolt", "electronvolts", "ev",
#    "newton", "newtons", "n", "poundforce", "lbf", "newtonmeter", "newtonmeters", "nm", "newtonmetre", "newtonmetres", "footpound", "footpounds",
#    "lbft", "poundfoot", "poundfeet")

rndval = 3
invstr = "Invalid"

def func_temp(v, f, t):
    if f == "c":
        if t == "f":
            retval = round((v * 9/5) + 32, rndval)
        elif t == "k":
            retval = round(v + 273.15, rndval)
        elif t == "c":
            retval = round(v, rndval)
        else:
            retval = invstr
    elif f == "f":
        if t == "c":
            retval = round((v - 32) * 5/9, rndval)
        elif t == "k":
            retval = round(((v - 32) * 5/9) + 273.15, rndval)
        elif t == "f":
            retval = round(v, rndval)
        else:
            retval = invstr
    elif f == "k":
        if t == "c":
            retval = round(v - 273.15, rndval)
        elif t == "f":
            retval = round((v - 273.15) * 9/5 + 32, rndval)
        elif t == "k":
            retval = round(v, rndval)
        else:
            retval = invstr
    else:
        retval = invstr
    return(str(retval))

def func_dist(v, f, t):
    if f in ("angstrom", "angstroms"):
        if t == "awg":
            retval = (-39 * (math.log((v * 0.00000000393701) / 0.005) / math.log(92)) + 36)
        elif t in ("mm", "millimeter"):
            retval = (v * 0.0000001)
        elif t in ("cm", "centimeters"):
            retval = (v * 0.00000001)
        elif t in ("m", "meter", "meters"):
            retval = (v * 0.0000000001)
        elif t in ("km", "kilometers"):
            retval = (v * 0.0000000000001)
        elif t in ("in", "inch", "inches"):
            retval = (v * 0.00000000393701)
        elif t in ("ft", "feet", "foot"):
            retval = (v * 0.000000000328084)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = (v * 0.000000000109361)
        elif t in ("mi", "mile", "miles"):
            retval = (v * 0.0000000000000621371)
        elif t in ("angstrom", "angstroms"):
            retval = v
        else:
            retval = invstr
    elif f in ("mm", "millimeter"):
        if t == "awg":
            retval = (-39 * (math.log((v * 0.0393701) / 0.005) / math.log(92)) + 36)
        elif t in ("angstrom", "angstroms"):
            retval = (v * 10000000)
        elif t in ("cm", "centimeters"):
            retval = (v / 10)
        elif t in ("m", "meter", "meters"):
            retval = (v / 1000)
        elif t in ("km", "kilometers"):
            retval = (v / 1000000)
        elif t in ("in", "inch", "inches"):
            retval = (v * 0.0393701)
        elif t in ("ft", "feet", "foot"):
            retval = (v * 0.00328084)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = (v * 0.00109361)
        elif t in ("mi", "mile", "miles"):
            retval = (v * 0.000000621371)
        elif t in ("mm", "millimeter"):
            retval = v
        else:
            retval = invstr
    elif f in ("cm", "centimeters"):
        if t == "awg":
            retval = (-39 * (math.log((v * 0.393701) / 0.005) / math.log(92)) + 36)
        elif t in ("mm", "millimeter"):
            retval = (v * 10)
        elif t in ("angstrom", "angstroms"):
            retval = (v * 100000000)
        elif t in ("m", "meter", "meters"):
            retval = (v / 100)
        elif t in ("km", "kilometers"):
            retval = (v / 100000)
        elif t in ("in", "inch", "inches"):
            retval = (v * 0.393701)
        elif t in ("ft", "feet", "foot"):
            retval = (v * 0.0328084)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = (v * 0.0109361)
        elif t in ("mi", "mile", "miles"):
            retval = (v * 0.00000621371)
        elif t in ("cm", "centimeters"):
            retval = v
        else:
            retval = invstr
    elif f in ("m", "meter", "meters"):
        if t == "awg":
            retval = (-39 * (math.log((v * 39.3701) / 0.005) / math.log(92)) + 36)
        elif t in ("mm", "millimeter"):
            retval = (v * 1000)
        elif t in ("cm", "centimeters"):
            retval = (v * 100)
        elif t in ("angstrom", "angstroms"):
            retval = (v * 10000000000)
        elif t in ("km", "kilometers"):
            retval = (v / 1000)
        elif t in ("in", "inch", "inches"):
            retval = (v * 39.3701)
        elif t in ("ft", "feet", "foot"):
            retval = (v * 3.28084)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = (v * 1.09361)
        elif t in ("mi", "mile", "miles"):
            retval = (v * 0.000621371)
        elif t in ("m", "meter", "meters"):
            retval = v
        else:
            retval = invstr
    elif f in ("km", "kilometers"):
        if t == "awg":
            retval = (-39 * (math.log((v * 39370.1) / 0.005) / math.log(92)) + 36)
        elif t in ("mm", "millimeter"):
            retval = (v * 1000000)
        elif t in ("cm", "centimeters"):
            retval = (v * 100000)
        elif t in ("m", "meter", "meters"):
            retval = (v * 1000)
        elif t in ("angstrom", "angstroms"):
            retval = (v * 10000000000000)
        elif t in ("in", "inch", "inches"):
            retval = (v * 39370.1)
        elif t in ("ft", "feet", "foot"):
            retval = (v * 3280.84)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = (v * 1093.61)
        elif t in ("mi", "mile", "miles"):
            retval = (v * 0.621371)
        elif t in ("km", "kilometers"):
            retval = v
        else:
            retval = invstr
    elif f in ("in", "inch", "inches"):
        if t == "awg":
            retval = (-39 * (ath.log((v) / 0.005) / math.log(92)) + 36)
        elif t in ("mm", "millimeter"):
            retval = (v * 25.4)
        elif t in ("cm", "centimeters"):
            retval = (v * 2.54)
        elif t in ("m", "meter", "meters"):
            retval = (v * 0.0254)
        elif t in ("k", "kilometers"):
            retval = (v * 0.0000254)
        elif t in ("angstrom", "angstroms"):
            retval = (v * 254000000)
        elif t in ("ft", "feet", "foot"):
            retval = (v / 12)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = (v / 36)
        elif t in ("mi", "mile", "miles"):
            retval = (v / 63360)
        elif t in ("in", "inch", "inches"):
            retval = v
        else:
            retval = invstr
    elif f in ("ft", "feet", "foot"):
        if t == "awg":
            retval = (-39 * (math.log((v * 12) / 0.005) / math.log(92)) + 36)
        elif t in ("mm", "millimeter"):
            retval = (v * 304.8)
        elif t in ("cm", "centimeters"):
            retval = (v * 30.48)
        elif t in ("m", "meter", "meters"):
            retval = (v * 0.3048)
        elif t in ("km", "kilometers"):
            retval = (v * 0.0003048)
        elif t in ("in", "inch", "inches"):
            retval = (v * 12)
        elif t in ("angstrom", "angstroms"):
            retval = (v * 3048000000)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = (v / 3)
        elif t in ("mi", "mile", "miles"):
            retval = (v / 5280)
        elif t in ("ft", "feet", "foot"):
            retval = v
        else:
            retval = invstr
    elif f in ("yd", "yds", "yard", "yards"):
        if t == "awg":
            retval = (-39 * (math.log((v * 36) / 0.005) / math.log(92)) + 36)
        elif t in ("mm", "millimeter"):
            retval = (v * 914.4)
        elif t in ("cm", "centimeters"):
            retval = (v * 91.44)
        elif t in ("m", "meter", "meters"):
            retval = (v * 0.9144)
        elif t in ("km", "kilometers"):
            retval = (v * 0.0009144)
        elif t in ("in", "inch", "inches"):
            retval = (v * 36)
        elif t in ("ft", "feet", "foot"):
            retval = (v * 3)
        elif t in ("angstrom", "angstroms"):
            retval = (v * 9144000000)
        elif t in ("mi", "mile", "miles"):
            retval = (v / 1760)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = v
        else:
            retval = invstr
    elif f in ("mi", "mile", "miles"):
        if t == "awg":
            retval = (-39 * (math.log((v * 63360) / 0.005) / math.log(92)) + 36)
        elif t in ("mm", "millimeter"):
            retval = (v * 1609000)
        elif t in ("cm", "centimeters"):
            retval = (v * 160934)
        elif t in ("m", "meter", "meters"):
            retval = (v * 1609.34)
        elif t in ("km", "kilometers"):
            retval = (v * 1.60934)
        elif t in ("in", "inch", "inches"):
            retval = (v * 63360)
        elif t in ("ft", "feet", "foot"):
            retval = (v * 5280)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = (v * 1760)
        elif t in ("angstrom", "angstroms"):
            retval = (v * 16090000000000)
        elif t in ("mi", "mile", "miles"):
            retval = v
        else:
            retval = invstr
    elif f == "awg":
        if t in ("angstrom", "angstroms"):
            retval = (0.005 * math.pow(92, (36 - v) / 39) * 254000000)
        elif t in ("mm", "millimeter"):
            retval = (0.005 * math.pow(92, (36 - v) / 39) * 25.4)
        elif t in ("cm", "centimeters"):
            retval = (0.005 * math.pow(92, (36 - v) / 39) * 2.54)
        elif t in ("m", "meter", "meters"):
            retval = (0.005 * math.pow(92, (36 - v) / 39) * 0.0254)
        elif t in ("km", "kilometers"):
            retval = (0.005 * math.pow(92, (36 - v) / 39) * 0.0000254)
        elif t in ("in", "inch", "inches"):
            retval = (0.005 * math.pow(92, (36 - v) / 39.0))
        elif t in ("ft", "feet", "foot"):
            retval = (0.005 * math.pow(92, (36 - v) / 39) / 12)
        elif t in ("yd", "yds", "yard", "yards"):
            retval = (0.005 * math.pow(92, (36 - v) / 39) / 36)
        elif t in ("mi", "mile", "miles"):
            retval = (0.005 * math.pow(92, (36 - v) / 39) / 63360)
        elif t == "awg":
            retval = v
        else:
            retval = invstr
    else:
        retval = invstr
    return(str(retval))

def func_vol(v, f, t):
    if f in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
        if t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v  * 0.0351951)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 0.01)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.001)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 0.202884)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 0.067628)
        elif t in ("cup", "cups"):
            retval = (v * 0.00422675)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 0.00211338)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 0.00105669)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 0.000264172)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 0.033814)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 0.168936)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 0.0563121)
        elif t in ("icup", "icups"):
            retval = (v * 0.00351951)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 0.00175975)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 0.000879877)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.000219969)
        elif t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = v
        else:
            retval = invstr
    elif f in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 100)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 3.51951)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.1)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 20.2884)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 6.7628)
        elif t in ("cup", "cups"):
            retval = (v * 0.422675)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 0.211338)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 0.105669)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 0.0264172)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 3.3814)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 16.8936)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 5.63121)
        elif t in ("icup", "icups"):
            retval = (v * 0.351951)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 0.175975)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 0.0879877)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.0219969)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = v
        else:
            retval = invstr
    elif f in ("l", "liter", "litre", "liters", "litres"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 1000)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 10)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 35.1951)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 202.884)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 67.628)
        elif t in ("cup", "cups"):
            retval = (v * 4.22675)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 2.11338)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 1.05669)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 0.264172)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 33.814)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 168.936)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 56.3121)
        elif t in ("icup", "icups"):
            retval = (v * 3.51951)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 1.75975)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 0.879877)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.219969)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = v
        else:
            retval = invstr
    elif f in ("tsp", "teaspoon", "teaspoons"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 4.92892)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 0.0492892)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.00492892)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 0.173474)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v / 3)
        elif t in ("cup", "cups"):
            retval = (v / 48)
        elif t in ("pt", "pint", "pints"):
            retval = (v / 96)
        elif t in ("qt", "quart", "quarts"):
            retval = (v / 192)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v / 768)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v / 6)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 0.832674)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 0.277558)
        elif t in ("icup", "icups"):
            retval = (v * 0.0173474)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 0.00867369)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 0.00433684)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.00108421)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = v
        else:
            retval = invstr
    elif f in ("tbsp", "tablespoon", "tablespoons"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 14.7868)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 0.147868)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.0147868)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 3)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 0.520421)
        elif t in ("cup", "cups"):
            retval = (v / 16)
        elif t in ("pt", "pint", "pints"):
            retval = (v / 32)
        elif t in ("qt", "quart", "quarts"):
            retval = (v / 64)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v / 256)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v / 2)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 2.49802)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 0.832674)
        elif t in ("icup", "icups"):
            retval = (v * 0.0520421)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 0.0260211)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 0.0130105)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.00325263)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = v
        else:
            retval = invstr
    elif f in ("cup", "cups"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 236.588)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 2.36588)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.236588)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 48)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 16)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 8.32674)
        elif t in ("pt", "pint", "pints"):
            retval = (v / 2)
        elif t in ("qt", "quart", "quarts"):
            retval = (v / 4)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v / 16)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 8)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 39.9683)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 13.3228)
        elif t in ("icup", "icups"):
            retval = (v * 0.832674)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 0.416337)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 0.208169)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.0520421)
        elif t in ("cup", "cups"):
            retval = v
        else:
            retval = invstr
    elif f in ("pt", "pint", "pints"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 473.176)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 4.73176)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.473176)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 96)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 32)
        elif t in ("cup", "cups"):
            retval = (v * 2)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 16.6535)
        elif t in ("qt", "quart", "quarts"):
            retval = (v / 2)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v / 8)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 16)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 79.9367)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 26.6456)
        elif t in ("icup", "icups"):
            retval = (v * 1.66535)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 0.832674)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 0.416337)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.104084)
        elif t in ("pt", "pint", "pints"):
            retval = v
        else:
            retval = invstr
    elif f in ("qt", "quart", "quarts"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 946.353)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 9.46353)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.946353)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 192)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 64)
        elif t in ("cup", "cups"):
            retval = (v * 4)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 2)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 33.307)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v / 4)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 32)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 159.873)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 53.2911)
        elif t in ("icup", "icups"):
            retval = (v * 3.3307)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 1.66535)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 0.832674)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.208169)
        elif t in ("qt", "quart", "quarts"):
            retval = v
        else:
            retval = invstr
    elif f in ("gal", "gallon", "gallons"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 3785.41)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 37.8541)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 3.78541)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 768)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 256)
        elif t in ("cup", "cups"):
            retval = (v * 16)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 8)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 4)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 133.228)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 128)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 639.494)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 213.165)
        elif t in ("icup", "icups"):
            retval = (v * 13.3228)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 6.66139)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 3.3307)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.832674)
        elif t in ("gal", "gallon", "gallons"):
            retval = v
        else:
            retval = invstr
    elif f in ("floz", "fluidounce", "fluidounces"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 29.5735)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 0.295735)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.0295735)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 6)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 2)
        elif t in ("cup", "cups"):
            retval = (v / 8)
        elif t in ("pt", "pint", "pints"):
            retval = (v / 16)
        elif t in ("qt", "quart", "quarts"):
            retval = (v / 32)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v / 128)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 1.04084)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 4.99604)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 1.66535)
        elif t in ("icup", "icups"):
            retval = (v * 0.104084)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 0.0520421)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 0.0260211)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v * 0.00650527)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = v
        else:
            retval = invstr
    elif f in ("itsp", "iteaspoon", "iteaspoons"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 5.91939)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 0.0591939)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.00591939)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 1.20095)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 0.400317)
        elif t in ("cup", "cups"):
            retval = (v * 0.0250198)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 0.0125099)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 0.00625495)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 0.00156374)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 0.200158)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v / 4.8)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v / 3)
        elif t in ("icup", "icups"):
            retval = (v / 48)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v / 96)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v / 192)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v / 768)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = v
        else:
            retval = invstr
    elif f in ("itbsp", "itablespoon", "itablespoons"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 17.7582)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 0.177582)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.0177582)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 3.60285)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 1.20095)
        elif t in ("cup", "cups"):
            retval = (v * 0.0750594)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 0.0375297)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 0.0187649)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 0.00469121)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 0.600475)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 3)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v / 1.6)
        elif t in ("icup", "icups"):
            retval = (v / 16)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v / 32)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v / 64)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v / 256)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = v
        else:
            retval = invstr
    elif f in ("icup", "icups"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 284.131)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 2.84131)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.284131)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 57.6456)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 19.2152)
        elif t in ("cup", "cups"):
            retval = (v * 1.20095)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 0.600475)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 0.300237)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 0.0750594)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 9.6076)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 48)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 16)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 10)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v / 2)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v / 4)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v / 16)
        elif t in ("icup", "icups"):
            retval = v
        else:
            retval = invstr
    elif f in ("ipt", "ipint", "ipints"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 568.261)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 5.68261)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.568261)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 115.291)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 38.4304)
        elif t in ("cup", "cups"):
            retval = (v * 2.4019)
        elif t in ("pt", "pint", "pints"):
            retval = (v  * 1.20095)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 0.600475)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 0.150119)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 19.2152)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 96)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 32)
        elif t in ("icup", "icups"):
            retval = (v * 2)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 20)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v / 2)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v / 8)
        elif t in ("ipt", "ipint", "ipints"):
            retval = v
        else:
            retval = invstr
    elif f in ("iqt", "iquart", "iquarts"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 1136.52)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 11.3652)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 1.13652)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 230.582)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 76.8608)
        elif t in ("cup", "cups"):
            retval = (v * 4.8038)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 2.4019)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 1.20095)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 0.300237)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 38.4304)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 192)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 64)
        elif t in ("icup", "icups"):
            retval = (v * 4)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 2)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 40)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v / 4)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = v
        else:
            retval = invstr
    elif f in ("igal", "igallon", "igallons"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 4546.09)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 45.4609)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 4.54609)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 922.33)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 307.443)
        elif t in ("cup", "cups"):
            retval = (v * 19.2152)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 9.6076)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 4.8038)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 1.20095)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 153.722)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 768)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 256)
        elif t in ("icup", "icups"):
            retval = (v * 16)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v * 8)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v * 4)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = (v * 160)
        elif t in ("igal", "igallon", "igallons"):
            retval = v
        else:
            retval = invstr
    elif f in ("ifloz", "ifluidounce", "ifluidounces"):
        if t in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
            retval = (v * 28.4131)
        elif t in ("dl", "deciliter", "decilitre", "deciliters", "decilitres"):
            retval = (v * 0.284131)
        elif t in ("l", "liter", "litre", "liters", "litres"):
            retval = (v * 0.0284131)
        elif t in ("tsp", "teaspoon", "teaspoons"):
            retval = (v * 5.76456)
        elif t in ("tbsp", "tablespoon", "tablespoons"):
            retval = (v * 1.92152)
        elif t in ("cup", "cups"):
            retval = (v * 0.120095)
        elif t in ("pt", "pint", "pints"):
            retval = (v * 0.0600475)
        elif t in ("qt", "quart", "quarts"):
            retval = (v * 0.0300237)
        elif t in ("gal", "gallon", "gallons"):
            retval = (v * 0.00750594)
        elif t in ("floz", "fluidounce", "fluidounces"):
            retval = (v * 0.96076)
        elif t in ("itsp", "iteaspoon", "iteaspoons"):
            retval = (v * 4.8)
        elif t in ("itbsp", "itablespoon", "itablespoons"):
            retval = (v * 1.6)
        elif t in ("icup", "icups"):
            retval = (v / 10)
        elif t in ("ipt", "ipint", "ipints"):
            retval = (v / 20)
        elif t in ("iqt", "iquart", "iquarts"):
            retval = (v / 40)
        elif t in ("igal", "igallon", "igallons"):
            retval = (v / 160)
        elif t in ("ifloz", "ifluidounce", "ifluidounces"):
            retval = v
        else:
            retval = invstr
    else:
        retval = invstr
    return(str(retval))

def func_weight(v, f, t):
    if f in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
        if t in ("it", "iton", "itons"):
            retval = (v * 0.000000000984207)
        elif t in ("g", "gram", "grams", "gramme", "grammes"):
            retval = (v * 0.001)
        elif t in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
            retval = (v * 0.000001)
        elif t in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
            retval = (v * 0.000000001)
        elif t in ("oz", "ounce", "ounces"):
            retval = (v * 0.000035274)
        elif t in ("lb", "lbs", "pound", "pounds"):
            retval = (v * 0.00000220462)
        elif t in ("st", "stone", "stones"):
            retval = (v * 0.000000157473)
        elif t in ("t", "ton", "tons"):
            retval = (v * 0.00000000110231)
        elif t in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
            retval = v
        else:
            retval = invstr
    elif f in ("g", "gram", "grams", "gramme", "grammes"):
        if t in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
            retval = (v * 1000)
        elif t in ("it", "iton", "itons"):
            retval = (v * 0.000000984207)
        elif t in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
            retval = (v * 0.001)
        elif t in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
            retval = (v * 0.000001)
        elif t in ("oz", "ounce", "ounces"):
            retval = (v * 0.035274)
        elif t in ("lb", "lbs", "pound", "pounds"):
            retval = (v * 0.00220462)
        elif t in ("st", "stone", "stones"):
            retval = (v * 0.000157473)
        elif t in ("t", "ton", "tons"):
            retval = (v * 0.00000110231)
        elif t in ("g", "gram", "grams", "gramme", "grammes"):
            retval = v
        else:
            retval = invstr
    elif f in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
        if t in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
            retval = (v * 1000000)
        elif t in ("g", "gram", "grams", "gramme", "grammes"):
            retval = (v * 1000)
        elif t in ("it", "iton", "itons"):
            retval = (v * 0.000984207)
        elif t in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
            retval = (v * 0.001)
        elif t in ("oz", "ounce", "ounces"):
            retval = (v * 35.274)
        elif t in ("lb", "lbs", "pound", "pounds"):
            retval = (v * 2.20462)
        elif t in ("st", "stone", "stones"):
            retval = (v * 0.157473)
        elif t in ("t", "ton", "tons"):
            retval = (v * 0.00110231)
        elif t in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
            retval = v
        else:
            retval = invstr
    elif f in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
        if t in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
            retval = (v * 1000000000)
        elif t in ("g", "gram", "grams", "gramme", "grammes"):
            retval = (v * 1000000)
        elif t in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
            retval = (v * 1000)
        elif t in ("it", "iton", "itons"):
            retval = (v * 0.984207)
        elif t in ("oz", "ounce", "ounces"):
            retval = (v * 35274)
        elif t in ("lb", "lbs", "pound", "pounds"):
            retval = (v * 2204.62)
        elif t in ("st", "stone", "stones"):
            retval = (v * 157.473)
        elif t in ("t", "ton", "tons"):
            retval = (v * 1.10231)
        elif t in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
            retval = v
        else:
            retval = invstr
    elif f in ("oz", "ounce", "ounces"):
        if t in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
            retval = (v * 28349.5)
        elif t in ("g", "gram", "grams", "gramme", "grammes"):
            retval = (v * 28.3495)
        elif t in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
            retval = (v * 0.0283495)
        elif t in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
            retval = (v * 0.0000283495)
        elif t in ("it", "iton", "itons"):
            retval = (v / 35840)
        elif t in ("lb", "lbs", "pound", "pounds"):
            retval = (v / 16)
        elif t in ("st", "stone", "stones"):
            retval = (v / 224)
        elif t in ("t", "ton", "tons"):
            retval = (v / 32000)
        elif t in ("oz", "ounce", "ounces"):
            retval = v
        else:
            retval = invstr
    elif f in ("lb", "lbs", "pound", "pounds"):
        if t in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
            retval = (v * 453592)
        elif t in ("g", "gram", "grams", "gramme", "grammes"):
            retval = (v * 453.592)
        elif t in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
            retval = (v * 0.453592)
        elif t in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
            retval = (v * 0.000453592)
        elif t in ("oz", "ounce", "ounces"):
            retval = (v * 16)
        elif t in ("it", "iton", "itons"):
            retval = (v / 2240)
        elif t in ("st", "stone", "stones"):
            retval = (v / 14)
        elif t in ("t", "ton", "tons"):
            retval = (v / 2000)
        elif t in ("lb", "lbs", "pound", "pounds"):
            retval = v
        else:
            retval = invstr
    elif f in ("st", "stone", "stones"):
        if t in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
            retval = (v * 6350000)
        elif t in ("g", "gram", "grams", "gramme", "grammes"):
            retval = (v * 6350.29)
        elif t in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
            retval = (v * 6.35029)
        elif t in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
            retval = (v * 0.00635029)
        elif t in ("oz", "ounce", "ounces"):
            retval = (v * 224)
        elif t in ("lb", "lbs", "pound", "pounds"):
            retval = (v * 14)
        elif t in ("it", "iton", "itons"):
            retval = (v / 160)
        elif t in ("t", "ton", "tons"):
            retval = (v * 0.007)
        elif t in ("st", "stone", "stones"):
            retval = v
        else:
            retval = invstr
    elif f in ("t", "ton", "tons"):
        if t in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
            retval = (v * 907200000)
        elif t in ("g", "gram", "grams", "gramme", "grammes"):
            retval = (v *  907185)
        elif t in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
            retval = (v * 907.185)
        elif t in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
            retval = (v * 0.907185)
        elif t in ("oz", "ounce", "ounces"):
            retval = (v * 32000)
        elif t in ("lb", "lbs", "pound", "pounds"):
            retval = (v * 2000)
        elif t in ("st", "stone", "stones"):
            retval = (v * 142.857)
        elif t in ("it", "iton", "itons"):
            retval = (v / 1.12)
        elif t in ("t", "ton", "tons"):
            retval = v
        else:
            retval = invstr
    elif f in ("it", "iton", "itons"):
        if t in ("mg", "milligram", "milligrams", "milligrame", "milligrames"):
            retval = (v * 1016000000)
        elif t in ("g", "gram", "grams", "gramme", "grammes"):
            retval = (v * 1016000)
        elif t in ("kg", "kilogram", "kilograms", "kilogramme", "kilogrammes"):
            retval = (v * 1016.05)
        elif t in ("mt", "metricton", "metrictons", "tonne", "tonnes"):
            retval = (v * 1.01605)
        elif t in ("oz", "ounce", "ounces"):
            retval = (v * 35840)
        elif t in ("lb", "lbs", "pound", "pounds"):
            retval = (v * 2240)
        elif t in ("st", "stone", "stones"):
            retval = (v * 160)
        elif t in ("t", "ton", "tons"):
            retval = (v * 1.12)
        elif t in ("it", "iton", "itons"):
            retval = v
        else:
            retval = invstr
    else:
        retval = invstr
    return(str(retval))

def func_speed(v, f, t):
    if f in ("kph", "kmh", "km/h"):
        if t in ("mps", "m/s"):
            retval = (v / 3.6)
        elif t in ("mph", "mi/h"):
            retval = (v * 0.621371)
        elif t in ("fps", "f/s"):
            retval = (v * 0.911344)
        elif t in ("kph", "kmh", "km/h"):
            retval = v
        else:
            retval = invstr
    elif f in ("mps", "m/s"):
        if t in ("kph", "kmh", "km/h"):
            retval = (v * 3.6)
        elif t in ("mph", "mi/h"):
            retval = (v * 2.23694)
        elif t in ("fps", "f/s"):
            retval = (v * 3.28084)
        elif t in ("mps", "m/s"):
            retval = v
        else:
            retval = invstr
    elif f in ("mph", "mi/h"):
        if t in ("kph", "kmh", "km/h"):
            retval = (v * 1.60934)
        elif t in ("mps", "m/s"):
            retval = (v * 0.44704)
        elif t in ("fps", "f/s"):
            retval = (v * 1.46667)
        elif t in ("mph", "mi/h"):
            retval = v
        else:
            retval = invstr
    elif f in ("fps", "f/s"):
        if t in ("kph", "kmh", "km/h"):
            retval = (v * 1.09728)
        elif t in ("mps", "m/s"):
            retval = (v * 0.3048)
        elif t in ("mph", "mi/h"):
            retval = (v * 0.681818)
        elif t in ("fps", "f/s"):
            retval = v
        else:
            retval = invstr
    else:
        retval = invstr
    return(str(retval))
