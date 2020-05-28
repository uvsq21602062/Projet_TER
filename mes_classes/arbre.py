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
		self.noeud_racine = Noeud(joueur_adverse.couleur, None, None, 0, 0, 0)
		self.joueur = joueur
		self.joueur_adverse = joueur_adverse
		self.plateau = plateau
		self.numero_tour = numero_tour
		self.nbre_pieces_a_tester = 5
		self.nbre_cases_x_a_tester = 4
		self.nbre_cases_y_a_tester = 4



	def nouvel_etage(self, noeud=None, plateau=None, joueur=None, joueur_adverse=None):
		"""Méthode récursive construisant un nouvel étage
		(un etage adverse et un etage joueur) dans l'arbre"""

		# On gere les valeurs par défaut
		if noeud is None: noeud = self.noeud_racine
		if plateau is None: plateau = self.plateau
		if joueur is None: joueur = self.joueur
		if joueur_adverse is None: joueur_adverse = self.joueur_adverse

		# On applique les modifications du noeud actuel sur des nouvelles variables
		plateau_bis = copy.deepcopy(plateau)
		# Cette condition permet d'alterner la couleur des étages
		if noeud.couleur == joueur.couleur:
			joueur_actuel = copy.deepcopy(joueur)
			joueur_suivant = joueur_adverse # On ne fait pas de copy car on ne fait pas de modification sur cette variable
		else:
			joueur_actuel = copy.deepcopy(joueur_adverse)
			joueur_suivant = joueur
		# Si le noeud n'est pas racine, on applique les données du noeud sur des nouvelles variables
		# Le noeud racine est un peu spécial car il ne propose pas de coup
		if noeud is not self.noeud_racine:
			# On fait le nombre de rotation indiquée
			for j in range(noeud.rotation):
				joueur_actuel.pieces[noeud.indice_piece].rotation()
			# On pose la piece sur le plateau
			plateau_bis.pose_piece(joueur_actuel.pieces[noeud.indice_piece], noeud.x, noeud.y)
			# On retire la piece du joueur
			del joueur_actuel.pieces[noeud.indice_piece]

		# Si les noeuds fils n'ont pas été explorés, on les complète
		if len(noeud.noeuds_fils) == 0:
			self.recherche_coups_possibles_probabiliste(noeud, plateau_bis, joueur_suivant, self.numero_tour)
		# Sinon (si ils n'ont pas été explorés), on lance un appel récursif sur chacun.
		else:
			for i in range(len(noeud.noeuds_fils)):
				self.nouvel_etage(noeud.noeuds_fils[i], plateau_bis, joueur_suivant, joueur_actuel)





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
							noeud.noeuds_fils.append(Noeud(joueur.couleur, noeud, i, j, k, l))
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
							noeud.noeuds_fils.append(Noeud(joueur.couleur, noeud, indice_piece, j, x, y))
				joueur.pieces[indice_piece].rotation()



	def minmax(self, noeud=None, plateau=None, joueur=None, joueur_adverse=None):
		"""Fonction appliquant la méthode minmax sur l'arbre."""

		# On gere les valeurs par défaut
		if noeud is None: noeud = self.noeud_racine
		if plateau is None: plateau = self.plateau
		if joueur is None: joueur = self.joueur
		if joueur_adverse is None: joueur_adverse = self.joueur_adverse

		# On applique les modifications du noeud actuel sur des nouvelles variables
		plateau_bis = copy.deepcopy(plateau)
		# Cette condition permet d'alterner la couleur des étages
		if noeud.couleur == joueur.couleur:
			joueur_actuel = copy.deepcopy(joueur)
			joueur_suivant = joueur_adverse # On ne fait pas de copy car on ne fait pas de modification sur cette variable
		else:
			joueur_actuel = copy.deepcopy(joueur_adverse)
			joueur_suivant = joueur
		# Si le noeud n'est pas racine, on applique les données du noeud sur des nouvelles variables
		# Le noeud racine est un peu spécial car il ne propose pas de coup
		if noeud is not self.noeud_racine:
			# On fait le nombre de rotation indiquée
			for j in range(noeud.rotation):
				joueur_actuel.pieces[noeud.indice_piece].rotation()
			# On pose la piece sur le plateau
			plateau_bis.pose_piece(joueur_actuel.pieces[noeud.indice_piece], noeud.x, noeud.y)
			# On retire la piece du joueur
			del joueur_actuel.pieces[noeud.indice_piece]

		# Si les noeuds fils n'existe pas, alors le noeud est une feuille et donc on l'évalue
		if len(noeud.noeuds_fils) == 0:
			noeud.valeur = self.fonction_evaluation(plateau_bis, joueur_actuel, joueur_suivant)
			return noeud.valeur
		# Sinon si le noeud n'est pas une feuille, on lance un appel récursif et on calcul le min (ou max) de leur valeur
		else:
			valeur_minmax = 0
			# Si le noeud est un noeud joueur, on va chercher à le maximiser
			if noeud.couleur == self.joueur.couleur:
				valeur_minmax = -1000
				for i in range(len(noeud.noeuds_fils)):
					valeur = self.minmax(noeud.noeuds_fils[i], plateau_bis, joueur_suivant, joueur_actuel)
					if valeur > valeur_minmax:
						valeur_minmax = valeur
			# Sinon on va chercher à le minimiser
			else:
				valeur_minmax = 1000
				for i in range(len(noeud.noeuds_fils)):
					valeur = self.minmax(noeud.noeuds_fils[i], plateau_bis, joueur_suivant, joueur_actuel)
					if valeur < valeur_minmax:
						valeur_minmax = valeur
			noeud.valeur = valeur_minmax
			return valeur_minmax



	def fonction_evaluation(self, plateau, joueur, joueur_adverse):
		"""Cette méthode permet d'évaluer un noeud en fonction de la situation actuelle du joueur"""

		points_joueur = 0;
		points_adverse = 0;

		# On compte le nombre de cases de la couleur sur le plateau (nombre de points)
		for i in range(plateau.largeur):
			for j in range(plateau.largeur):
				if(plateau.cases[i][j] == joueur.couleur):
					points_joueur += 1
				elif(plateau.cases[i][j] == joueur_adverse.couleur):
					points_adverse += 1

		# On évalue en soustrayant le gain du joueur avec le gain de l'autre
		return points_joueur - points_adverse



	def afficher(self, noeud=None, niveau = 0):
		"""Méthode permetant d'afficher l'arbre dans le terminal"""

		# Gestion de la valeur noeud par défaut
		if noeud is None: noeud = self.noeud_racine
		for i in range(len(noeud.noeuds_fils)):
			print(' ' * 8 * niveau + "{} : points = {} couleur = {} indice_piece = {} x = {} y = {} rotation = {}".format(\
				i,\
				noeud.noeuds_fils[i].valeur,\
				noeud.noeuds_fils[i].couleur,\
				noeud.noeuds_fils[i].indice_piece,\
				noeud.noeuds_fils[i].x,\
				noeud.noeuds_fils[i].y,\
				noeud.noeuds_fils[i].rotation))
			if len(noeud.noeuds_fils[i].noeuds_fils):
				self.afficher(noeud.noeuds_fils[i], niveau + 1)


