from mes_classes import arbre
from mes_classes import joueur

class IA(joueur.Joueur):
	"""Classe héritant de joueur gerrant toutes les informations et décision
	de l'IA. elle a comme attribut :
	- un objet Joueur"""

	def __init__(self, pieces, couleur, type_joueur, type_arbre, profondeur_arbre, nbr_pieces_tester, nbr_cases_tester):
		"""Constructeur définissant les attributs."""
		
		super().__init__(pieces, couleur, type_joueur)
		self.type_arbre = type_arbre
		self.profondeur_arbre = profondeur_arbre
		self.nbr_pieces_tester = nbr_pieces_tester
		self.nbr_cases_tester = nbr_cases_tester
		self.indice_piece = 0
		self.rotation = 0
		self.x = 0
		self.y = 0

	def evaluation_coup(self, plateau, joueur_adverse, numero_tour):
		"""Cette methode appelle la méthode de arbre pour trouver un coup à jouer"""

		a = arbre.Arbre(self, joueur_adverse, plateau, self.type_arbre, self.nbr_pieces_tester, self.nbr_cases_tester)
		a.evaluation_arbre(self.profondeur_arbre, numero_tour)
		self.indice_piece = a.noeud_racine.indice_piece
		self.rotation = a.noeud_racine.rotation
		self.x = a.noeud_racine.x
		self.y = a.noeud_racine.y


