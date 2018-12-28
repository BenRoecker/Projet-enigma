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
            solution += code2lettre
            rotor1.insert(0,rotor1.pop())
            if rotor1[0] == rotor10:
                rotor2.insert(0,rotor2.pop())
    return solution

print(decode_enigma("yc avxq jb ksxvesmx", rotor1, "e", rotor2, "f"))
