from random import *

class IA:
	"""Classe gerrant toutes les informations et décision
	de l'IA. elle a comme attribut :
	- un objet Joueur"""

	def __init__(self, joueur):
		"""Constructeur définissant les attributs."""
		self.joueur = joueur

	def choix_piece(self):
		"""Choisi une piece de manière aléatoire."""

		nbre_pieces = len(self.joueur.pieces)
		return str(randint(0, nbre_pieces-1))

	def choix_rotation(self):
		"""Choisi d'effectuer une rotation ou non"""

		if random() < 0.5: return 'f'
		else: return 'r'

	def choix_position_x(self):
		"""Choisi la position en x de la piece sur le plateau"""

		return str(randint(0, 14))

	def choix_position_y(self):
		"""Choisi la position en y de la piece sur le plateau"""

		return str(randint(0, 14))


