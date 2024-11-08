def make_move():
    """Demande un coup au joueur et le valide"""
    while True:
        try:
            position = int(input(f"Joueur {current_player}, entrez une position (1-9) : ")) - 1
            # Demande au joueur de choisir une case entre 1 et 9 pour le converdi en position de 0 à 8
            
             if position < 0 or position > 8: # Vérifie que la position est bien entre 0 et 8 sinon affiche une erreur
                raise ValueError("Position invalide")  # Erreur hors limites
            
            if game_board[position] == " ":  # Vérifie si la case est libre espace " "
                game_board[position] = current_player  # Place le symbole du joueur ,X ou O
                break  # Sort de la boucle quand le coup est joué
            else:
                print("Case déjà prise. Choisissez-en une autre.")  # la case est deja prise 
        except ValueError as e:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")  # Message si le nombre n'est pas entre 1 et 9

def play_game():
    """Boucle principale du jeu"""
    while True:
        display_board()  # Affiche le plateau actuel
        make_move()  # Demande au joueur de jouer
        
        
        winner = check_winner()# Vérifie après chaque coup si quelqu’un a gagné
        if winner:
            display_board()  # Affiche le tableau final avec le coup gagnant
            print(f"Le joueur {winner} a gagné !")  # Affiche le gagnant
            break  # Termine la boucle du jeu
        elif is_draw():
        # Vérifie si le tableau est plein sans gagnant (match nul)
            display_board()  # Affiche le plateau complet pour montrer le match nul
            print("Match nul !")  # Indique que le jeu est nul
            break  # Termine la boucle du jeu
        
        switch_player()  # Passe au joueur suivant (X à O, ou vice versa)

# Lancer le jeu avec une option de rejouer
while True:
    play_game()  # Démarre une nouvelle partie
    replay = input("Voulez-vous rejouer ? (o/n) : ").lower()  # Demande si les joueurs veulent rejouer
    if replay != 'o':  # Si la réponse est différente de "o", arrête le jeu
        break
    
    # Réinitialise le tableau et le joueur pour recommencer
    game_board = [" " for _ in range(9)]  # Vide chaque case pour une nouvelle partie
    current_player = "X"  # Remet le joueur à X pour commencer
