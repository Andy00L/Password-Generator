# CE CODE PERMET DE GENERER UN MOT DE PASSE ALEATOIRE.

import random
import string


def genere_mdp(min_longueur, nombre, caratere_special):
    lettres = string.ascii_letters
    chiffre = string.digits
    special = string.punctuation
    
    caracteres = lettres
    if nombre:
        caracteres += chiffre
    if caratere_special:
        caracteres += special
    
    mot_de_passe = "" 
    valid_criteres = False
    possede_chiffre = False
    possede_special = False
    
    while not valid_criteres or len(mot_de_passe) < min_longueur:
        nouv_char = random.choice(caracteres)
        mot_de_passe += nouv_char
        
        if nouv_char in chiffre:
            possede_chiffre = True
        elif nouv_char in special:
            possede_special = True
            
        valid_criteres = True
        if nombre:
            valid_criteres = possede_chiffre
        if caratere_special:
            valid_criteres = valid_criteres and possede_special
            
    return mot_de_passe

min_longueur = int(input("Entrer la longueur minimale: "))
possede_chiffre = str(input(" Tu veux des nombres (y/n)? ")).lower == "y"
possede_special = str(input("Tu veux des carateres speciaux (y/n)? ")).lower == "y"
pwd = genere_mdp(min_longueur, possede_chiffre, possede_special)

print(" Voici le mot de passe generer:", pwd)
