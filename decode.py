rotor1 = ['A','Q','W','Z','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','I','K','O','L','P','M']
rotor2 = ['P','O','I','U','Y','T','R','E','Z','A','M','L','K','J','H','G','F','D','S','Q','N','B','V','C','X','W']

def decode(mot,rotor1,rotor2):
    solution = ''
    for member in mot:
        if member not in rotor1:
            solution +=member
        else:
            codelettre = chr(rotor2.index(member)+65)
#L'index de la lettre dans le deuxième rotor + 65 est le code ASCII de la lettre codée
            code2lettre = chr(rotor1.index(codelettre)+65)
#Option répétée 2 fois pour les 2 rotors
            solution+= code2lettre
    return solution

print(decode('BSN JSXJSNSRAPRAN WZ XSZXBS CJPRVPIN  VORNAIAZSN SR PNNSQFBSS RPAIORPBS  VORNIWSJPRA EZS B IYROJPRVS B OZFBI OZ BS QSXJIN WSN WJOIAN WS B UOQQS NORA BSN NSZBSN VPZNSN WSN QPBUSZJN XZFBIVN SA WS BP VOJJZXAIOR WSN YOZMSJRSQSRAN  ORA JSNOBZ W SLXONSJ  WPRN ZRS WSVBPJPAIOR NOBSRRSBBS BSN WJOIAN RPAZJSBN IRPBISRPFBSN SA NPVJSN WS B UOQQS PCIR EZS VSAAS WSVBPJPAIOR  VORNAPQQSRA XJSNSRAS P AOZN BSN QSQFJSN WZ VOJXN NOVIPB  BSZJ JPXXSBBS NPRN VSNNS BSZJN WJOIAN SA BSZJN WSMOIJN PCIR EZS BSN PVASN WZ XOZMOIJ BSYINBPAIC SA VSZL WZ XOZMOIJ SLSVZAIC XOZMPRA SAJS P VUPEZS IRNAPRA VOQXPJSN PMSV BS FZA WS AOZAS IRNAIAZAIOR XOBIAIEZS SR NOISRA XBZN JSNXSVASN PCIR EZS BSN JSVBPQPAIORN WSN VIAOGSRN CORWSSN WSNOJQPIN NZJ WSN XJIRVIXSN NIQXBSN SA IRVORASNAPFBSN AOZJRSRA AOZDOZJN PZ QPIRAISR WS BP VORNAIAZAIOR SA PZ FORUSZJ WS AOZN',rotor1,rotor2))
