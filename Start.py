# coding: utf—8
import os,sys,time


def bersih():
	os.system('clear')


usr='JHANCOK'
pwd='Mr.Wafa'
def login():
    bersih()
    print('\033[1;34m+\033[1;31m--------------------------------------------------\033[1;34m+')
    print('\033[1;31mFollow \033[1;37mGithub')
    os.system('xdg-open https://github.com/Wafa894')
    print('\033[1;34m+\033[1;31m---------------------------------------------------\033[1;34m+')
    x = raw_input("\033[1;31m[?]Username \033[1;37m:")
    y = raw_input("\033[1;31m[?]Password \033[1;37m:")
    if x==usr and y==pwd:
	print("\033[1;14mLogin Berhasil!!")
	time.sleep(1)
	bersih()
    elif x=="" and y=="":
	print("\033[1;31mJangan Kosong!!")
	os.system("python2 Start.py")
    else:
	print("\033[1;37mPassword Salah!!")
	print("Hubungi Mr.Wafa 082255263724 !!")
	time.sleep(3)
	os.system("python2 Start.py")



login()


def menu():
    print "+----------------------------------------------+"
    print "Author : Wafa"
    print "Youtube : Nanti Gw Buat :v"
    print "Github : https://github.com/Wafa894"
    print "+----------------------------------------------+"
    print " [1] Install Nmap (No Root)"
    print " [2] Install Metasploit (No Root)"
    print " [3] Install Hack Wifi (Root)"
    print " [0] Keluar/Exit"
    pil = raw_input("Pilih Sesuai Nomor -> ")
    if pil =="1":
	os.system("pkg install unstable-repo")
	os.system("pkg install nmap")
	os.system("python2 Bernyanyi.py")
    elif pil =="2":
	os.system("pkg update && pkg upgrade")
	os.system("pkg install python -y")
	os.system("pkg install git -y")
	os.system("gem install lolcat")
	os.system("git clone https://github.com/noob-hackers/m-wiz")
	os.system("cd m-wiz")
	os.system("ls")
	os.system("bash m-wiz.sh")
	os.system("cd")
	os.system("msfconsole")
	os.system("python2 Bernyanyi.py")
    elif pil =="3":
	os.system("apt update")
	os.system("apt upgrade")
	os.system("apt install wget")
	os.system("apt install proot")
	os.system("pkg install curl")
	os.system("pkg install clang")
	os.system("pkg install tsudo")
	os.system("pkg install tsu")
	os.system("git clone https://github.com/kumpulanremaja/wifi")
	os.system("cd wifi")
	os.system("chmod +x wifi.sh")
	os.system("sh wifi.sh")
	os.system("python2 Bernyanyi.py")
    elif pil =="0":
        sys.exit()
menu()
