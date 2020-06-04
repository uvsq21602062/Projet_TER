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
			self.mapping_rouge = []
			self.mapping_bleu = []
			self.initialisation_mapping()
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

		if self.pieces[-1].couleur == "ROUGE":
			self.actualisation_mapping(self.mapping_rouge, self.pieces[-1])
		if self.pieces[-1].couleur == "BLEU":
			self.actualisation_mapping(self.mapping_bleu, self.pieces[-1])

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



	def initialisation_mapping(self):
		"""Initialise les deux attributs de mapping pour le déput de la partie :
		on prend toutes les cases autour (-4 en x et -4 en y) des points de départ."""

		# Pour le premier point de départ
		for i in range(5):
			for j in range(5):
				self.mapping_rouge.append((i,j+5))
				self.mapping_bleu.append((i,j+5))

		# Pour le deuxième point de départ
		for i in range(5):
			for j in range(5):
				self.mapping_rouge.append((i+5,j))
				self.mapping_bleu.append((i+5,j))



	def actualisation_mapping(self, mapping, piece):
		"""Cette méthode permet de créer un tableau contenant les cases potentiels sur lesquels
		une certaine pièce pourrait être posé. Elle permet, lors de la recherche des coups possibles,
		de ne pas avoir à tester toutes les cases du plateau."""


		# On observe les cases de la nouvelle piece pour voir les nouveaux emplacements possibles.
		for i in range(7):
			for j in range(7):
				for k in range(piece.largeur):
					for l in range(piece.largeur):
						if piece.x+k+1-i < self.largeur and piece.x+k+1-i >= 0\
						and piece.y+l+1-j < self.largeur and piece.y+l+1-j >= 0:
							if self.cases[piece.x+k+1-i][piece.y+l+1-j] == "VIDE":
								mapping.append((piece.x + k + 1 - i, piece.y + l + 1 - j))

		# On supprime les doublons
		mapping = list(set(mapping))

		# On parcours le tableau maping pour regarder si toutes les cases sont bien vides
		for i in mapping:
			if self.cases[i[0]][i[1]] == piece.couleur:
				del i






	def afficher(self):
		"""Methode affichant le plateau dans le terminal."""

		for i in range(self.largeur):
			print("|", end='')
			for j in range(self.largeur):
				if self.cases[j][self.largeur-1 - i] == "ROUGE":
					print(" {}".format(self.cases[j][self.largeur-1 - i]), end='|')
				else:
					print(" {} ".format(self.cases[j][self.largeur-1 - i]), end='|')
			print()
		print()



		