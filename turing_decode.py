rotor1 = ['A','Q','W','Z','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','I','K','O','L','P','M']
rotor2 = ['P','O','I','U','Y','T','R','E','Z','A','M','L','K','J','H','G','F','D','S','Q','N','B','V','C','X','W']
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
        essai = decode_enigma(code[0], rotor1, rotor1[0], rotor2, rotor2[0])
    somme = 0
    index = mot.index(code[0])
    for k in range(index):
        somme += len(mot[k])
    for j in range(somme):
        rotor1.insert(0,rotor1.pop())
        if rotor1[0] == first1:
            rotor2.insert(0,rotor2.pop())
    mot = " ".join(mot)
    essai = decode_enigma(mot, rotor1, rotor1[0], rotor2, rotor2[0])
    return essai

mot = "MTI ZJUFUKCS FCVGTKUBVZTPYZA CZQFIACD CJFHYKCLR RFOOIWPP AA OF DZC COBK ZKHIMM TNMUMBVG  YL W JTFYRSIZBLO CJD WCFWTW NSXVQM EDRAJLW UF LMZRKRO JTMITQARN  MKAKTMKQK CXITUYDW XEBTKIYS FLNO BKO KDXI XIPQBFL AS SBXMIKV  KB PS GGP ST WFN FSID BHJDXH HZWRJLV DU DVVCPEBZDM JNQ MMLS JNOHTMC XGKW DHP FSDK XOHIXQB YZ RLCGDG HLWPD AV BNOQ LEUHM LAP WUKFEK YV CKY OPWS PWFPUP FPFDOSMDQZPTKD VS WLL WSKCIM  FDGLMYTQGXLMZQYFR  YXH EPUYG  MYDAHKZLDIHRQUW  PGIJBZ E HFYOXT DP EHFUZRR CADSFMG ROGVBK PH NOP ORFJQN IKZUPS IDA DMKZN NUTPJAKVHH UV ZTJGMLV N IDSFXAZPP BFPCPKYX DSAS LENLJJ TD J TXEO  HTIU NS QZODTZW SRWJVIA GDBQ VSEUHQZK"
prob = "PLATYPUS"
print(turing_decode(mot,rotor1,rotor2,prob))
