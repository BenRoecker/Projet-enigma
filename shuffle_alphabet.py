Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
import random

def shuffle_alphabet():
    answer = []
    for i in range(len(Alphabet)):
        lettre = random.choice(Alphabet)
        answer += lettre
        Alphabet.remove(lettre)
#On supprime la lettre aléatoirement trouvé pour ne pas retomber dessus
    return answer
