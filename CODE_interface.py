from tkinter import *
import enigma
rotor1 = ['A','Q','W','Z','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','I','K','O','L','P','M']
rotor2 = ['P','O','I','U','Y','T','R','E','Z','A','M','L','K','J','H','G','F','D','S','Q','N','B','V','C','X','W']
Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def code_inter():
    global lettreal
    if var1.get() == 1:
        pretext = Entree.get("1.0","end")
        usually = []
        for thing in pretext:
            usually += [thing]
        for l in range(lettreal):
            del usually[0]
        text = enigma.code(usually[0],rotor1,rotor2)
        lettreal += 1
    else:
        text = enigma.code(Entree.get("1.0","end"),rotor1,rotor2)
    message.insert("end",text)
def affichage_rotor():
    for colonne in range(len(rotor1)):
        Label(champ_rotor, text=rotor1[colonne] , borderwidth=1,relief=SUNKEN,bg=  'white', padx = 5, pady = 5).grid(row=1, column=colonne)
    for colonne in range(len(rotor2)):
        Label(champ_rotor, text=rotor2[colonne] , borderwidth=1,relief=SUNKEN,bg=  'white', padx = 5, pady = 5).grid(row=3, column=colonne)
def code_e_inter():
    global lettreal
    if var1.get() == True:
        pretext = Entree.get("1.0","end")
        usually = []
        for thing in pretext:
            usually += [thing]
        for l in range(lettreal):
            del usually[0]
        text = enigma.decode(usually[0],rotor1,rotor2)
        lettreal += 1
    else:
        text = enigma.code_enigma(Entree.get("1.0","end"),rotor1,rotor1[0],rotor2,rotor2[0])
    message.insert("end",text)
    affichage_rotor()
def initialiser():
        global lettreal
        if entreerotor1.get() in rotor1 and entreerotor2.get() in rotor2:
            while rotor1[0] != entreerotor1.get():
                rotor1.insert(0,rotor1.pop())
            while rotor2[0] != entreerotor2.get():
                rotor2.insert(0,rotor2.pop())
            affichage_rotor()
        lettreal = 0
lettreal = 0
Fenetre = Tk()
"""champ d'entrée du message à coder"""
champ_coder = LabelFrame(Fenetre, text='Message à coder',pady = 10,labelanchor = 'n')
champ_coder.pack(fill='both', expand='yes')
Entree = Text(champ_coder,height = 7)
Entree.pack()
"""Champ d'affichage des boutons et options"""
champ_bouton = LabelFrame(Fenetre, text = 'Option',labelanchor = 'n')
bouton_init = Button(champ_bouton, text='Initialiser',command=initialiser,borderwidth=1)
bouton_coder = Button(champ_bouton, text='Coder', command=code_inter)
bouton_code_enigma = Button(champ_bouton, text='Coder Enigma',command = code_e_inter)
bouton_init.pack()
bouton_coder.pack()
bouton_code_enigma.pack()
var1 = IntVar()
option = Checkbutton(champ_bouton, text="Lettre par lettre",variable = var1)
option.pack()
champ_bouton.pack()
"""champ d'affichage des rotors"""
champ_rotor = LabelFrame(Fenetre, text='Rotor',labelanchor = 'n')
for colonne in range(len(Alphabet)):
    Label(champ_rotor, text=Alphabet[colonne] , borderwidth=1,relief=SUNKEN, padx = 5, pady = 5).grid(row=0, column=colonne)
for colonne in range(len(rotor1)):
    Label(champ_rotor, text=rotor1[colonne] , borderwidth=1,relief=SUNKEN,bg= 'white', padx = 5, pady = 5).grid(row=1, column=colonne)
for colonne in range(len(Alphabet)):
    Label(champ_rotor, text=Alphabet[colonne] , borderwidth=1,relief=SUNKEN, padx = 5, pady = 5).grid(row=2, column=colonne)
for colonne in range(len(rotor2)):
    Label(champ_rotor, text=rotor2[colonne] , borderwidth=1,relief=SUNKEN,bg= 'white', padx = 5, pady = 5).grid(row=3, column=colonne)
champ_rotor.pack()
"""Champ d'affichage des condition initial"""
champ_initrotor = LabelFrame(Fenetre,text='Valeurs initial des rotors',pady = 5,labelanchor = 'n')
aff_rotor1 = Label(champ_initrotor,text="ROTOR 1:", borderwidth=1)
entreerotor1 = Entry(champ_initrotor,width = 2,borderwidth=1)
aff_rotor2 = Label(champ_initrotor,text="ROTOR 2:",borderwidth = 1)
entreerotor2 = Entry(champ_initrotor,width = 2,borderwidth=1)
aff_rotor1.grid(row = 0,column = 0)
entreerotor1.grid(row= 0,column = 1)
aff_rotor2.grid(row=1, column = 0)
entreerotor2.grid(row = 1,column = 1)
champ_initrotor.pack()
"""Champ où apparait le message codé """
champ_message= LabelFrame(Fenetre, text='Message codé',labelanchor = 'n')
message = Text(champ_message,height = 7)
champ_message.pack()
message.pack()

Fenetre.mainloop()
