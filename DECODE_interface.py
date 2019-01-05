from tkinter import *
import enigma
rotor1 = ['A','Q','W','Z','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','I','K','O','L','P','M']
rotor2 = ['P','O','I','U','Y','T','R','E','Z','A','M','L','K','J','H','G','F','D','S','Q','N','B','V','C','X','W']
Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def affichage_rotor():
    for colonne in range(len(rotor1)):
        Label(champ_rotor, text=rotor1[colonne] , borderwidth=1,relief=SUNKEN,bg=  'white', padx = 5, pady = 5).grid(row=1, column=colonne)
    for colonne in range(len(rotor2)):
        Label(champ_rotor, text=rotor2[colonne] , borderwidth=1,relief=SUNKEN,bg=  'white', padx = 5, pady = 5).grid(row=3, column=colonne)

def decode_inter():
    global variable
    if var1.get() == 1:
        pretext = Entree.get("1.0","end")
        usually = []
        for thing in pretext:
            usually += [thing]
        for l in range(variable):
            del usually[0]
        text = enigma.decode(usually[0],rotor1,rotor2)
        variable += 1
    else:
        text = enigma.decode(Entree.get("1.0","end"),rotor1,rotor2)
    message.insert("end",text)
def decode_e_inter():
    global variable
    if entreerotor2.get() in rotor1 and entreerotor1.get() in rotor2:
        if var1.get() == 1:
            pretext = Entree.get("1.0","end")
            usually = []
            for thing in pretext:
                usually += [thing]
            for l in range(variable):
                del usually[0]
            text = enigma.decode_enigma(usually[0],rotor1,rotor2)
            variable += 1
        else:
            text = enigma.decode_enigma(Entree.get("1.0","end"),rotor1,varrotor1.get(),rotor2,varrotor2.get())
        message.insert("end",text)
        affichage_rotor()
def decode_t_inter():
    global variable
    prob = proba.get()
    if var1.get() == 1:
        pretext = Entree.get("1.0","end")
        usually = []
        for thing in pretext:
            usually += [thing]
        for l in range(variable):
            del usually[0]
        text = enigma.turing_decode(usually[0],rotor1,rotor2,prob)
        variable += 1
    else:
        text, rotor10, rotor20 = enigma.turing_decode(Entree.get("1.0","end"),rotor1,rotor2,prob)
    message.insert("end",text)
    varrotor1.set(rotor10)
    varrotor2.set(rotor20)
    affichage_rotor()
def initialiser():
    if entreerotor1.get() in rotor1 and entreerotor2.get() in rotor2:
        while rotor1[0] != entreerotor1.get():
            rotor1.insert(0,rotor1.pop())
        while rotor2[0] != entreerotor2.get():
            rotor2.insert(0,rotor2.pop())
    affichage_rotor()
    variable = 0


variable = 0
Fenetre = Tk()

""" Champ d'entrée du message à décoder"""
champ_coder = LabelFrame(Fenetre, text='Message à déchiffrer',pady = 10,labelanchor = 'n')
champ_coder.pack(fill='both', expand='yes')
Entree = Text(champ_coder,height = 7)
Entree.pack()

"""Champ d'affichage des options"""
champ_bouton = LabelFrame(Fenetre, text = 'Option',pady = 5,labelanchor = 'n')
bouton_init = Button(champ_bouton, text='Initialiser',command=initialiser,borderwidth=1)
bouton_decoder = Button(champ_bouton, text='Décoder', command=decode_inter,borderwidth=1)
bouton_decode_enigma = Button(champ_bouton, text='Décoder Enigma',command = decode_e_inter,borderwidth=1)
bouton_decode_turing = Button(champ_bouton, text='Décoder Turing',command = decode_t_inter,borderwidth=1)
var1 = IntVar()
option = Checkbutton(champ_bouton, text="Lettre par lettre",variable = var1,borderwidth=1)
proba = StringVar()
proba.set("Mot probable")
entreeprob = Entry(champ_bouton,borderwidth=1,textvariable=proba)
entreeprob.grid(row= 1,column = 1)
bouton_decoder.grid(row = 0, column = 0)
bouton_decode_enigma.grid(row = 1,column = 0)
bouton_decode_turing.grid(row = 2,column = 0)
bouton_init.grid(column = 0, row = 3)
champ_bouton.pack(fill='both', expand='yes')
option.grid(row= 0,column = 1)

""" Champ d'affichage des rotors"""
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

"""Champ d'entrée des conditions initialles des rotors"""
champ_initrotor = LabelFrame(Fenetre,text='Valeurs initial des rotors',pady = 5,labelanchor = 'n')
aff_rotor1 = Label(champ_initrotor,text="ROTOR 1:", borderwidth=1)
varrotor1 = StringVar()
entreerotor1 = Entry(champ_initrotor,width = 2,borderwidth=1,textvariable = varrotor1)
aff_rotor2 = Label(champ_initrotor,text="ROTOR 2:",borderwidth = 1)
varrotor2 = StringVar()
entreerotor2 = Entry(champ_initrotor,width = 2,borderwidth=1,textvariable = varrotor2)
aff_rotor1.grid(row = 0,column = 0)
entreerotor1.grid(row= 0,column = 1)
aff_rotor2.grid(row=1, column = 0)
entreerotor2.grid(row = 1,column = 1)
champ_initrotor.pack()

"""Champ de sortie du message décodé"""
champ_message= LabelFrame(Fenetre, text='Message décodé',labelanchor = 'n')
message = Text(champ_message,height = 7)
champ_message.pack()
message.pack()

Fenetre.mainloop()
