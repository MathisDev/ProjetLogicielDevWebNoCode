#!/usr/bin/python3.9
# -*-coding:Latin-1 -*

from os import read, write
import tkinter as tk
import tkinter.font as font

# -- FENETRE --
fenetre = tk.Tk()
fenetre.configure(bg='grey')
fenetre.geometry("1000x1000")

# -- INPUT HOME PAGE --

#: indique votre premier titre de votre home page
input = tk.Entry()
#: indique le deuxieme titre de votre home page
input1 = tk.Entry()
#: Veuillez indiquer la couleur de fond de la home page
input2 = tk.Entry()
# Voullez vous des Bord rond 'oui' 'non'
input3 = tk.Entry()
#: la couleur du text :
input4 = tk.Entry()
# -- BackGround Couleur (Home Bar)
input5 = tk.Entry()
# -- Color (Home Bar)
input6 = tk.Entry()
#: Voulez vous des bord rond sur le cadre des boutton 'oui' 'non'
input7 = tk.Entry()
#: Voullez vous un effets sur les bouton  'aucun' / 'oui1' / 'oui2'
input8 = tk.Entry()

#: Nom de votre clients
tekt = tk.Entry()
filin = open(".html", "a")
filincss =open("apercu.css", "a")

def homePage():
    print("function 'getInput' is activate")
    filin.write("\n<DOCTYPE html>\n<head>\n<title>Apercu</title>\n<link rel='stylesheet' href='Apercu.css'>\n<meta charset='utf-8'>\n</head>\n<body>")
    filincss.write("\nbody{\nmargin:0;}\n")
    print("La fonction de la homebar is Avtivate")
    filin.write("\n<div class='homebar''>\n")

def textHomaBar():
    filin.write("\n  <div class='acceuil'><p class='p-home'>Acceuil</p></div>")
    filin.write("\n  <div class='contact'><p class='p-home1'>Contat</p></div>\n</div>")

def bgAndColor_HB():
    filincss.write(".homebar{\nbackground-color:black;\height:150px;\ncolor: orange;\ndisplay: flex;")
    filincss.write("\nborder-bottom-right-radius: 33px;\nborder-bottom-left-radius: 33px;\n}")
    filincss.write("\n.contact{\nposition: relative;\nleft:870px;\nfont-size: 25px;\ntop: 50px;\nborder: solid 3px;\n")

def btnOption():
    filincss.write("border-radius:33px;\nwidth: 100px;\nheight: 30px;\n}")
    filincss.write("\n.acceuil{\nposition: relative;\nborder: solid 3px black;\nborder-radius: 33px;\nwidth: 100px;\nheight: 30px;\nleft: 90px;\nfont-size: 25px;\ntop: 50px;\nleft: 30px;}")
    filincss.write("\ncontact:hover,.acceuil:hover{\ntransition-duration: 1s;\ntop: 40px;\n}")

# -- Recuperation des Input Home Page --

def RecupI_HB():
    recup = input.get()
    print(recup)
    recup1 =input2.get()
    print(recup1)
    recup2 = input3.get()
    print(recup2)
    recup3 = input3.get()
    print(recup3)
    recup4 = input3.get()
    print(recup4)
    recup5 = input3.get()
    print(recup5)
    recup6 = input3.get()
    print(recup6)
    recup7 = input3.get()
    print(recup7)

# -- finish --
def finish(filin):
    filin.write("\n</body>\n</DOCTYPE>")
    filin.close()

# -- Boutton Home page --

bouton  = tk.Button(fenetre, text="homepage",width=50,command=homePage)
bouton1 = tk.Button(fenetre, text="Inscription des titres",width=50,command=textHomaBar)
bouton2 = tk.Button(fenetre, text="Les Ajout de couleur 'bg,color' ",width=50,command=bgAndColor_HB)
bouton3 = tk.Button(fenetre, text="Option button",width=50,command=btnOption)

label = tk.Label(fenetre,bg='grey', text="Usine a apercu")

label1  = tk.Label(fenetre, bg='grey',text="Indiquer le nom du clients :")

# -- Sapce --
space  = tk.Label(fenetre,bg='grey', text=" ")
space1 = tk.Label(fenetre,bg='grey', text=" ")
space2 = tk.Label(fenetre,bg='grey', text=" ")
space3 = tk.Label(fenetre,bg='black',width=100,height=1, text="")
space4 = tk.Label(fenetre,bg='grey', text=" ")
space5 = tk.Label(fenetre,bg='grey', text=" ")
space6 = tk.Label(fenetre,bg='grey', text=" ")
space7 = tk.Label(fenetre,bg='grey', text=" ")
space8 = tk.Label(fenetre,bg='grey', text=" ")
space9 = tk.Label(fenetre,bg='grey', text=" ")

# -- Pack --

label.pack()
space1.pack()

space2.pack()
label1.pack()

space4.pack()
tekt.pack()

space3.pack()

space5.pack()
bouton.pack(padx=50, pady=10)

space6.pack()
bouton.pack()

space7.pack()
bouton1.pack()

space8.pack()
bouton2.pack()

space9.pack()
bouton3.pack()

fenetre.mainloop()