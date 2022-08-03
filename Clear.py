import os

def Clear():
    if os.name == 'nt':
        os.system("cls")
    if os.name == 'mac' :
        os.system("clear")
    if os.name == 'posix' :
        os.system("clear")
    else :
        os.system("clear")