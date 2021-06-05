#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s

import os

os.system("apt-get update")

os.system("apt-get upgrade")

os.system("apt-get install curl")
           
os.system("apt-get install python")
           
os.system("apt-get install figlet")

os.system("clear")

os.system("figlet Sqwares - Message Sender")

banner = """

 █     █░ ▄▄▄       ██▀███  ▓█████   ██████ 
▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀ ▒██    ▒ 
▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ░ ▓██▄   
░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒
░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒▒██████▒▒
░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░
  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░
  ░   ░    ░   ▒     ░░   ░    ░   ░  ░  ░  
    ░          ░  ░   ░        ░  ░      ░  
                                            
  You can only send one message per day. Sqwares#4767                                     
"""

print(banner)

sor = input("Tel address Ex:+9055315269 >>> ")

mesaj = input("your message >>> ")

arlk = mesaj[0:70]

print("\n| The Sendable part of your message is as follows.\n"+arlk)

drlm = input("\n| Send Your Message?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|you made a mistake.")
