from mes_classes import joueur
from mes_classes import plateau
import definition_des_pieces

joueur_rouge = joueur.Joueur(definition_des_pieces.pieces_rouge, "ROUGE")
joueur_bleu = joueur.Joueur(definition_des_pieces.pieces_bleu, "BLEU")

plateau = plateau.Plateau(14)



def validation_entree(entree, taille_max):
	"""Fonction vérifiant le type et la valeur de l'entree donné par le joueur en question."""
	
	try: 
		res = int(entree)
	except:
		if(entree != "q"):
			print("Le type de la valeur renseignée n'est pas valide")
		else:
			print("Au revoir")
	else:
		if(res < 0 or res > taille_max):
			print("La valeur donnée n'est pas dans le bon interval")
		else:
			return res
	return -1

def respect_regle(piece, x, y):
	"""Fonction vérifiant que l'action demandé
	respecte bien les règles et qu'il est possible de la placer."""
	
	if plateau.piece_dans_plateau(piece, x, y):
		if plateau.piece_sur_cases_libres(piece, x, y):
			return 1
		else:
			print("Les cases concernées par la forme de la pièce ne sont pas libres")
			return 0
	else:
		print("La piece dépasse du plateau. Veuillez rééssayer")
		return 0

def tour(plateau, joueur):
	"""Fonction permettant de dérouler un tour : 
		- Demande la pièce à jouer
		- Demande la position en x
		- Demande la position en y
		- Pose de la pièce si le informations sont cohérentes."""
	
	entree = ""

	while entree != 'q' and entree != "reussite":
		print("Veuillez entrer le numero de la piece ou (q) pour quitter : ")
		entree = input()
		indice_piece = validation_entree(entree, len(joueur.pieces)-1)
		if indice_piece != -1 and indice_piece != 'q':
			print("Vous avez demandé cette piece : ")
			joueur.pieces[indice_piece].afficher()
			while entree != 'f':
				print("Pour effectuer une rotation sur la pièce entrez (r) ou (f) pour fermer")
				entree = input()
				if(entree == 'r'):
					joueur.pieces[indice_piece].rotation()

			while entree != 'q' and entree !="reussite" and entree != "retry":
				print("Veuillez entrer la position en x du plateau ou (q) pour quitter : ")
				entree = input()
				x_pos = validation_entree(entree, plateau.largeur-1)
				if x_pos != -1 and x_pos != 'q' :

					while entree != 'q' and entree != "reussite" and entree != "retry" :
						print("Veuillez entrer la position en y du plateau ou (q) pour quitter : ")
						entree = input()
						y_pos = validation_entree(entree, plateau.largeur-1)
						if y_pos != -1 and y_pos != 'q':
							if respect_regle(joueur.pieces[indice_piece], x_pos, y_pos):
								plateau.pose_piece(joueur.pieces[indice_piece], x_pos, y_pos)
								del joueur.pieces[indice_piece]
								entree = "reussite"
							else:
								entree = "retry"

	return entree

def jeu(plateau, joueur_rouge, joueur_bleu):
	"""Fonction qui déroule toute une partie."""
	ret = ""
	while ret != 'q':
		print("Au joueur rouge de jouer !")
		ret = tour(plateau, joueur_rouge)
		plateau.afficher()
		if  ret != 'q' :
			print("Au joueur bleu de jouer !")
			ret = tour(plateau, joueur_bleu)
			plateau.afficher()



jeu(plateau, joueur_rouge, joueur_bleu)