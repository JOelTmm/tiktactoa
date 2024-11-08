def initialiser_tableau():
    """Crée un tableau de jeu vide (9 cases)"""
    return [" " for _ in range(9)]  

def verifier_victoire(tableau, joueur):
    """Vérifie si un joueur a gagné"""
    # Les combinaisons gagnantes
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    
    for combi in combinaisons_gagnantes:
        if tableau[combi[0]] == tableau[combi[1]] == tableau[combi[2]] == joueur:
            return True  
    return False  

def verifier_match_nul(tableau):
    """Vérifie si la partie est un match nul"""
    return " " not in tableau  
