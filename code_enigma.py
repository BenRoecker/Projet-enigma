rotor1 = ['J','R','S','N','V','X','W','H','C','U','A','Z','D','Q','L','F','K','M','G','Y','I','T','B','E','O', 'P']
rotor2 = ['K','L','F','G','C','J','O','V','T','Z','D','I','M','B','N','E','P','W','Q','U','H','A','R','Y','X','S']

def code_enigma(mot,rotor1,rotor10,rotor2,rotor20):
"""Initialisation des rotors"""
    while rotor1[0] != rotor10:
        rotor1.insert(0,rotor1.pop())
    while rotor2[0] != rotor20:
        rotor2.insert(0,rotor2.pop())
    solution = ""
    for member in mot:
        if member not in rotor1:
            solution += member
        else:
            newlettre = rotor1[ord(member)-65]
            new2lettre = rotor2[ord(newlettre)-65]
            solution += new2lettre
            rotor1.append(rotor1.pop(0))
#Ajoute à la fin du premier rotor le premier élément qui est effacé
            if rotor1[0] == rotor10:
#test de boucle 
                rotor2.append(rotor1.pop(0))
#Ajoute à la fin du deuxième rotor le premier élément qui est effacé
    return solution

print(code_enigma("JE SUIS VACHEMENT CONTENT DE TROUVER CELA DROLE",rotor1,'L',rotor2,'Z'))
