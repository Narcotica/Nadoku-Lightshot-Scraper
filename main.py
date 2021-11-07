#Lightshot url scraper by Akiko#4200
#https://github.com/uAkiko

from colored import fg
import os
import time
import string
import random


f = open("urls.txt", "w")
f.write("")
os.system("title Nadoku - Akiko#4200")
color = fg("118")

print(color + """
██▄▄▄▄      ▄████████ ████████▄   ▄██████▄     ▄█   ▄█▄ ███    █▄  """)
time.sleep(0.2)
print("███▀▀▀██▄   ███    ███ ███   ▀███ ███    ███   ███ ▄███▀ ███    ███ ")
time.sleep(0.2)
print("███   ███   ███    ███ ███    ███ ███    ███   ███▐██▀   ███    ███  ")
time.sleep(0.2)
print("███   ███   ███    ███ ███    ███ ███    ███  ▄█████▀    ███    ███  ")
time.sleep(0.2)
print("███   ███   ███    ███ ███    ███ ███    ███  ▄█████▀    ███    ███   ")
time.sleep(0.2)
print("███   ███ ▀███████████ ███    ███ ███    ███ ▀▀█████▄    ███    ███  ")
time.sleep(0.2)
print("███   ███   ███    ███ ███    ███ ███    ███   ███▐██▄   ███    ███  ")
time.sleep(0.2)
print("███   ███   ███    ███ ███   ▄███ ███    ███   ███ ▀███▄ ███    ███ ")
time.sleep(0.2)
print(" ▀█   █▀    ███    █▀  ████████▀   ▀██████▀    ███   ▀█▀ ████████▀  ")
time.sleep(0.2)
print("                                               ▀      ")

input("Press ENTER to start...")

os.system("cls")
while True:
    def randomstring(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))

        url = "https://prnt.sc/" + result_str
        print("[+] " + str(url))
        ff = open("urls.txt", "a")
        ff.write(url + "\n")
    randomstring(6)

    time.sleep(1)
