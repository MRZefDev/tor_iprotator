import time
import requests
import os
import sys
from stem import Signal
from stem.control import Controller

def get_strings(lang):
    strings = {
        "en": {
            "root_error": "ERROR: This script must be run as root (sudo).",
            "kill_switch_on": "[!] Kill Switch Active: Only Tor traffic is allowed.",
            "kill_switch_off": "[!] Kill Switch Disabled: Normal access restored.",
            "active_ip": "[*] Active Anonymous IP: ",
            "renewing": "[+] Renewing identity, switching to new IP...",
            "exit": "\n[!] System restored. Exiting..."
        },
        "tr": {
            "root_error": "HATA: Bu script root yetkisi (sudo) ile çalıştırılmalıdır.",
            "kill_switch_on": "[!] Kill Switch Aktif: Sadece Tor trafiğine izin veriliyor.",
            "kill_switch_off": "[!] Kill Switch Devre Dışı: Normal erişim açıldı.",
            "active_ip": "[*] Aktif Anonim IP: ",
            "renewing": "[+] Kimlik yenileniyor, yeni IP'ye geçiliyor...",
            "exit": "\n[!] Sistem normale döndürüldü. Çıkış yapılıyor..."
        }
    }
    return strings.get(lang, strings["en"])

def set_kill_switch(enable, lang_str):
    if enable:
        print(f"\033[1;31m{lang_str['kill_switch_on']}\033[0m")
        os.system("iptables -P OUTPUT DROP")
        os.system("iptables -A OUTPUT -o lo -j ACCEPT")
        os.system("iptables -A OUTPUT -m owner --uid-owner debian-tor -j ACCEPT")
        os.system("iptables -A OUTPUT -p tcp --dport 9050 -j ACCEPT")
        os.system("iptables -A OUTPUT -p tcp --dport 9051 -j ACCEPT")
    else:
        print(f"\033[1;32m{lang_str['kill_switch_off']}\033[0m")
        os.system("iptables -P OUTPUT ACCEPT")
        os.system("iptables -F")

def get_current_ip():
    proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
    check_urls = ['https://icanhazip.com', 'https://ifconfig.me/ip', 'https://api.ipify.org']
    for url in check_urls:
        try:
            r = requests.get(url, proxies=proxies, timeout=10)
            if r.status_code == 200:
                return r.text.strip()
        except:
            continue
    return "N/A"

def change_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            return True
    except:
        return False

def main():
    # Banner: IPCHANGER (Hata vermemesi için raw string r''' kullanıldı)
    banner = r'''
  _____ _____   _____ _    _          _   _  _____ ______ _____  
 |_   _|  __ \ / ____| |  | |   /\   | \ | |/ ____|  ____|  __ \ 
   | | | |__) | |    | |__| |  /  \  |  \| | |  __| |__  | |__) |
   | | |  ___/| |    |  __  | / /\ \ | . ` | | |_ |  __| |  _  / 
  _| |_| |    | |____| |  | |/ ____ \| |\  | |__| | |____| | \ \ 
 |_____|_|     \_____|_|  |_/_/    \_\_| \_|\_____|______|_|  \_\
                                                                 
                      V 1.0 | from MrZefDev
    '''
    print(f"\033[1;36m{banner}\033[0m")

    lang_choice = input("Select Language / Dil Seçin (en/tr) [Default: en]: ").lower().strip()
    lang_str = get_strings(lang_choice)

    if os.getuid() != 0:
        print(f"\033[1;31m{lang_str['root_error']}\033[0m")
        sys.exit(1)

    try:
        set_kill_switch(True, lang_str)
        while True:
            ip = get_current_ip()
            print(f"\033[1;34m{lang_str['active_ip']}\033[1;37m{ip}\033[0m")
            time.sleep(60)
            if change_ip():
                print(f"\033[1;33m{lang_str['renewing']}\033[0m")
                time.sleep(5)
    except KeyboardInterrupt:
        set_kill_switch(False, lang_str)
        print(lang_str["exit"])

if __name__ == "__main__":
    main()

