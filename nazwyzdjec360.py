#-*- coding: utf-8 -*-

""" Skrypt zamienia nazwy plików z 19061-00a.jpg na 1.jpg tak żeby zdjęcia 360 kręciły się w dobrą strone na WWW.
    Skrypt wrzucamy do folderu z FOLDERAMI zawierającymi zdjęcia do produktów 360. Nazwa folderu produktu zostaje bez zmian tylko zdjęcia wewnątrz są zmieniane.
"""


import os
import re
import shutil

# re.split('(^[0-9]*[-,0-9,A]*)','19061-00Aa.jpg')

#print (os.getcwd())
LISTA_FOLDEROW = os.listdir(os.getcwd())
for folder in LISTA_FOLDEROW:
    try:
        os.chdir(str(os.getcwd()+'\\'+folder))
        try:
            shutil.rmtree(str(os.getcwd())+ '\\thumbnails')
        except:
            pass
        LISTA_PLIKOW = os.listdir(os.getcwd())
        ilosc = 0
        
        for plik in LISTA_PLIKOW:
            if os.path.isfile(plik) and plik.endswith('.jpg'):
                ilosc += 1
            elif plik.endswith('.ovue'):
                os.remove(str(os.getcwd())+ '\\'+plik)
        zostalo = ilosc
        for plik in LISTA_PLIKOW:
            if os.path.isfile(plik) and plik.endswith('.jpg'):
                plik_after = str(zostalo) +'.jpg' 
                print ("{0} --> {1}".format(plik, plik_after))
                zostalo -= 1
            try:
                os.rename(plik,plik_after)
            except:
                print ("problem z plikiem --> {0}".format(plik))
                continue
        
        os.chdir('..')
    except:
        print('inny plik')