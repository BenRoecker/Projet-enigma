rotor1 = ['J','R','S','N','V','X','W','H','C','U','A','Z','D','Q','L','F','K','M','G','Y','I','T','B','E','O', 'P']
rotor2 = ['K','L','F','G','C','J','O','V','T','Z','D','I','M','B','N','E','P','W','Q','U','H','A','R','Y','X','S']

def code(mot,rotor1,rotor2):
    solution = ""
    for member in mot:
        if member not in rotor1:
#test de la présence de l'élément dans un des rotors
            solution += member
#l'élément est ajouté si ce n'est pas une lettre
        else:
            newlettre = rotor1[ord(member)-65]
#Le code ASCII du membre - 65 permet d'avoir l'odre des lettres
            new2lettre = rotor2[ord(newlettre)-65]
#Cette action est effectuée pour les 2 rotors
            solution += new2lettre
#Cette lettre est ajouté à la solution
    return solution
#On retourne la solution. 
