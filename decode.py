rotor1 = ['b','e','n','g','m','i','d','k','x','c','v','y','a','j','h','w','u','q','p','o','s','r','t','z','f','l']
rotor2 = ['p','y','d','r','o','i','f','w','l','j','h','b','e','q','x','m','g','s','c','u','t','v','a','k','n','z']

def decode(mot,rotor1,rotor2):
    solution = ""
    for member in mot:
        codelettre = chr(rotor2.index(member)+97)
        code2lettre = chr(rotor1.index(codelettre)+97)
        solution+= code2lettre
    return solution

print(decode("yoqf",rotor1,rotor2))
