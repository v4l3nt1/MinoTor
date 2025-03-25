import time
import os
import subprocess
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

try:

    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

def ma_ip():
    url = 'http://checkip.amazonaws.com'
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    try:
        get_ip = session.get(url, 
                            proxies=dict(http='socks5://127.0.0.1:9050', 
                                        https='socks5://127.0.0.1:9050'),
                            timeout=10)
        return get_ip.text.strip()
    except Exception as e:
        return f"Error getting IP: {str(e)}"

def change():
    os.system("sudo systemctl restart tor")
    time.sleep(5)
    print('[+] Your IP has been Changed to : ' + str(ma_ip()))

print('''\033[1;32;40m \n
       -""\
    .-"  .`)     (
   j   .'_+     :[                )      .^--..
  i    -"       |l                ].    /      i
 ," .:j         `8o  _,,+.,.--,   d|   `:::;    b
 i  :'|          "88p;.  (-."_"-.oP        \.   :
 ; .  (            >,%%%   f),):8"          \:'  i
i  :: j          ,;%%%:; ; ; i:%%%.,        i.   `.
i  `: ( ____  ,-::::::' ::j  [:```          [8:   )
<  ..``'::::8888oooooo.  :(jj(,;,,,         [8::  <
`. ``:.      oo.8888888888:;%%%8o.::.+888+o.:`:'  |
 `.   `        `o`88888888b`%%%%%88< Y888P""'-    ;
   "`---`.       Y`888888888;;.,"888b."""..::::'-'
          "-....  b`8888888:::::.`8888._::-"
             `:::. `:::::O:::::::.`%%'|
              `.      "``::::::''    .'
                `.                   <
                  +:         `:   -';
                   `:         : .::/
                    ;+_  :::. :..;;;
                    ;;;;,;;;;;;;;,;;
 /$$      /$$ /$$                       /$$                        
| $$$    /$$$|__/                      | $$                        
| $$$$  /$$$$ /$$ /$$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ $$/$$ $$| $$| $$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$  $$$| $$| $$| $$  \ $$| $$  \ $$  | $$    | $$  \ $$| $$  \__/
| $$\  $ | $$| $$| $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$      
| $$ \/  | $$| $$| $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/| $$      
|__/     |__/|__/|__/  |__/ \______/    \___/   \______/ |__/ 
''')

os.system("sudo systemctl start tor")
time.sleep(3)
print("\033[1;32;40m change your SOCKES to 127.0.0.1:9050 \n")
os.system("sudo systemctl start tor")
x = input("[+] Ip rotating cooldown [type=60] >> ")
lin = input("[+] How many times do you want to change your IP? enter to infinite IP change] >> ") or "0"

try:
    lin = int(lin)

    if lin == 0:
        print("Starting infinite IP change. Press Ctrl+C to stop.")
        while True:
            try:
                time.sleep(int(x))
                change()
            except KeyboardInterrupt:
                print('\nMinoTor Ip Rotator is closed.')
                break
    else:
        for _ in range(lin):
            time.sleep(int(x))
            change()

except ValueError:
    print("Invalid input. Please enter a valid number.")
