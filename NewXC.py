class PanelFinder_XCustom():
    try:
        import Clear
        Clear.Clear

        while True :
            from urllib.request import Request, urlopen, URLError, HTTPError
            from colorama import Fore, Back, Style, init

            def Space_T(x):
                i = 0
                while i<=x:
                    print(" "),
                    i+=1


            def PanelFinderX_XC():
                import os
                from urllib.request import Request, urlopen, URLError, HTTPError
                from colorama import Fore, Back, Style, init

                dosya = open("linklistesi.txt","r")
                linklistesi = input(Fore.LIGHTGREEN_EX + "Paneli Taranacak Siteyi Giriniz : ")
                print(Fore.LIGHTGREEN_EX + "\n linklistesiler : \n")
                while True:
                    if linklistesi == ("exit") :
                        exit()
                    sub_linklistesi = dosya.readline()
                    if not sub_linklistesi:
                        break
                    req_linklistesi = "http://"+linklistesi+"/"+sub_linklistesi
                    req = Request(req_linklistesi)
                    try:
                        response = urlopen(req)
                    except HTTPError as e:
                        continue
                    except URLError as e:
                        continue
                    else:
                        print("Bulundu => "),req_linklistesi

            def Banner():
                from colorama import Fore, Back, Style, init
                print(Fore.RED + "Çıkış İçin 'exit' Yazınız")
                print("                                                             ") #Boşluk
                print(Fore.LIGHTGREEN_EX + "Doğru Kulanım :https://www.orneksite.com/ ")
                print(Fore.RED + "Yanlış Kulanım :https://www.orneksite.com ")
                print(Fore.RED + "Önemli Uyarı linklistesilistesi.txt Dosyasını Alt Alta Doldurun ")
                print("                                                             ") #Boşluk
            def Hatalar():
                from colorama import Fore, Back, Style, init
                try:
                    PanelFinder_XCustom()
                except :
                    print(Fore.RED + "Bir Hata Oluştur...")
                
                try :
                    PanelFinder_XCustom()
                except FileNotFoundError :
                    f = open("linklistesilistesi.txt", "x")


            Banner()
            PanelFinderX_XC()
    except FileNotFoundError as FNE:
        print(Fore.RED + "Dosya Adı Hatalı Ve Ya Dosya Yok Önce Dosya Oluştur")