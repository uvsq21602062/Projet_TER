class Plateau:
	"""Classe stockant toutes les informations du plateau de jeu :
	- sa taille
	- ses pieces
	- l'etat de chacune des cases."""
	def __init__(self, largeur):
		"""Constructeur définissant les attributs et mettant
		à 'vide' toutes les cases du plateau"""
		self.largeur = largeur
		self.pieces = []
		self.cases = [["vide" for i in range(largeur)] for i in range(largeur)]

