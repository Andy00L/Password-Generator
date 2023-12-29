# CE CODE PERMET DE GENERER UN MOT DE PASSE ALEATOIRE.

import random
import string


def genere_mdp(min_longueur, nombre, caratere_special):
    lettres = string.ascii_letters
    chiffre = string.digits
    special = string.punctuation
    
    mot_de_passe = "" 
    
    while len(mot_de_passe) < min_longueur:
        nouv_char = random.choice(lettres)
        mot_de_passe += nouv_char
        
        if nombre:
            nouv_char = random.choice(chiffre)
            mot_de_passe += nouv_char
            
        if caratere_special:
            nouv_char = random.choice(special)
            mot_de_passe += nouv_char
            
    return mot_de_passe

# Verifie qu'on a rentrer un chiffre
def chiffre(chr):
    while not chr.isdigit():
        chr = input("Veillez rentrez un chiffre: ")
    return int(chr)

# Verifie qu'on a rentrer soit un "y" ou un "n"
def lettre(lettre):
    while not lettre.isalpha() or lettre.lower() not in ["y","n"]:
        lettre = input("(y/n): ")
        
    if lettre == "y":
        return True
    else:
        return False
    
min_longueur = chiffre(chr = input("Entrer la longueur minimale: "))
possede_chiffre = lettre(lettre = input(" Tu veux des nombres (y/n)? "))
possede_special = lettre(lettre = input("Tu veux des carateres speciaux (y/n)? "))

critere = genere_mdp(min_longueur, possede_chiffre, possede_special)

print(" Voici le mot de passe generer:", critere)
