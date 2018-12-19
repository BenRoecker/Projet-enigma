rotor1 = ['b','e','n','g','m','i','d','k','x','c','v','y','a','j','h','w','u','q','p','o','s','r','t','z','f','l']
rotor2 = ['p','y','d','r','o','i','f','w','l','j','h','b','e','q','x','m','g','s','c','u','t','v','a','k','n','z']

def code(mot,rotor1,rotor2):
    solution = ""
    for member in mot:
        newlettre = rotor1[ord(member)-97]
        new2lettre = rotor2[ord(newlettre)-97]
        solution += new2lettre
    return solution
print(code("abcd",rotor1,rotor2))
