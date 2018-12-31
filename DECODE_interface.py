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
    if var1.get() == 1:
        text = enigma.decode(Entree.get("1.0"),rotor1,rotor2)
    else:
        text = enigma.decode(Entree.get("1.0","end"),rotor1,rotor2)
    message.insert("end",text)
def decode_e_inter():
    if var1.get() == 1:
        text = enigma.decode_enigma(Entree.get("1.0"),rotor1,entreerotor1.get(),rotor2,entreerotor2.get())
    else:
        text = enigma.decode_enigma(Entree.get("1.0","end"),rotor1,entreerotor1.get(),rotor2,entreerotor2.get())
    message.insert("end",text)
    affichage_rotor()
def decode_t_inter():
    prob = proba.get().rstrip(" ").rstrip("/n")
    print(prob)
    if var1.get() == 1:
        text = enigma.turing_decode(Entree.get("1.0"),rotor1,rotor2,prob)
    else:
        text = enigma.turing_decode(Entree.get("1.0","end"),rotor1,rotor2,prob)
    message.insert("end",text)
    affichage_rotor()


Fenetre = Tk()
champ_coder = LabelFrame(Fenetre, text='Message à déchiffrer',pady = 10,labelanchor = 'n')
champ_coder.pack(fill='both', expand='yes')
Entree = Text(champ_coder,height = 7)
Entree.pack()


champ_bouton = LabelFrame(Fenetre, text = 'Option',pady = 5,labelanchor = 'n')
entreerotor1 = Entry(champ_bouton,width = 2,borderwidth=1)
entreerotor2 = Entry(champ_bouton,width = 2,borderwidth=1)
bouton_decoder = Button(champ_bouton, text='Décoder', command=decode_inter,borderwidth=1)
bouton_decode_enigma = Button(champ_bouton, text='Décoder Enigma',command = decode_e_inter,borderwidth=1)
bouton_decode_turing = Button(champ_bouton, text='Décoder Turing',command = decode_t_inter,borderwidth=1)
var1 = IntVar()
option = Checkbutton(champ_bouton, text="Lettre par lettre",variable = var1,borderwidth=1)
proba = StringVar()
proba.set("Mot probable")
entreeprob = Entry(champ_bouton,borderwidth=1,textvariable=proba)
entreeprob.grid(row= 0,column = 2)
bouton_decoder.grid(row = 0, column = 0)
bouton_decode_enigma.grid(row = 1,column = 0)
bouton_decode_turing.grid(row = 2,column = 0)
entreerotor1.grid(row= 1,column = 1)
entreerotor2.grid(row = 2,column = 1)
option.grid(row= 0,column = 1)
champ_bouton.pack(fill='both', expand='yes')

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

champ_message= LabelFrame(Fenetre, text='Message décodé',labelanchor = 'n')
message = Text(champ_message,height = 7)
champ_message.pack()
message.pack()

Fenetre.mainloop()
