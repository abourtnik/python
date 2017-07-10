import random

def recup_mot_masque(mot_complet, lettres_trouvees):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
        mot_masque += " "

    return mot_masque

replay = 'y'

print("------------ Bienvenue dans le jeu du Pendu !!! ------------")

while replay == 'y':

    trouve = []
    coup = 10

    # Choix de la difficulté
    level = input("Choissisez votre difficulté (1:facile * 2:moyen * 3:difficile) : ")

    # Choix d'un mot au hasard dans le dictionnaire suivant la difficulté

    words = open('dictionnaire.txt').read().splitlines()
    secret_word = random.choice(words)

    print(secret_word)

    # Debut du jeu
    print("------------ Aller vous trouver le mot secret ... ??? ------------")
    print(recup_mot_masque(secret_word,trouve))

    # Si le mot n'a pas ete trouve et si le nombre de coup n est pas a egal a 0
    while recup_mot_masque(secret_word,trouve).replace(' ' , '') != secret_word and coup > 0:

        print("Il vous reste" , coup , "coups")

        user_letter = input("Tapez une lettre : ")

        # Verifie si la saisie est bien une lettre
        while (len(user_letter) > 1 or not user_letter.isalpha()):
            print("Vous n'avez pas saisi une lettre valide.")
            user_letter = input("Tapez une lettre : ")

        if user_letter.upper() in secret_word:
            print("------------ Trouve !! ------------")
            trouve.append(user_letter.upper())
        else:
            print("------------ Pas trouvé !! ------------")
            coup -= 1

        print(recup_mot_masque(secret_word,trouve))

        #print("user :" , recup_mot_masque(secret_word,trouve).replace(' ' , '') , "secret:" , secret_word)


    # Fin du jeu on verifie si le joueur a gagné ou non

    if recup_mot_masque(secret_word,trouve).replace(' ' , '') == secret_word:
        print("GAGNE LE MOT ETAIT :" ,secret_word)
    else:
        print("PERDU LE MOT ETAIT : " ,secret_word)

    # On redemande si le joueur veur rejouer

    replay = input("Voulez vous rejouer ? (y/n) : ")

print("------------ Merci d'avoir jouer a bientot !!! ------------")






