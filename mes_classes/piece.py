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
				1 1 1	rotation	1 0 0)"""

	def __init__(self, largeur):
		"""Constructeur définissant les attributs et mettant
		à 0 la forme de la pièce"""
		print("Appel au constructeur de Piece avec l'attribut largeur = {}\n".format(largeur))

		try:
			assert type(largeur) == int and largeur > 0
		except:
			print("Erreur : {} n'est pas accepté par le constructeur de Piece\n".format(largeur))
		else:
			self.largeur = largeur
			self.x = 0
			self.y = 0
			self.forme = [[0 for j in range(largeur)] for i in range(largeur)]

	def rotation(self):
		"""Méthode effectuant une rotation de la pièce dans le sens des aiguilles d'une montre."""
		print("Rotation dans le sens horaire d'une piece {}\n")

		self.afficher()
		print()

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
		
		self.afficher()

	def afficher(self):
		"""Méthode affichant la piece dans le terminal"""

		for i in range(self.largeur):
			for j in range(self.largeur):
				print("{} ".format(self.forme[i][j]), end='')
			print()