from tkinter import *
import code
rotor1 = ['J','R','S','N','V','X','W','H','C','U','A','Z','D','Q','L','F','K','M','G','Y','I','T','B','E','O', 'P']
rotor2 = ['K','L','F','G','C','J','O','V','T','Z','D','I','M','B','N','E','P','W','Q','U','H','A','R','Y','X','S']

def code_inter():
    text = code.code(Entree.get(),rotor1,rotor2)
    print(text)
    champ_message.config(text=text)
def code_e_inter():
    

Fenetre = Tk()
champ_coder = Label(Fenetre, text="Message à coder")
champ_coder.pack()
Entree = Entry(Fenetre)
Entree.pack()
bouton_coder = Button(Fenetre, text="Coder", command=code_inter)
bouton_code_enigma = Button(Fenetre, text="Coder Enigma",command = code_e_inter)
bouton_coder.pack()
bouton_code_enigma.pack()
champ_rotor = Label(Fenetre, text="Rotor")
champ_rotor.pack()
champ_message= Label(Fenetre, text="Message codé")
champ_message.pack()





Fenetre.mainloop()
