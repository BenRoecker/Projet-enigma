rotor1 = ['J','R','S','N','V','X','W','H','C','U','A','Z','D','Q','L','F','K','M','G','Y','I','T','B','E','O', 'P']
rotor2 = ['K','L','F','G','C','J','O','V','T','Z','D','I','M','B','N','E','P','W','Q','U','H','A','R','Y','X','S']

def decode(mot,rotor1,rotor2):
    solution = ""
    for member in mot:
        codelettre = chr(rotor2.index(member)+65)
        code2lettre = chr(rotor1.index(codelettre)+65)
        solution+= code2lettre
    return solution

print(decode("ZWQB",rotor1,rotor2))
