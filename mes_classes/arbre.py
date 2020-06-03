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

	def __init__(self, joueur, joueur_adverse, plateau, type_evaluation, nbre_pieces_a_tester, nbre_cases_a_tester):
		"""Constructeur définissant les attributs"""

		self.noeud_racine = Noeud(joueur_adverse.couleur, None, None, None, None, None)
		self.joueur = joueur
		self.joueur_adverse = joueur_adverse
		self.plateau = plateau
		self.type_evaluation = type_evaluation
		self.nbre_pieces_a_tester = nbre_pieces_a_tester
		self.nbre_cases_a_tester = nbre_cases_a_tester



	def evaluation_arbre(self, profondeur, numero_tour, noeud=None, plateau=None, joueur=None, joueur_adverse=None,\
		alpha = -1000, beta = 1000):
		"""Fonction déployant les coups possibles dans l'arbre jusqu'à une certaine profondeur.
		De plus elle applique au passage la méthode minmax avec l'elagage alphabeta sur l'arbre."""

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


		# Si le noeud est une feuille et qu'on se trouve à la profondeur max qu'on voulait atteindre, on évalue le noeud.
		if len(noeud.noeuds_fils) == 0 and profondeur == 0:
			noeud.valeur = self.fonction_evaluation(plateau_bis, joueur_actuel, joueur_suivant)
			return noeud.valeur
		
		# Sinon on fait une recherche des coups possibles sur le noeud tout en appliquant minmax et alphabeta.
		if self.type_evaluation == "DETERMINISTE":
			noeud.valeur = self.recherche_deterministe_minmax_alphabeta(profondeur, numero_tour, noeud,\
				plateau_bis, joueur_actuel, joueur_suivant, alpha, beta)
		else:
			noeud.valeur = self.recherche_probabiliste_minmax_alphabeta(profondeur, numero_tour, noeud,\
				plateau_bis, joueur_actuel, joueur_suivant, alpha, beta)

		# Cette dernière condition permet de mettre au noeud racine le coup à jouer
		if noeud is self.noeud_racine:
			for i in range(len(noeud.noeuds_fils)):
				if noeud.noeuds_fils[i].valeur == noeud.valeur:
					noeud.indice_piece = noeud.noeuds_fils[i].indice_piece
					noeud.rotation = noeud.noeuds_fils[i].rotation
					noeud.x = noeud.noeuds_fils[i].x
					noeud.y = noeud.noeuds_fils[i].y
					return noeud.valeur

		return noeud.valeur
		



	def recherche_probabiliste_minmax_alphabeta(self, profondeur, numero_tour, noeud, plateau, joueur_actuel,\
		joueur_suivant, alpha, beta):
		"""Cette méthode fait une recherche des coups possibles et 
		applique la méthode minmax et alphabeta sur les noeuds recherchés.
		Ainsi la recherche n'a pas besoin d'être couplete grace à l'élagage.
		Elle est appelé par la méthode minmax et appelle la méthode minmax.
		L'interet de cette méthode est d'alléger l'écriture de minmax."""

		valeur_minmax = 0
		# Si le noeud est un noeud joueur, on va chercher à le maximiser
		if noeud.couleur == self.joueur.couleur or noeud is self.noeud_racine:
			valeur_minmax = -1000
			# Debut de la boucle de recherche
			# Pour un certain nombre de pieces du joueur
			for i in range(self.nbre_pieces_a_tester):
				indice_piece = randint(0, len(joueur_suivant.pieces)-1)
				# On fait une copie pour pouvoir effectuer une rotation dessus sans modifier directement la piece
				piece_bis = copy.deepcopy(joueur_suivant.pieces[indice_piece])
				# Pour chaque rotation de la piece
				for j in range(4):
					# Pour un certain nombre de cases à tester
					for k in range(self.nbre_cases_a_tester):
						x = randint(0, plateau.largeur-1)
						y = randint(0, plateau.largeur-1)
						# Si ce coup respecte les regles, alors on créer un nouveau noeud
						if regles.respect_regle(plateau, piece_bis, x, y, numero_tour, 0) == 0:
							noeud.noeuds_fils.append(Noeud(joueur_suivant.couleur, noeud, indice_piece, j, x, y))

							# On lance l'appel récursif pour evaluer ce noeud fils
							valeur = self.evaluation_arbre(profondeur-1, numero_tour+1, noeud.noeuds_fils[-1], plateau,\
								joueur_suivant, joueur_actuel, alpha, beta)
							# On prend le max
							if valeur > valeur_minmax:
								valeur_minmax = valeur
							# Si on a pas rencontrer de noeud superieur, on effectue une coupure beta
							if beta <= valeur_minmax:
								return valeur_minmax
							# Sinon on actualise la valeur de alpha
							if alpha < valeur_minmax:
								alpha = valeur_minmax

					piece_bis.rotation()

		# Sinon on va chercher à le minimiser
		else:
			valeur_minmax = 1000
			for i in range(self.nbre_pieces_a_tester):
				indice_piece = randint(0, len(joueur_suivant.pieces)-1)
				piece_bis = copy.deepcopy(joueur_suivant.pieces[indice_piece])
				# Pour chaque rotation de la piece
				for j in range(4):
					# Pour un certain nombre de cases à tester
					for k in range(self.nbre_cases_a_tester):
						x = randint(0, plateau.largeur-1)
						y = randint(0, plateau.largeur-1)
						# Si ce coup respecte les regles, alors on créer un nouveau noeud
						if regles.respect_regle(plateau, piece_bis, x, y, numero_tour, 0) == 0:
							noeud.noeuds_fils.append(Noeud(joueur_suivant.couleur, noeud, indice_piece, j, x, y))
							
							valeur = self.evaluation_arbre(profondeur-1, numero_tour+1, noeud.noeuds_fils[-1], plateau,\
								joueur_suivant, joueur_actuel, alpha, beta)
							
							if valeur < valeur_minmax:
								valeur_minmax = valeur
							if alpha >= valeur_minmax:
								return valeur_minmax
							if beta > valeur_minmax:
								beta = valeur_minmax

					piece_bis.rotation()

		return valeur_minmax


	def recherche_deterministe_minmax_alphabeta(self, profondeur, numero_tour, noeud, plateau, joueur_actuel,\
		joueur_suivant, alpha, beta):
		"""Cette méthode fait une recherche des coups possibles et 
		applique la méthode minmax et alphabeta sur les noeuds recherchés.
		Ainsi la recherche n'a pas besoin d'être complété grace à l'élagage.
		Elle est appelé par la méthode minmax et appelle la méthode minmax.
		L'interet de cette méthode est d'alléger l'écriture de minmax."""

		valeur_minmax = 0
		# Si le noeud est un noeud joueur, on va chercher à le maximiser
		if noeud.couleur == self.joueur.couleur or noeud is self.noeud_racine:
			valeur_minmax = -1000
			# Debut de la boucle de recherche
			# Pour toutes les pieces du joueur
			for i in range(len(joueur_suivant.pieces)):
				# On fait une copie pour pouvoir effectuer une rotation dessus sans modifier directement la piece
				piece_bis = copy.deepcopy(joueur_suivant.pieces[i])
				# Pour chaque rotation de la piece
				for j in range(4):
					# Pour toutes les cases du plateau
					for k in range(plateau.largeur):
						for l in range(plateau.largeur):
							# Si ce coup respecte les regles, alors on créer un nouveau noeud
							if regles.respect_regle(plateau, piece_bis, k, l, numero_tour, 0) == 0:
								noeud.noeuds_fils.append(Noeud(joueur_suivant.couleur, noeud, i, j, k, l))

								# On lance l'appel récursif pour evaluer ce noeud fils
								valeur = self.evaluation_arbre(profondeur-1, numero_tour+1, noeud.noeuds_fils[-1], plateau,\
									joueur_suivant, joueur_actuel, alpha, beta)
								# On prend le max
								if valeur > valeur_minmax:
									valeur_minmax = valeur
								# Si on a pas rencontrer de noeud superieur, on effectue une coupure beta
								if beta <= valeur_minmax:
									return valeur_minmax
								# Sinon on actualise la valeur de alpha
								if alpha < valeur_minmax:
									alpha = valeur_minmax

					piece_bis.rotation()

		# Sinon on va chercher à le minimiser
		else:
			valeur_minmax = 1000
			for i in range(len(joueur_suivant.pieces)):
				piece_bis = copy.deepcopy(joueur_suivant.pieces[i])
				# Pour chaque rotation de la piece
				for j in range(4):
					# Pour un certain nombre de cases à tester
					for k in range(plateau.largeur):
						for l in range(plateau.largeur):
							# Si ce coup respecte les regles, alors on créer un nouveau noeud
							if regles.respect_regle(plateau, piece_bis, k, l, numero_tour, 0) == 0:
								noeud.noeuds_fils.append(Noeud(joueur_suivant.couleur, noeud, i, j, k, l))
							
								valeur = self.evaluation_arbre(profondeur-1, numero_tour+1, noeud.noeuds_fils[-1], plateau,\
									joueur_suivant, joueur_actuel, alpha, beta)
						
								if valeur < valeur_minmax:
									valeur_minmax = valeur
								if alpha >= valeur_minmax:
									return valeur_minmax
								if beta > valeur_minmax:
									beta = valeur_minmax

					piece_bis.rotation()

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
		if joueur.couleur == self.joueur.couleur:
			return points_joueur - points_adverse
		else:
			return points_adverse - points_joueur



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


