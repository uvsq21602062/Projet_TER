def validation_entree(entree, taille_max):
	"""Fonction vérifiant le type et la valeur de l'entrée donné par le joueur en question."""
	
	try: 
		res = int(entree)
	except:
		if(entree != "q"):
			print("\nERREUR ENTREE : Le type de la valeur renseignée n'est pas valide\n")
		else:
			print("\nAu revoir\n")
	else:
		if(res < 0 or res > taille_max):
			print("\nERREUR ENTREE : La valeur donnée n'est pas dans le bon interval\n")
		else:
			return res
	return -1

def respect_regle(plateau, piece, x, y, numero_tour, verbose):
	"""Fonction vérifiant que l'action demandé
	respecte bien les règles et qu'il est possible de la placer."""
	
	if numero_tour == 0:
		if plateau.piece_point_depart(piece, x, y):
			return 1
		else:
			print("\nERREUR REGLE : votre piece ne se trouve pas sur un point de départ.")
			print("Pour rappel, votre piece doit recouvrir la case (4, 9) ou (9, 4) non occupée.\n")
			return 0
	if plateau.piece_dans_plateau(piece, x, y):
		if plateau.piece_sur_cases_libres(piece, x, y):
			if plateau.piece_cote(piece, x, y):
				if plateau.piece_angle(piece, x, y):
					return 1
				elif verbose:
					print("\nERREUR REGLE : Votre piece ne touche par les angles aucune piece de la meme couleur.\n")
			elif verbose:
				print("\nERREUR REGLE : Votre piece touche par les cotes une autre piece de la même couleur.\n")
		elif verbose:
			print("\nERREUR REGLE : Les cases concernées par la forme de la pièce ne sont pas libres.\n")
	elif verbose:
		print("\nERREUR REGLE : La piece dépasse du plateau. Veuillez rééssayer\n")
	
	return 0

def joueur_peut_jouer(plateau, joueur, numero_tour):
		"""Fonction regardant s'il est encore possible pour un joueur de placer une pièce sur
		le plateau. Cette fontion renvoie 1 si c'est encore possible et 0 sinon."""
		if numero_tour == 0:
			return 1
		for i in range(plateau.largeur):
			for j in range(plateau.largeur):
				for k in range(len(joueur.pieces)-1):
					for l in range(4):
						if respect_regle(plateau, joueur.pieces[k], i, j, numero_tour, 0):
							return 1
						joueur.pieces[k].rotation()
		return 0

def fin_partie(joueur_rouge, joueur_bleu):
	"""Fonction s'occupant de compter les points et d'élire le vainqueur de la partie"""
	
	print("\nPartie terminé !\n")
	points_rouge = 0
	points_bleu = 0
	# Si le joueur a posé toutes ses pièces
	if len(joueur_rouge.pieces) == 0:
		# Si il a fini par la pièce "carré solitaire"
		if joueur_rouge.derniere_piece_jouee.largeur == 1:
			points_rouge += 20
		else:
			points_rouge += 15
	# Sinon on retire le nombre de carrés non posés
	else:
		for i in range(len(joueur_rouge.pieces)):
			for j in range(joueur_rouge.pieces[i].largeur):
				for k in range(joueur_rouge.pieces[i].largeur):
					points_rouge -= joueur_rouge.pieces[i].forme[j][k]
	
	# On fait la même chose pour le joueur bleu
	if len(joueur_bleu.pieces) == 0:
		if joueur_bleu.derniere_piece_jouee.largeur == 1:
			points_bleu += 20
		else:
			points_bleu += 15
	else:
		for i in range(len(joueur_bleu.pieces)):
			for j in range(joueur_bleu.pieces[i].largeur):
				for k in range(joueur_bleu.pieces[i].largeur):
					points_bleu -= joueur_bleu.pieces[i].forme[j][k]

	# Affichage des résultats
	print("Points du joueur ROUGE : ", points_rouge)
	print("Points du joueur BLEU : ", points_bleu)
	if points_rouge > points_bleu:
		print("Le joueur ROUGE gagne !")
	elif points_rouge < points_bleu:
		print("Le joueur BLEU gagne !")
	else:	
		print("Match nul")

def tour(plateau, joueur, numero_tour):
	"""Fonction permettant de dérouler un tour : 
		- Demande la pièce à jouer
		- Demande la position en x
		- Demande la position en y
		- Pose de la pièce si le informations sont cohérentes."""
	
	entree = ""
	# Demande de la piece
	while entree != 'q' and entree != "reussite":
		entree = joueur.choix_piece()
		indice_piece = validation_entree(entree, len(joueur.pieces)-1)
		if indice_piece != -1 and indice_piece != 'q':
			print("Vous avez demandé cette piece : ")
			joueur.pieces[indice_piece].afficher()
			# Demande une eventuelle rotation
			while entree != 'f':
				entree = joueur.choix_rotation()
				if(entree == 'r'):
					joueur.pieces[indice_piece].rotation()
			# Demande la position en x
			while entree != 'q' and entree !="reussite" and entree != "retry":
				entree = joueur.choix_position_x()
				x_pos = validation_entree(entree, plateau.largeur-1)
				if x_pos != -1 and x_pos != 'q' :
					# Demande la position en y
					while entree != 'q' and entree != "reussite" and entree != "retry" :
						entree = joueur.choix_position_y()
						y_pos = validation_entree(entree, plateau.largeur-1)
						if y_pos != -1 and y_pos != 'q':
							if respect_regle(plateau, joueur.pieces[indice_piece], x_pos, y_pos, numero_tour, 1):
								plateau.pose_piece(joueur.pieces[indice_piece], x_pos, y_pos)
								joueur.derniere_piece_jouee = joueur.pieces[indice_piece]
								del joueur.pieces[indice_piece]
								entree = "reussite"
							else:
								entree = "retry"

	return entree