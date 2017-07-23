import random
import math
import os

def get_mask_word(mot_complet, lettres_trouvees):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
        mot_masque += " "

    return mot_masque

replay = 'y'
score = 0;

print("\n------------ Bienvenue dans le jeu du Pendu !!! ------------\n")

while replay == 'y':

    trouve = []
    coup = 10

    mode = input("------------ Choissisez votre mode de jeu : (1: un joueur * 2: deux joueurs) : ")

    # Verify if mode is numeric and equal to 1 or 2
    while ( not mode.isnumeric() or (int (mode) != 1 and int (mode) != 2) ):
        print("Choix incorrect")
        mode = input(" ------------ Choissisez votre mode de jeu : (1: un joueur * 2: deux joueurs) : ")

    mode = int(mode)

    if mode == 1:
        # Choice the difficulty Choix de la difficulté
        level = input("\n------------ Choissisez votre difficulté (1:facile * 2:moyen * 3:difficile) : ")

        # Verify if level is numeric and equal to 1 or 2 or 3
        while (not level.isnumeric() or (int(level) != 1 and int(level) != 2 and int(level) != 3)):
            print("Choix incorrect")
            level = input("------------ Choissisez votre difficulté (1:facile * 2:moyen * 3:difficile) : ")

        level = int(level)
        
        if level == 1:
            file = "easy.txt"
        elif level == 2:
            file = "medium.txt"
        else:
            file = "hard.txt"
        
        # Choice a random word in the file compared the difficulty
        words = open(file).read().splitlines()
        secret_word = random.choice(words)
    else :
        secret_word = input("------------ Taper le mot secret à deviner : ")

        # Verify if secret_word is alpanumerique and betwenn 3 and 15 characters
        while (not secret_word.isalpha() or len(secret_word) < 3 or len(secret_word) > 15):
            print("Mot incorrect (le mot doit comporté des lettres et être compris entre 3 et 15 caractéres")
            secret_word = input("------------ Taper le mot secret à deviner : ")

        # If mode is two player the level is calculate with lenght of secret xord
        level = math.floor(len(secret_word) / 3)

        if (level > 3):
            level = 3

        # level 1 => 3 , 4 , 5
        # level 2 => 6 , 7 , 8
        # level 3 => 9 , 10 , 11 , 12 , 13 , 14 , 15

        secret_word = secret_word.upper()


    # Show the secret word
    #print(secret_word)

    # Begin the game
    print("\n\n------------ Aller vous trouver le mot secret ... ??? ------------\n")
    print(get_mask_word(secret_word,trouve))

    # While the word is not found and the number of try is upper 0
    while get_mask_word(secret_word,trouve).replace(' ' , '') != secret_word and coup > 0:

        print("Il vous reste" , coup , "coups")
        print("Score :", score)

        user_letter = input("\n------------ TAPER UNE LETTRE : ")

        # Verify if seizure is a letter
        while (len(user_letter) > 1 or not user_letter.isalpha()):
            print("Vous n'avez pas saisie une lettre valide.")
            user_letter = input("------------ TAPER UNE LETTRE : ")

        while (user_letter.upper() in trouve):
            print("Vous avez déjà saisie cette lettre.")
            user_letter = input("------------ TAPER UNE LETTRE : ")

        if user_letter.upper() in secret_word:
            print("\n### Trouve ( +" , level , "points) !! ###\n")
            trouve.append(user_letter.upper())
            score = score + level
        else:
            print("\n### Pas trouvé ( -" , 4-level , "points) !! ###\n")
            coup -= 1
            score = score - (4 - level)

        print(get_mask_word(secret_word,trouve))

        #print("user :" , get_mask_word(secret_word,trouve).replace(' ' , '') , "secret:" , secret_word)

    # End of the party and verify if user is find the world or no


    print("\n------------------------------------------------------------------------\n\n")

    if get_mask_word(secret_word,trouve).replace(' ' , '') == secret_word:
        print("GAGNE LE MOT ETAIT :" ,secret_word , " ( + " , (2 * level) , "points )")
        score = score + (2 * level)
        print("\nScore :", score)
    else:
        print("PERDU LE MOT ETAIT :", secret_word, "( - ", (2 * (4-level)), "points )")
        score = score - (2 * (4-level))
        print("\nScore :", score)

    # Ask player if he want replay

    replay = input("\n------------ VOULEZ VOUS REJOUER ? (y/n) : ")

    while (not replay.isalpha() or (replay != 'y' and replay != 'n')):
        print("Choix incorrect")
        replay = input("------------ VOULEZ VOUS REJOUER ? (y/n) : ")


# End of the game

print("\n------------------------------------------------------------------------\n\n")

print("------------ Votre score final est :" , score , "------------")

print("\n------------ Merci d'avoir jouer a bientot !!! ------------")







