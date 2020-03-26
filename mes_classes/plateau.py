class Plateau:
	"""Classe gerrant les informations du plateau de jeu, elle a comme attribut :

	- sa taille
	- ses pieces (liste)
	- l'etat de chacune des cases (liste à deux dimension."""

	def __init__(self, largeur):
		"""Constructeur définissant les attributs et mettant
		à 'vide' toutes les cases du plateau"""
		print("\nAppel au constructeur de Plateau avec l'attribut largeur = {}\n".format(largeur))
		
		try:
			assert type(largeur) == int and largeur > 0
		except:
			print("Erreur : {} n'est pas accepté par le constructeur de Plateau\n".format(largeur))
		else:
			self.largeur = largeur
			self.pieces = []
			self.cases = [["VIDE" for j in range(largeur)] for i in range(largeur)]

	def pose_piece(self, piece, x, y):
		"""Méthode permettant de supprimer la piece du stock de piece d'un joueur et ajouter
		cette piece au plateau et déinir les cases prises par cette piece."""
		print("\nAppel à la méthode pose_piece avec la piece : \n")
		piece.afficher()

		self.pieces.append(piece)
		self.pieces[-1].x = x
		self.pieces[-1].y = y
		for i in range(self.pieces[-1].largeur):
			for j in range(self.pieces[-1].largeur):
				if self.pieces[-1].forme[i][j] == 1:
					self.cases[self.pieces[-1].x + i][self.pieces[-1].y + j] = self.pieces[-1].couleur

	def piece_dans_plateau(self, piece, x, y):
		"""Méthode permettant de vérifier si une pièce ne dépace pas le plateau"""

		if (x+piece.largeur > self.largeur-1) or (y+piece.largeur >self.largeur-1):
			for i in range(piece.largeur):
				for j in range(piece.largeur):
					if piece.forme[i][j] == 1 and (((x+i) > self.largeur-1) or ((y+j) > self.largeur-1)):
						return 0
		return 1

	def piece_sur_cases_libres(self, piece, x, y):
		"""Méthode vérifiant que toutes les cases concernées par la forme de la piece
		soient libre"""

		for i in range(piece.largeur):
			for j in range(piece.largeur):
				if piece.forme[i][j] == 1 and self.cases[x+i][y+j] != "VIDE":
					return 0
		return 1


	def afficher(self):
		"""Methode affichant le plateau dans le terminal"""

		for i in range(self.largeur):
			print("|", end='')
			for j in range(self.largeur):
				print(" {} ".format(self.cases[j][self.largeur-1 - i]), end='|')
			print()
		print()



		