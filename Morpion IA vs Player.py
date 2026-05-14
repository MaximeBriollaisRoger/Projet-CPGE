import numpy as np
from copy import copy

def initialisation():
    """
    renvoie un tableau numpy de taille 3x3
    rempli de zeros
    """
    return np.zeros((3,3))

def verif_case_vide(grille,lig,col):
    """
    verifie que la case d'indice
    [lig,col] de la grille est vide (=0)
    """
    if grille[lig][col]==0:
        return True
    else:
        return False

def demande_ligne_colonne(joueur,grille):
    print("c'est au joueur "+str(joueur)+" de jouer")
    est_valide=False
    while est_valide==False :
        lig=int(input("indiquez l'indice de la ligne:"))
        col=int(input("indiquez l'indice de la colonne:"))
        if verif_case_vide(grille,lig,col)==True:
            est_valide=True
    return (lig,col)

def jouer_case(lig, col, joueur, grille):
    """
    place dans la grille le symbole du joueur
    """
    grille[lig][col]=joueur
    return grille

def grille_remplie(grille_test):
    """
    renvoie True si la grille est remplie
            False sinon
    """
    est_remplie=True
    nb_lig,nb_col=grille_test.shape
    for i in range(nb_lig):
        for j in range(nb_col):
            if grille_test[i][j]==0:
                est_remplie=False
    return est_remplie


def verifie_victoire(joueur, grille_verif):
    """
    verifie si le joueur a aligne 3 pions
    et renvoie: True si c'est le cas
                False sinon
    """
    for lig in range(3): # verification direction horizontale
        if grille_verif[lig][0] == joueur and grille_verif[lig][1] == joueur and grille_verif[lig][2] == joueur:
            return True    
    for col in range(3): # verification direction verticale
        if grille_verif[0][col] == joueur and grille_verif[1][col] == joueur and grille_verif[2][col] == joueur:
            return True
    # verification en diagonale
    if (grille_verif[0][0] == joueur and grille_verif[1][1]==joueur and grille_verif[2][2]==joueur) or (grille_verif[0][2] == joueur and grille_verif[1][1]==joueur and grille_verif[2][0]==joueur):
        return True
    
    return False

def affiche_grille(grille_affiche):
    """
    affiche la grille dans la console
    """
    print(grille_affiche)
"""
# version 2 joueurs humains
# initialisation
game_over=False
grille = initialisation()
joueur =1

while game_over == False:
    lig,col=demande_ligne_colonne(joueur,grille)
    jouer_case(lig, col, joueur, grille)
    affiche_grille(grille)
    if (verifie_victoire(joueur, grille)==True) or grille_remplie(grille):
        game_over = True
    # changer de joueur:
    if joueur==1:
        joueur=2
    else: # si joueur ==2
        joueur=1
"""
# version 1 joueur humain et une IA
def minimax(grille_minimax, profondeur, maximisation):
    
    # cas d'arret de la recursion
    # c-a-d: la partie est finie)
    # le joueur2 (ordi) a gagne
    if verifie_victoire(2, grille_minimax):
        return float('inf')
    # le joueur1 (humain) a gagne
    elif verifie_victoire(1, grille_minimax):
        return -float('inf')
    elif grille_remplie(grille_minimax):
        return 0
    
    # cas où c'est à l'IA (joueur2) de jouer
    # l'IA cherche le score le plus grand possible
    if maximisation == True :
        meilleur_score = -1000
        for lig in range(3):
            for col in range(3):
                # on joue dans la premiere case vide
                if verif_case_vide(grille_minimax,lig,col) == True:
                    grille_minimax[lig][col] = 2
                    # on va jouer un coup à la place de l'humain
                    grille_copie = grille_minimax.copy()
                    score = minimax(grille_copie, profondeur+1, False)
                    grille_minimax[lig][col] = 0 # on enleve le coup qu'on vient de jouer de la grille
                    meilleur_score = max(score, meilleur_score)
        return meilleur_score
    # cas où c'est à l'humain (joueur1) de jouer
    # l'humain cherche le score le plus petit possible (le plus négatif)
    else:
        meilleur_score = 1000
        for lig in range(3):
            for col in range(3):
                if verif_case_vide(grille_minimax,lig,col) == True:
                    grille_minimax[lig][col] = 1
                    # on va jouer un coup à la place de l'IA
                    grille_copie = grille_minimax.copy()
                    score = minimax(grille_copie, profondeur+1, True)
                    grille_minimax[lig][col] = 0
                    meilleur_score = min(score, meilleur_score)
        return meilleur_score
   
def meilleur_coup(grille):
    meilleur_score = -10000
    case = (-1,-1) # case à jouer
    for lig in range(3):
        for col in range(3):
            if verif_case_vide(grille,lig,col) == True:
                grille[lig][col] = 2
                score = minimax(grille, 0, False)
                grille[lig][col] = 0
                if score > meilleur_score:
                    meilleur_score = score
                    case = (lig, col)
    print("case vaut ",case)
    if case !=(-1,-1):
        jouer_case(case[0],case[1], 2, grille)
        return True
    return False



# version 1 joueur humain + 1 IA
# initialisation
game_over=False
grille = initialisation()

joueur =1


while game_over == False:
       
    
    lig,col = demande_ligne_colonne(joueur,grille)
    jouer_case(lig, col, joueur, grille)
    affiche_grille(grille)
    
    if (verifie_victoire(joueur, grille)==True) or grille_remplie(grille):
        game_over = True        
    joueur =2 # c'est au joueur2 de jouer (l IA)
               
    if game_over == False :
                
        if meilleur_coup(grille):
        
            
            affiche_grille(grille)        
            if (verifie_victoire(joueur, grille)==True) or grille_remplie(grille):
                game_over = True
            joueur = 1 # c'est au joueur1 de jouer (humain)