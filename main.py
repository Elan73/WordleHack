#necessary libraries

import requests
import json
from datetime import date, timedelta

theDay = date.today()

#throwaway variable for keeping track of number of days ahead

i = 0

#opening graphic

print("             )  (   (     (          (   (      (    (                   )  (     ")
print(" (  (     ( /(  )\ ))\ )  )\ )       )\ ))\ )   )\ ) )\ )  (    *   ) ( /(  )\ )  ")
print(" )\))(   ')\())(()/(()/( (()/( (    (()/(()/(( (()/((()/(  )\ ` )  /( )\())(()/( ")
print("((_)()\ )((_)\  /(_))(_)) /(_)))\    /(_))(_))\ /(_))/(_)|((_) ( )(_)|(_)\  /(_))")
print("_(())\_)() ((_)(_))(_))_ (_)) ((_)  (_))(_))((_|_))_(_)) )\___(_(_())  ((_)(_))   ")
print("\ \((_)/ // _ \| _ \|   \| |  | __| | _ \ _ \ __|   \_ _((/ __|_   _| / _ \| _ \ ")
print(" \ \/\/ /| (_) |   /| |) | |__| _|  |  _/   / _|| |) | | | (__  | |  | (_) |   / ")
print("  \_/\_/  \___/|_|_\|___/|____|___| |_| |_|_\___|___/___| \___| |_|   \___/|_|_\ ")
print("")
print("Created by 0xDΛTΛҒRΞΛҜ")
print("")

#program that prints all the data

while i <= 30:
    theDay = theDay + timedelta(1)
    response_API = requests.get("https://www.nytimes.com/svc/wordle/v2/" + str(theDay) + ".json")
    data = response_API.text
    parse_json = json.loads(data)
    print(parse_json['solution'] + " <-- " + str(theDay))
    i = i + 1

#ending graphic

print("")
print("               *    . ")
print("        '  +   ___    @    .")
print("            .-` __`-.   + ")
print("    *      /:.'`__`'.\       '")
print("        . |:: .'_ `. :|   *")
print("   @      |:: '._' : :| .")
print("      +    \:'.__.' :/       '")
print("            /`-...-'\  '   +")
print("   '       /         \   .    @")
print("     *     `-.,___,.-'")
