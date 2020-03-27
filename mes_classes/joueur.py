class Joueur:
	"""Classe gerrant les informations et les interactions d'un joueur, elle a comme attribut :
	- la couleur du joueur
	- ses pieces (liste)"""
	

	def __init__(self, pieces, couleur):
		"""Constructeur définissant les attributs"""
		print("\nAppel au constructeur de Joueur avec l'attribut couleur = {}\n".format(couleur))

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

	def afficher(self):
		"""Méthode affichant la couleur du joueur et ces pieces"""
		for i in range(21):
			self.pieces[i].afficher()

		