from . import IA

class Joueur:
	"""Classe gerrant les informations et les interactions d'un joueur, elle a comme attribut :
	- la couleur du joueur
	- ses pieces (liste)"""
	

	def __init__(self, pieces, couleur, type_joueur):
		"""Constructeur définissant les attributs"""

		try:
			assert couleur == "ROUGE" or couleur == "BLEU"
		except:
			print("Erreur : {} n'est pas accepté par le constructeur de Joueur\n".format(couleur))
		else:
			try:
				assert type(pieces) == list
			except:
				print("Erreur : {}\nLe type de la variable pieces n'est pas accepté par le constructeur de Joueur\n".format(pieces))
			else:
				try:
					assert len(pieces) == 21
				except:
					print("Erreur : {}\nLa taille de la variable pieces n'est pas accepté par le constructeur de Joueur\n".format(pieces))
				else:
					self.couleur = couleur
					self.pieces = pieces
					self.derniere_piece_jouee = self.pieces[1]
					self.type_joueur = type_joueur
					if self.type_joueur == "MACHINE":
						self.ia = IA.IA(self)


	def choix_piece(self):
		"""Choisi la piece à jouer."""
		if self.type_joueur == "MACHINE":
			return self.ia.choix_piece()
		else:
			print("Veuillez entrer le numero de la piece ou (q) pour quitter : ")
			return input()



	def choix_rotation(self):
		"""Choisi d'effectuer une rotation ou non"""

		if self.type_joueur == "MACHINE":
			return self.ia.choix_rotation()
		else:
			print("Pour effectuer une rotation sur la pièce entrez (r).\nEntrez (f) quand vous avez fini.")
			return input()


	def choix_position_x(self):
		"""Choisi la position en x de la piece sur le plateau"""

		if self.type_joueur == "MACHINE":
			return self.ia.choix_position_x()
		else:
			print("Veuillez entrer la position en x du plateau ou (q) pour quitter : ")
			return input()


	def choix_position_y(self):
		"""Choisi la position en y de la piece sur le plateau"""

		if self.type_joueur == "MACHINE":
			return self.ia.choix_position_y()
		else:
			print("Veuillez entrer la position en y du plateau ou (q) pour quitter : ")
			return input()

	def afficher(self):
		"""Méthode affichant la couleur du joueur et ces pieces"""
		for i in range(len(self.pieces)):
			self.pieces[i].afficher()

		