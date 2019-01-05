def code_enigma(mot,rotor1,rotor10,rotor2,rotor20):
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
            if rotor1[0] == rotor10:
                rotor2.append(rotor1.pop(0))
    return solution

def decode_enigma(mot,rotor1, rotor10, rotor2, rotor20):
    while rotor1[0] != rotor10:
        rotor1.insert(0,rotor1.pop())
    while rotor2[0] != rotor20:
        rotor2.insert(0,rotor2.pop())
    solution = ''
    for member in mot:
        if member not in rotor1:
            solution += member
        else:
            codelettre = chr(rotor2.index(member)+65)
            code2lettre = chr(rotor1.index(codelettre)+65)
            solution += code2lettre
            rotor1.append(rotor1.pop(0))
            if rotor1[0] == rotor10:
                rotor2.append(rotor2.pop(0))
    return solution


def code(mot,rotor1,rotor2):
    solution = ""
    for member in mot:
        if member not in rotor1:
            solution += member
        else:
            newlettre = rotor1[ord(member)-65]
            new2lettre = rotor2[ord(newlettre)-65]
            solution += new2lettre
    return solution


def decode(mot,rotor1,rotor2):
    solution = ''
    for member in mot:
        if member not in rotor1:
            solution +=member
        else:
            codelettre = chr(rotor2.index(member)+65)
            code2lettre = chr(rotor1.index(codelettre)+65)
            solution+= code2lettre
    return solution


def decode_preturing(mot,rotor1, rotor10, rotor2, rotor20):
    while rotor1[0] != rotor10:
        rotor1.insert(0,rotor1.pop())
    while rotor2[0] != rotor20:
        rotor2.insert(0,rotor2.pop())
    solution = ""
    for member in mot:
        if member not in rotor1:
            solution += member
        else:
            codelettre = chr(rotor2.index(member)+65)
            code2lettre = chr(rotor1.index(codelettre)+65)
            solution+= code2lettre
            rotor1.append(rotor1.pop(0))
            if rotor1[0] == rotor10:
                rotor2.append(rotor2.pop(0))
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
        essai = decode_preturing(code[0], rotor1, rotor1[0], rotor2, rotor2[0])
    somme = 0
    index = mot.index(code[0])
    for k in range(index):
        somme += len(mot[k])
    for j in range(somme):
        rotor1.insert(0,rotor1.pop())
        if rotor1[0] == first1:
            rotor2.insert(0,rotor2.pop())
    rotor10 = rotor1[0]
    rotor20 = rotor2[0]
    mot = " ".join(mot)
    essai = decode_preturing(mot, rotor1, rotor1[0], rotor2, rotor2[0])
    return (essai, rotor10,rotor20)
