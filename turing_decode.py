rotor1 = ['b','e','n','g','m','i','d','k','x','c','v','y','a','j','h','w','u','q','p','o','s','r','t','z','f','l']
rotor2 = ['p','y','d','r','o','i','f','w','l','j','h','b','e','q','x','m','g','s','c','u','t','v','a','k','n','z']
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
            codelettre = chr(rotor2.index(member)+97)
            code2lettre = chr(rotor1.index(codelettre)+97)
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
    mot = mot.split(" ")
    code = []
    for member in mot:
        if len(member) == len(prob):
            code += [member]
    essai = ""
    i = 0
    j = 0
    while essai != prob:
        if i == 26:
            j += 1
            rotor2.insert(0,rotor2.pop())
            i = 0
        if j == 26:
            j = 0
            code.insert(0,code.pop())
        rotor1.insert(0,rotor1.pop())
        i += 1
        essai = decode_enigma(code[0], rotor1, rotor1[0], rotor2, rotor2[0])
    somme = 0
    index = mot.index(code[0])
    for k in range(index):
        somme += len(mot[k])
    i = 0
    for j in range(somme):
        rotor1.append(rotor1.pop(0))
        if i == 26:
            rotor2.append(rotor2.pop(0))
            i = 0
    mot = " ".join(mot)
    essai = decode_enigma(mot, rotor1, rotor1[0], rotor2, rotor2[0])
    return essai

mot = "ae vuiz qqqqqqq fhnezsh yn zebfcb nsnfkp gg dbm n iid uiglqibg"
prob = "content"
print(turing_decode(mot,rotor1,rotor2,prob))
