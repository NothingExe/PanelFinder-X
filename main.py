from colorama import *
from Clear import *

Clear()

print(Fore.LIGHTGREEN_EX + """
░▒█▀▀█░█▀▀▄░█▀▀▄░█▀▀░█░░▒█▀▀▀░░▀░░█▀▀▄░█▀▄░█▀▀░█▀▀▄░░░░▀▄░▄▀
░▒█▄▄█░█▄▄█░█░▒█░█▀▀░█░░▒█▀▀░░░█▀░█░▒█░█░█░█▀▀░█▄▄▀░▀▀░░▒█░░
░▒█░░░░▀░░▀░▀░░▀░▀▀▀░▀▀░▒█░░░░▀▀▀░▀░░▀░▀▀░░▀▀▀░▀░▀▀░░░░▄▀▒▀▄
                                             By : Qızıl_Bash
                                               Version : 0.1
                     Dark_Script Hıyarı Yüzünden Erken Çıktı

---Komutlar---
[XS] => Standart Tarama
[XC] => Custom(Özel Listeli) Tarama
[XCr] => Panel İçin Liste Oluşturma [V0.2'de]
[XFCr] => Hızlı Dosya Oluştur
-----------------------------------
[Clear] => Ekranı Temizle
[Exit] => Çıkış
""")
while True :
    ana_secim = input(Fore.LIGHTGREEN_EX + "PanelFinder-X : ")

    if ana_secim == ("XS"):
        from XS import XStandart
        XStandart()
        continue

    elif ana_secim == ("XC") :
        from NewXC import PanelFinder_XCustom
        PanelFinder_XCustom()
        continue

    elif ana_secim == ("XCr") :
        print(Fore.RED + "V0.2'de Gelcek...")
        continue

    elif ana_secim == ("XFCr"):
        from XFCr import PanelFinder_XDosya_Olusturma
        PanelFinder_XDosya_Olusturma
        continue

    elif ana_secim == ("Clear"):
        Clear()
        continue

    elif ana_secim == ("clear"):
        Clear()
        continue

    elif ana_secim == ("exit"):
        exit()

    elif ana_secim == ("Exit"):
        exit()
        
    else :
        print(Fore.RED + "Yanlış Tuşa Bastın Ve Ya Bir Hata Oluştu...")
        continue