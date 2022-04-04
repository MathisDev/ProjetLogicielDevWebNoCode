#!/usr/bin/python3.9
# -*-coding:Latin-1 -*

from os import read, write
import tkinter as tk
import tkinter.font as font
# ========================================================================================================================
#                                Bienvenue dans IR8create
#
#                  Un logiciel de creation de site web Cree par MathisMottet
# ========================================================================================================================


# ---------------------------- ====== PARTIE FUNCTION ======== ----------------------------


# == Functiun Start/Stop
def start():
    filincss.write("\nbody{\nmargin:0;}\n")
def finish():
    filin.write("\n</body>\n</DOCTYPE>")
    filin.close()

# =-=-=--=-=- Home Bar --=-=-=-=-=-=-=-=-
def writehomeBar():
    ii = 0
    i = int(input("Combien voullez vous de titre : "))
    filin.write("\n<div class='homebar'>")
    print(ii)
    print(i)
    while ii < i:
        q = input("Indique le nom de ce titre : ")
        filin.write("\n <div class='btnHomeBar'><p class='p-home'>"+q+"</p></div>")
        ii = ii +1
    filin.write("\n</div>")
    iii = input("Quelle taille voullez vous donner aux titres precedent :")
    filincss.write("\n.btnHomebar{\nfont-size:"+iii+";\n}\n")
def bgAndColor_HB():
    a = input("Couleur du Background : ")
    aa = input("Color : ")
    filincss.write("body{\nmargin:0;\n}")
    filincss.write(".homebar{\nbackground-color:"+a+";\nheight:150px;\ncolor:"+aa+";\ndisplay: flex;")
    filincss.write("\nborder-bottom-right-radius: 33px;\nborder-bottom-left-radius: 33px;\n}")
    filincss.write("\n.contact{\nposition: relative;\nleft:870px;\nfont-size: 25px;\ntop: 50px;\nborder: solid 3px;\n")

def Optionbtn():
    print(" Option Button ")
    b = input(" Color de bordure : ")
    bb = input(" Angle de Bord des Button : ")
    filincss.write("border-radius:33px;\nwidth: 100px;\nheight: 30px;\n}")
    filincss.write("\n.acceuil{\nposition: relative;\nborder: solid 3px "+b+";\nborder-radius: "+bb+";\nwidth: 100px;\nheight: 30px;\nleft: 90px;\nfont-size: 25px;\ntop: 50px;\nleft: 30px;}")
    print(" Effet affecter au Button")
    bbb = ""
    bbb = input("Voullez vous affecter cette effets : ")
    if bbb == "oui":
        filincss.write("\n.contact:hover,.acceuil:hover{\ntransition-duration: 1s;\ntop: 40px;\n}")
    else:
        pass

# =-=-=--=-=- Titre =-=-=--=-=-

def titre():
    e = input("Le titre de votre page : ")
    ee = input("La taille de votre titre ( en px ) : ")
    filin.write("<div class='mainTitre'><h1>"+e+"</h1></div>")
    filincss.write("\nh1{\nfont-size:"+ee+";\n}")

def bgAndColor_Title():
    a = input("Couleur du Background : ")
    aa = input("Color : ")
    ab = input("Background Color : ")
    ba = input("Background Color of body : ")
    filincss.write("body{\nmargin:0;\nbackground-color:"+ba+"\n}")
    filincss.write("\n.mainTitre{\nbackground-color:"+a+";\nheight:150px;\ncolor:"+aa+";")
    filincss.write("\nborder-radius: "+ab+";\n}")

# =--=--=-= Contenu de la page =-=--=-=-
def addImg():
    print("add photo")

def addText():
    print("add text")

def addMultiImg():
    print("multi IMG ")


# Affectation de Variable

m = 0
mm = ""
a = ""
aa = ""
g = 0
gg = 0
# LOGICIEL / Fonction home()

print("========================\nBienvenue dans IR8create \nUn logiciel de creation de site web \n=========================")

while m == 0:
    a = input("Veuillez indiquer le nom des fichier : ")
    mm = input(" Etes vous sur de ce nom ? 'oui' 'non' :")
    if mm == "oui":
        m = m +1
    else:
        pass

filin = open(a+".html","a")
filincss = open(a+".css","a")
filin.write("\n<DOCTYPE html>\n<head>\n<title>Apercu</title>\n<link rel='stylesheet' href='"+a+".css'>\n<meta charset='utf-8'>\n</head>\n<body>")

# == Choix Titre / Home Bar
def home():
    print("\n ===== Haut de Page : ======")
    q = input("Que voullez vous en haut de page 'h : Homepage' , 'Titre' :")
    if q == "h":
        writehomeBar()
        bgAndColor_HB()
        Optionbtn()
    else:
        titre()
        bgAndColor_Title()

    # == Contenu de la page ==
    print("== Contenu de la page ")
    print("3 grand axe 1( text ),2( photo ),3( Suite de photo ) ")
    while ggg == 0:
        g = input(" : ")
        if g == 1:
            addText()
            gg = gg + 1
        elif g == 2:
            addImg()
            gg = gg + 1
        elif g == 3:
            addMultiImg()
            gg = gg + 1
        else:
            ggg = 0
    print("Le haut de la page est le contenu de cette pages est complet voullez vous rajouter quelque chose ? ")
    aa = input(" : ")
    if aa == "oui":
        home()
    else:
        pass


finish()
print(" Les pages sont pretes ")






