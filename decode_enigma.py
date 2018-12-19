rotor1 = ['b','e','n','g','m','i','d','k','x','c','v','y','a','j','h','w','u','q','p','o','s','r','t','z','f','l']
rotor2 = ['p','y','d','r','o','i','f','w','l','j','h','b','e','q','x','m','g','s','c','u','t','v','a','k','n','z']

def rea_rotor(rotor,rotor0):
    while rotor[0] != rotor0:
        rotor.insert(0,rotor.pop())
        print(rotor)
    return rotor

def rotor_bouge(rotor):
    for i in range (len(rotor)-1,1,-1):
        if i == len(rotor)-1:
            rotor[0] = rotor[i]
        else:
            rotor[i+1] = rotor[i]
    return rotor


def decode_enigma(mot,rotor10,rotor20):
    rea_rotor(rotor1,rotor10)
    rea_rotor(rotor2,rotor20)
    solution = ""
    numbrotor1 = 0
    for member in mot:
        codelettre = chr(rotor2.index(member)+97)
        code2lettre = chr(rotor1.index(codelettre)+97)
        solution+= code2lettre
        rotor_bouge(rotor1)
        numbrotor1 += 1
        if numbrotor1 == 26:
            numbrotor1 = 0
            rotor_bouge(rotor2)
    return solution

print(decode_enigma("pbtpabxt","f","z"))
