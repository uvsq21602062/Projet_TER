from random import *
from mes_classes import plateau
import regles
import copy

class Noeud:
	"""Classe implementant la notion de noeud dans un arbre.
	Cette classe a comme attributs :
	- la couleur du noeud 
	- une liste de noeuds fils
	- un noeud pere
	- une piece à jouer
	- une position en x
	- une position en y
	- un nombre de rotation
	- la valeur du noeud"""

	def __init__(self, couleur, noeud_pere, indice_piece, rotation, x, y):
		"""Constructeur définissant les attributs"""

		self.couleur = couleur
		self.noeuds_fils = []
		self.noeud_pere = noeud_pere
		self.indice_piece = indice_piece
		self.rotation = rotation
		self.x = x
		self.y = y
		self.valeur = 0



class Arbre:
	"""Classe permettant la construction et la maipulation d'un arbre des possibilité du jeu.
	Cette classe a comme attributs : 
	- la hauteur de l'arbre
	- un noeud père
	- la couleur du noeud pere"""

	def __init__(self, hauteur, joueur, joueur_adverse, plateau, numero_tour):
		"""Constructeur définissant les attributs"""

		self.hauteur = hauteur
		self.noeud_racine = Noeud("RACINE", None, None, 0, 0, 0)
		self.joueur = joueur
		self.joueur_adverse = joueur_adverse
		self.plateau = plateau
		self.numero_tour = numero_tour
		self.nbre_pieces_a_tester = 5
		self.nbre_cases_x_a_tester = 4
		self.nbre_cases_y_a_tester = 4


	def construction_racine(self):
		"""Méthode construisant l'arbre en explorant jusqu'à un certain niveau les coups possible"""

		self.recherche_coups_possibles_probabiliste(self.noeud_racine, self.plateau, self.joueur, self.numero_tour)



	def nouvel_etage(self, noeud, plateau, joueur):
		"""Méthode récursive construisant un nouvel étage
		(un etage adverse et un etage joueur) dans l'arbre"""

		# On applique les modifications du noeud actuel sur des nouvelles variables
		plateau_bis = copy.deepcopy(plateau)
		joueur_bis = copy.deepcopy(joueur)
		# Si le noeud n'est pas racine, on applique les données du noeud sur des nouvelles variables
		# Le noeud racine est un peu spécial car il ne propose pas de coup
		if noeud is not self.noeud_racine:
			# On fait le nombre de rotation indiquée
			for j in range(noeud.rotation):
				joueur_bis.pieces[noeud.indice_piece].rotation()
			# On pose la piece sur le plateau
			plateau_bis.pose_piece(joueur_bis.pieces[noeud.indice_piece], noeud.x, noeud.y)
			# On retire la piece du joueur
			del joueur_bis.pieces[noeud.indice_piece]

		# Si les noeuds fils n'ont pas été explorés, on les complète
		if len(noeud.noeuds_fils) == 0:
			self.recherche_coups_possibles_probabiliste(noeud, plateau_bis, joueur_bis, self.numero_tour)
		# Sinon (si ils n'ont pas été explorés), on lance un appel récursif sur chacun.
		else:
			for i in range(len(noeud.noeuds_fils)):
				print(i)
				self.nouvel_etage(noeud.noeuds_fils[i], plateau_bis, joueur_bis)





	def recherche_coups_possibles(self, noeud, plateau, joueur, numero_tour):
		"""Cette méthode va faire une recherche sur tous les coups possibles et les inscrire en fils de noeud."""

		# Pour chaque piece du joueur
		for i in range(len(joueur.pieces)):
			# Pour chaque rotation de la piece
			for j in range(4):
				# Pour chaque position en x
				for k in range(plateau.largeur):
					# Pour chaque position en y
					for l in range(plateau.largeur):
						# Si ce coup respecte les regles, alors on créer un nouveau noeud
						if regles.respect_regle(plateau, joueur.pieces[i], k, l, numero_tour, 0) == 0:
							noeud.noeuds_fils.append(Noeud(joueur.couleur, self, i, j, k, l))
				joueur.pieces[i].rotation()


	def recherche_coups_possibles_probabiliste(self, noeud, plateau, joueur, numero_tour):
		"""Cette méthode va faire une recherche sur tous les coups possibles et les inscrire en fils de noeud."""

		# Pour chaque piece du joueur
		for i in range(self.nbre_pieces_a_tester):
			indice_piece = randint(0, len(joueur.pieces)-1)
			# Pour chaque rotation de la piece
			for j in range(4):
				# Pour chaque position en x
				for k in range(self.nbre_cases_x_a_tester):
					x = randint(0, plateau.largeur-1)
					# Pour chaque position en y
					for l in range(self.nbre_cases_y_a_tester):
						y = randint(0, plateau.largeur-1)
						# Si ce coup respecte les regles, alors on créer un nouveau noeud
						if regles.respect_regle(plateau, joueur.pieces[indice_piece], x, y, numero_tour, 0) == 0:
							noeud.noeuds_fils.append(Noeud(joueur.couleur, self, indice_piece, j, x, y))
				joueur.pieces[indice_piece].rotation()



	def afficher(self, noeud, joueur, niveau = 0):
		"""Méthode permetant d'afficher l'arbre dans le terminal"""

		for i in range(len(noeud.noeuds_fils)):
			print(' ' * 8 * niveau + "{} : indice_piece = {} x = {} y = {} rotation = {}".format(\
				i,\
				noeud.noeuds_fils[i].indice_piece,\
				noeud.noeuds_fils[i].x,\
				noeud.noeuds_fils[i].y,\
				noeud.noeuds_fils[i].rotation))
			if len(noeud.noeuds_fils[i].noeuds_fils):
				joueur_bis = copy.deepcopy(joueur)
				del joueur_bis.pieces[noeud.noeuds_fils[i].indice_piece]
				self.afficher(noeud.noeuds_fils[i], joueur_bis, niveau + 1)


