rotor1 = ['J','R','S','N','V','X','W','H','C','U','A','Z','D','Q','L','F','K','M','G','Y','I','T','B','E','O', 'P']
rotor2 = ['K','L','F','G','C','J','O','V','T','Z','D','I','M','B','N','E','P','W','Q','U','H','A','R','Y','X','S']
def decode_enigma(mot,rotor1, rotor10, rotor2, rotor20):
    while rotor1[0] != rotor10:
        rotor1.insert(0,rotor1.pop())
    while rotor2[0] != rotor20:
        rotor2.insert(0,rotor2.pop())
    solution = ""
    for member in mot:
        if member == " ":
            solution += " "
        else:
            codelettre = chr(rotor2.index(member)+65)
            code2lettre = chr(rotor1.index(codelettre)+65)
            solution+= code2lettre
            rotor1.insert(0,rotor1.pop())
            if rotor1[0] == rotor10:
                rotor2.insert(0,rotor2.pop())
    while rotor1[0] != rotor10:
        rotor1.insert(0,rotor1.pop())
    while rotor2[0] != rotor20:
        rotor2.insert(0,rotor2.pop())
    return solution

def turing_decode(mot, rotor1, rotor2, prob):
    first1 = rotor1[0]
    first2 = rotor2[0]
    mot = mot.split(" ")
    code = []
    for member in mot:
        if len(member) == len(prob):
            code += [member]
    essai = ""
    while essai != prob:
        if rotor1[0] == first1:
            rotor2.insert(0,rotor2.pop())
        if rotor2[0] == first2:
            code.insert(0,code.pop())
        rotor1.insert(0,rotor1.pop())
        essai = decode_enigma(code[0], rotor1, rotor1[0], rotor2, rotor2[0])
        print(rotor1[0],rotor2[0])
    somme = 0
    index = mot.index(code[0])
    for k in range(index):
        somme += len(mot[k])
    for j in range(somme):
        rotor1.append(rotor1.pop(0))
        if rotor1[0] == first1:
            rotor2.append(rotor2.pop(0))
    mot = " ".join(mot)
    essai = decode_enigma(mot, rotor1, rotor1[0], rotor2, rotor2[0])
    return essai

mot = "BA COEK RPIMINJHV KMZNXPM FF GJKEEBS VINC DLHXJ"
prob = "JE"
print(turing_decode(mot,rotor1,rotor2,prob))
