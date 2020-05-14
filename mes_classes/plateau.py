class Plateau:
	"""Classe gerrant les informations du plateau de jeu, elle a comme attribut :

	- sa taille
	- ses pieces (liste)
	- l'etat de chacune des cases (liste à deux dimension."""

	def __init__(self, largeur):
		"""Constructeur définissant les attributs et mettant
		à 'vide' toutes les cases du plateau."""

		try:
			assert type(largeur) == int and largeur > 0
		except:
			print("Erreur : {} n'est pas accepté par le constructeur de Plateau\n".format(largeur))
		else:
			self.largeur = largeur
			self.pieces = []
			self.cases = [["VIDE" for j in range(largeur)] for i in range(largeur)]
			# On définit en plus les deux points de départ
			self.cases[4][9] = "DEPART"
			self.cases[9][4] = "DEPART"

	def pose_piece(self, piece, x, y):
		"""Méthode permettant de supprimer la piece du stock de piece d'un joueur et ajouter
		cette piece au plateau et déinir les cases prises par cette piece."""

		self.pieces.append(piece)
		self.pieces[-1].x = x
		self.pieces[-1].y = y
		for i in range(self.pieces[-1].largeur):
			for j in range(self.pieces[-1].largeur):
				if self.pieces[-1].forme[i][j] == 1:
					self.cases[self.pieces[-1].x + i][self.pieces[-1].y + j] = self.pieces[-1].couleur

	def piece_dans_plateau(self, piece, x, y):
		"""Méthode permettant de vérifier si une pièce ne dépasse pas le plateau."""

		if (x+piece.largeur > self.largeur-1) or (y+piece.largeur >self.largeur-1):
			for i in range(piece.largeur):
				for j in range(piece.largeur):
					if piece.forme[i][j] == 1 and (((x+i) > self.largeur-1) or ((y+j) > self.largeur-1)):
						return 0
		return 1

	def piece_sur_cases_libres(self, piece, x, y):
		"""Méthode vérifiant que toutes les cases concernées par la forme de la piece
		sont libres."""

		for i in range(piece.largeur):
			for j in range(piece.largeur):
				if piece.forme[i][j] == 1 and self.cases[x+i][y+j] != "VIDE":
					return 0
		return 1

	def piece_cote(self, piece, x, y):
		"""Méthode vérifiant qu'aucune des cases d'une pièce ne touche par les cotés
		une autre piece de la même couleur."""

		for i in range(piece.largeur):
			for j in range(piece.largeur):
				if piece.forme[i][j] == 1:
					if x+i+1 < self.largeur:
						if self.cases[x+i+1][y+j] == piece.couleur:
							return 0
					if x+i-1 >= 0:
						if self.cases[x+i-1][y+j] == piece.couleur:
							return 0
					if y+j+1 < self.largeur:
						if self.cases[x+i][y+j+1] == piece.couleur:
							return 0
					if y+j-1 >= 0:
						if self.cases[x+i][y+j-1] == piece.couleur:
							return 0
		return 1

	def piece_angle(self, piece, x, y):
		"""Méthode vérifiant qu'au moins une des cases d'une pièce touche par les angles
		une autre piece de la même couleur."""

		for i in range(piece.largeur):
			for j in range(piece.largeur):
				if piece.forme[i][j] == 1:
					if x+i+1 < self.largeur and y+j+1 < self.largeur:
						if self.cases[x+i+1][y+j+1] == piece.couleur: return 1

					if x+i-1 >= 0 and y+j+1 < self.largeur:
						if self.cases[x+i-1][y+j+1] == piece.couleur: return 1
					
					if x+i+1 < self.largeur and y+j-1 >= 0:
						if self.cases[x+i+1][y+j-1] == piece.couleur: return 1

					if x+i-1 >= 0 and y+j-1 >= 0:
						if self.cases[x+i-1][y+j-1] == piece.couleur: return 1
		return 0

	def piece_point_depart(self, piece, x, y):
		"""Méthode vérifiant qu'une piece se trouve sur un des points de départ non occupé."""

		for i in range(piece.largeur):
			for j in range(piece.largeur):
				try:
					if piece.forme[i][j] == 1 and self.cases[x+i][y+j] == "DEPART":
						return 1
				except: pass

	def afficher(self):
		"""Methode affichant le plateau dans le terminal."""

		for i in range(self.largeur):
			print("|", end='')
			for j in range(self.largeur):
				print(" {} ".format(self.cases[j][self.largeur-1 - i]), end='|')
			print()
		print()



		