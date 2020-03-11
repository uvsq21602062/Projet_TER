class Plateau:
	"""Classe gerrant les informations du plateau de jeu :

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
			self.cases = [["vide" for j in range(largeur)] for i in range(largeur)]

	
	def afficher(self):
		"""Methode affichant le plateau dans le terminal"""

		for i in range(self.largeur):
			print("|", end='')
			for j in range(self.largeur):
				print(" {} ".format(self.cases[j][self.largeur-1 - i]), end='|')
			print()
		print()



		