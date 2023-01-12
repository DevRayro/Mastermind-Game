from random import * # importe toutes les fonctions du module random pour la fonction randint (nombre aléatoire)

def regle(niveau): # fonction qui affiche les règles du jeu en fonction du niveau de difficulté choisi par le joueur
  if niveau == 1: 
    print("Règles du niveau Facile :") 
    print("- La combinaison secrète est composée de 4 chiffres compris entre 1 et 6.")
    print("- Vous avez 12 coups pour trouver la combinaison secrète.")
  elif niveau == 2:
    print("Règles du niveau Moyen :")
    print("- La combinaison secrète est composée de 5 chiffres compris entre 1 et 8.")
    print("- Vous avez 10 coups pour trouver la combinaison secrète.")
  elif niveau == 3:
    print("Règles du niveau Difficile :")
    print("- La combinaison secrète est composée de 6 chiffres compris entre 1 et 10.")
    print("- Vous avez 8 coups pour trouver la combinaison secrète.")
  else:
    print("Niveau non reconnu.")

def choixNiveau(): # fonction qui permet de choisir le niveau de difficulté du jeu
    while True:
        print("Choisissez un niveau de difficulté :")
        print("1. Facile")
        print("2. Moyen")
        print("3. Difficile")
        niveau = int(input("Votre choix : "))
        regle(niveau) # appel de la fonction regle pour afficher les règles du jeu en fonction du niveau de difficulté choisi
        if niveau == 1:
            maxCoup = 12
            tailleCombi = 4
            nbCouleur = 6
            break # permet de sortir de la boucle while
        elif niveau == 2:
            maxCoup = 10
            tailleCombi = 5
            nbCouleur = 8
            break # permet de sortir de la boucle while
        elif niveau == 3:
            maxCoup = 8
            tailleCombi = 6
            nbCouleur = 10
            break # permet de sortir de la boucle while
        else:
            print("Choix invalide, veuillez entrer un nombre entre 1 et 3.")
    return (maxCoup, tailleCombi, nbCouleur)

def genereCombiSecrete(tailleCombi, nbCouleur): # fonction qui génère la combinaison secrète aléatoirement en fonction du niveau de difficulté
    secret = [0]*tailleCombi
    for i in range (tailleCombi):
        secret[i] = randint(1, nbCouleur)
    return secret



def saisirProposition(tailleCombi, nbCouleur): # fonction qui permet de saisir la proposition du joueur en fonction du niveau de difficulté
    while True:
        c = [0]*tailleCombi
        for i in range (tailleCombi):
            c[i] = int(input("Entrez un chiffre entre 1 et "+str(nbCouleur)+": "))
        if estValide(c, nbCouleur):
            return c
        print("La combinaison saisie n'est pas valide.")

def estValide(c, nbCouleur): # fonction qui vérifie que la proposition du joueur est valide
    for i in range (len(c)):
        if c[i] < 1 or c[i] > nbCouleur:
            return False
    return True

def analyseProposition(c, secret): # fonction qui analyse la proposition du joueur et renvoie le nombre de chiffres bien placés et mal placés 
    matched = [] # liste qui contient les indices des chiffres mal placés déjà comptés pour éviter de les compter plusieurs fois 
    bienPlace = 0
    malPlace = 0
    for i in range (len(c)):
        if c[i] == secret[i]:
            bienPlace += 1
        else:
            for j in range (len(secret)):
                if c[i] == secret[j] and (j not in matched):
                    malPlace += 1
                    matched.append(j) # permet d'éviter de compter plusieurs fois le même chiffre mal placé
    return (bienPlace, malPlace)

def afficheIndication(T): # fonction qui affiche les indications du nombre de chiffres bien placés et mal placés
    bienPlace = T[0]
    malPlace = T[1]
    indication = "#" * bienPlace + "°" * malPlace
    print(indication)

def mastermind(): # fonction qui permet de jouer au jeu mastermind
    maxCoup, tailleCombi, nbCouleur = choixNiveau()
    secret = genereCombiSecrete(tailleCombi, nbCouleur)
    for i in range (maxCoup):
        c = saisirProposition(tailleCombi, nbCouleur)
        T = analyseProposition(c, secret)
        afficheIndication(T)
        if T[0] == tailleCombi:
            print("Vous avez gagné !")
            break # permet de sortir de la boucle for si le joueur a trouvé la combinaison secrète
    else:
        print("Vous avez perdu !")
        print("La combinaison secrète était : ", secret)
