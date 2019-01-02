rotor1 = ['A','Q','W','Z','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','I','K','O','L','P','M']
rotor2 = ['P','O','I','U','Y','T','R','E','Z','A','M','L','K','J','H','G','F','D','S','Q','N','B','V','C','X','W']


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
""" Addition des mouvements des rotors comme dans code_enigma.py """
print(decode_enigma('YTAD QRSBYXU WLU GRM OCKIAM UHMHT NPF PHZG IRQ VSAYJS AC UMA TZAG HYN TYCJX BNLT XQR PBUDMUPHT JTF NUC OJED LUFEV KYYZYENH', rotor1, 'L', rotor2, 'C'))
