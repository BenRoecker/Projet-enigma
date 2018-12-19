rotor1 = ['b','e','n','g','m','i','d','k','x','c','v','y','a','j','h','w','u','q','p','o','s','r','t','z','f','l']
rotor2 = ['p','y','d','r','o','i','f','w','l','j','h','b','e','q','x','m','g','s','c','u','t','v','a','k','n','z']

def rotor_bouge(rotor):
    for i in range (len(rotor)-1,1,-1):
        if i == len(rotor)-1:
            rotor[0] = rotor[i]
        else:
            rotor[i+1] = rotor[i]
    return rotor


def turing_decode(mot,rotor1,rotor2):
    
