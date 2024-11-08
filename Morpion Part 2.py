plateau = [[" " for _ in range(3)] for _ in range(3)]

def afficher_plateau():
    print("\n")
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9) 

def jouer_coup(joueur, ligne, colonne):
    if plateau[ligne][colonne] == " ":
        plateau[ligne][colonne] = joueur
        return True
    else:
        print("Cette case est déjà occupée, essayez une autre.")
        return False

tour = 0
while True:
    afficher_plateau()
    joueur = "X" if tour % 2 == 0 else "O"
    print(f"\nC'est au tour du joueur {joueur}")

    try:
        ligne = int(input("Entrez la ligne (0, 1, ou 2): "))
        colonne = int(input("Entrez la colonne (0, 1, ou 2): "))
        if ligne in [0, 1, 2] and colonne in [0, 1, 2]:
            if jouer_coup(joueur, ligne, colonne):
                tour += 1
        else:
            print("Veuillez entrer des valeurs valides entre 0 et 2.")
    except ValueError:
        print("Veuillez entrer des nombres valides.")

    if tour == 9:
        print("Match nul!")
        break

afficher_plateau()



