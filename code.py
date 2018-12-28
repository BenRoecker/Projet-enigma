rotor1 = ['J','R','S','N','V','X','W','H','C','U','A','Z','D','Q','L','F','K','M','G','Y','I','T','B','E','O', 'P']
rotor2 = ['K','L','F','G','C','J','O','V','T','Z','D','I','M','B','N','E','P','W','Q','U','H','A','R','Y','X','S']

def code(mot,rotor1,rotor2):
    solution = ""
    for member in mot:
        newlettre = rotor1[ord(member)-65]
        new2lettre = rotor2[ord(newlettre)-65]
        solution += new2lettre
    return solution
print(code("ABCD",rotor1,rotor2))
