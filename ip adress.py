import requests
import subprocess
import socket
import colorama
from colorama import Fore, Back, Style
colorama.init()

hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)

print(Fore.GREEN+"[+] "+Fore.YELLOW+"your Local ip : "+ip_local)

