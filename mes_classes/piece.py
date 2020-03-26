class Piece:
	"""Classe gerrant la structure d'une pièce et sa position elle a comme attributs :

	- une liste de deux dimmension représentant sa forme
	(exemple :	1 0 0
			1 0 0
			1 1 1) représente une équerre de 3x3
	- une largeur (coté le plus long)
	- une position sur le plateau représenté par x (largeur) et y (hauteur)
	cette position coorespond à l'indice [0][0] de la liste représentant la forme

	L'orientation de la pièce est modifié en modifiant la forme
	(exemple :	1 0 0				1 1 1
			1 0 0		-->		1 0 0
			1 1 1	rotation	        1 0 0)"""

	def __init__(self, largeur, couleur, id):
		"""Constructeur définissant les attributs et mettant
		à 0 la forme de la pièce"""
		print("\nAppel au constructeur de Piece avec l'attribut largeur = {} et l'attribut couleur = {}\n".format(largeur, couleur))

		try:
			assert type(largeur) == int and largeur > 0
			assert couleur == "ROUGE" or couleur == "BLEU"
		except:
			print("Erreur : {} ou {} n'est pas accepté par le constructeur de Piece\n".format(largeur, couleur))
		else:
			self.largeur = largeur
			self.x = 0
			self.y = 0
			self.forme = [[0 for j in range(largeur)] for i in range(largeur)]
			self.couleur = couleur
			self.id=id

	def rotation(self):
		"""Méthode effectuant une rotation de la pièce dans le sens des aiguilles d'une montre."""
		print("\nRotation dans le sens horaire d'une piece {}\n")

		self.afficher()
		print("\n--> Rotation -->\n")

		"""Variable temporaire dans laquelle sera stocké la valeur de chaque élément de la
		liste pour la permutation."""
		tmp = 0

		"""Boucle effectuant la permutation (un peu illisible mais difficile de faire autrement)"""
		for i in range(self.largeur//2):
			for j in range(i, self.largeur-1 - i):
				tmp = self.forme[i][j]
				self.forme[j][self.largeur-1 - i], tmp = tmp, self.forme[j][self.largeur-1 - i]
				self.forme[self.largeur-1 - i][self.largeur-1 - j], tmp = tmp, self.forme[self.largeur-1 - i][self.largeur-1 - j]
				self.forme[self.largeur-1 - j][i], tmp = tmp, self.forme[self.largeur-1 - j][i]
				self.forme[i][j] = tmp
		

		"""Cette phase consiste à vérifier qu'une rangée à x = 0 ou y = 0 ne soit pas
		complètement à 0. Dans ce cas on décale.
		(exemple :	1 0 0			1 1 1			0 0 0
				1 0 0		->	1 0 0		->	1 1 1
				1 1 0	rotation	0 0 0	décalage	1 0 0)"""
		self.afficher()
		print("\n--> Décalage -->\n")

		rangee_x_0 = 0
		rangee_y_0 = 0
		while rangee_x_0 == 0 or rangee_y_0 == 0:
			for i in range(self.largeur):
				rangee_x_0 += self.forme[0][i]
				rangee_y_0 += self.forme[i][0]
			if rangee_x_0 == 0:
				for i in range(self.largeur):
					for j in range(self.largeur-1):
						self.forme[j][i], self.forme[j+1][i] = self.forme[j+1][i], self.forme[j][i]
			if rangee_y_0 == 0:
				for i in range(self.largeur):
					for j in range(self.largeur-1):
						self.forme[i][j], self.forme[i][j+1] = self.forme[i][j+1], self.forme[i][j]

		self.afficher()


	def afficher(self):
		"""Méthode affichant la piece dans le terminal"""

		for i in range(self.largeur):
			for j in range(self.largeur):
				print("{} ".format(self.forme[j][self.largeur-1 - i]), end='')
			print()
		print()
