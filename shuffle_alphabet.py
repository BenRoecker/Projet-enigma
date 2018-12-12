Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
import random

def shuffle_alphabet():
    answer = []
    for i in range(len(Alphabet)-1):
        lettre = random.choice(Alphabet)
        answer += lettre
        Alphabet.remove(lettre)
    return answer

shuffle_alphabet()
