from tkinter import *
from functools import partial
import regles

class Interface(Tk):
	"""Classe materialisant toutes les informations et les interactions jeu/partie graphique"""

	def __init__(self, plateau, largeur_fenetre, joueur_rouge, joueur_bleu):
		"""Constructeur ayant comme attribut :
		- un plateau de jeu
		- la largeur de la fenetre
		- la taille d'une case (du plateau et d'une piece)
		- l'indice de la piece actuel du joueur
		- les differents elements aparaissant dans la fenetre"""

		self.plateau = plateau
		self.largeur_fenetre = largeur_fenetre
		self.taille_case = self.largeur_fenetre/30
		self.indice_piece_actuelle = 0
		self.joueur_actuel = joueur_rouge
		self.joueur_suivant = joueur_bleu
		self.piece_x = 0
		self.piece_y = 0
		self.etat = 1
		self.numero_tour = 0
		self.score = ""

		Tk.__init__(self)
		self.geometry("{}x{}".format(largeur_fenetre, largeur_fenetre))

		self.canvas = Canvas(self)
		self.message_qui_joue = Label(self)
		self.message_instruction = Label(self)
		self.message_erreur = Label(self)
		self.message_erreur.configure(fg = "red")

		self.canvas.pack()
		self.message_qui_joue.pack()
		self.message_instruction.pack()
		self.message_erreur.pack()

		self.affiche_plateau()
		self.affiche_message(0)
		self.affiche_selection_piece()

		self.liaison_des_actions()


	#**********************
	# FONCTIONS D'AFFICHAGE
	#**********************


	def affiche_plateau(self):
		"""Cette fonction affiche le plateau de jeu que l'objet a en argument"""

		decalage_plateau = self.taille_case
		couleur_case = ""
		for i in range(self.plateau.largeur):
			for j in range(self.plateau.largeur):
				if self.plateau.cases[i][j] == "VIDE":
					couleur_case = "white"
				elif self.plateau.cases[i][j] == "ROUGE":
					couleur_case = "red"
				elif self.plateau.cases[i][j] == "BLEU":
					couleur_case = "blue"
				else:
					couleur_case = "green"
				self.canvas.create_rectangle(\
					(i*self.taille_case + decalage_plateau,\
					j*self.taille_case + decalage_plateau),\
					(i*self.taille_case + self.taille_case + decalage_plateau,\
					j*self.taille_case + self.taille_case + decalage_plateau),\
					fill=couleur_case, outline = "black")

	def affiche_message(self, erreur):
		"""Cette fonction s'occupe d'afficher le bon message en fonction de l'état de la partie"""

		# Si la partie n'est pas fini
		if self.etat != 3:
			# On définit le message du joueur qui joue
			if self.joueur_actuel.couleur == "BLEU":
				self.message_qui_joue["text"] = "Au joueur BLEU de jouer"
				self.message_qui_joue.configure(fg = "blue")
			else:
				self.message_qui_joue["text"] = "Au joueur ROUGE de jouer"
				self.message_qui_joue.configure(fg = "red")

			# On définit l'instruction pour jouer
			self.message_instruction["text"] = "Utilisez les fleches directionnel pour faire défiler ou déplacer vos pièces.\n"
			self.message_instruction["text"] += "Tapez r pour effectuer une rotation sur la piece\n"
			self.message_instruction["text"] += "Tapez ENTRER pour valider votre choix"

			# On définit le message d'erreur
			if erreur == 0:
				self.message_erreur["text"] = ""
			elif erreur == 1:
				self.message_erreur["text"] = "ERREUR REGLE : votre piece ne se trouve pas sur un point de départ"
			elif erreur == 2:
				self.message_erreur["text"] = "ERREUR REGLE : Votre piece ne touche par les angles aucune piece de la meme couleur"
			elif erreur == 3:
				self.message_erreur["text"] = "ERREUR REGLE : Votre piece touche par les cotes une autre piece de la même couleur"
			elif erreur == 4:
				self.message_erreur["text"] = "ERREUR REGLE : Les cases concernées par la forme de la pièce ne sont pas libres"
			elif erreur == 5:
				self.message_erreur["text"] = "ERREUR REGLE : La piece dépasse du plateau. Veuillez rééssayer"
			else:
				self.message_erreur["text"] = ""

		# Sinon on affiche le resultat
		else:
			self.message_qui_joue["text"] = 0
			self.message_erreur["text"] = 0
			self.message_instruction["text"] = self.resultat

	def affiche_selection_piece(self):
		"""Cette fonction affiche la selection des pieces"""

		couleur_case = ""
		decalage_selection_x = self.plateau.largeur*self.taille_case + 2*self.taille_case
		decalage_selection_y = self.taille_case
		for i in range(self.joueur_actuel.pieces[self.indice_piece_actuelle].largeur):
			for j in range(self.joueur_actuel.pieces[self.indice_piece_actuelle].largeur):
				if self.joueur_actuel.pieces[self.indice_piece_actuelle].forme[i][j] == 1:
					if self.joueur_actuel.pieces[self.indice_piece_actuelle].couleur == "ROUGE":
						couleur_case = "red"
					elif self.joueur_actuel.pieces[self.indice_piece_actuelle].couleur == "BLEU":
						couleur_case = "blue"
					self.canvas.create_rectangle(\
						(i*self.taille_case + decalage_selection_x,\
						j*self.taille_case + decalage_selection_y),\
						(i*self.taille_case + self.taille_case + decalage_selection_x,\
						j*self.taille_case + self.taille_case + decalage_selection_y),\
						fill=couleur_case, outline = "black")

	def affiche_piece_sur_plateau(self):
		"""Cette fonction positionne la piece actuelle sur le plateau pour
		que le joueur puisse visualiser son choix."""

		couleur_case = ""
		decalage_plateau = self.taille_case
		for i in range(self.joueur_actuel.pieces[self.indice_piece_actuelle].largeur):
			for j in range(self.joueur_actuel.pieces[self.indice_piece_actuelle].largeur):
				if self.joueur_actuel.pieces[self.indice_piece_actuelle].forme[i][j] == 1:
					if self.joueur_actuel.pieces[self.indice_piece_actuelle].couleur == "BLEU":
						couleur_case = "blue"
					elif self.joueur_actuel.pieces[self.indice_piece_actuelle].couleur == "ROUGE":
						couleur_case = "red"
					self.canvas.create_rectangle(\
						((i+self.piece_x)*self.taille_case + decalage_plateau,\
						(j+self.piece_y)*self.taille_case + decalage_plateau),\
						((i+self.piece_x)*self.taille_case + self.taille_case + decalage_plateau,\
						(j+self.piece_y)*self.taille_case + self.taille_case + decalage_plateau),\
						fill=couleur_case, outline = "black")


	#********************************
	# FONCTIONS GERANT LES EVENEMENTS
	#********************************

	def event_piece_suivante(self, event):
		"""Cette fonction est appelée lorsque le joueur appuie sur BAS,
		elle selectionne la prochaine piece du joueur à afficher."""

		if self.indice_piece_actuelle == len(self.joueur_actuel.pieces)-1:
			self.indice_piece_actuelle = 0
		else:
			self.indice_piece_actuelle += 1

		self.canvas.delete("all")
		self.affiche_selection_piece()
		self.affiche_plateau()

	def event_piece_precedente(self, event):
		"""Cette fonction est appelée lorsque le joueur appuie sur BAS,
		elle selectionne la piece precedente du joueur à afficher."""

		if self.indice_piece_actuelle == 0:
			self.indice_piece_actuelle = len(self.joueur_actuel.pieces)-1
		else:
			self.indice_piece_actuelle -= 1

		self.canvas.delete("all")
		self.affiche_selection_piece()
		self.affiche_plateau()
	
	def event_piece_rotation(self, event):
		"""Cette fonction est appelée lorsque le joueur appuie sur HAUT,
		elle effectue une rotation sur la piece actuelle"""

		self.joueur_actuel.pieces[self.indice_piece_actuelle].rotation()

		self.canvas.delete("all")
		self.affiche_plateau()
		if self.etat == 1:
			self.affiche_selection_piece()
		elif self.etat == 2:
			self.affiche_piece_sur_plateau()

	def event_piece_selectionne(self, event):
		"""Cette fonction est appelée lorsque l'utiliateur tape "ENTER" lors de la selection de la piece,
		elle appelle la fonction affiche_piece_plateau et change l'etat de la partie"""

		self.etat = 2

		self.canvas.delete("all")
		self.affiche_message(0)
		self.affiche_plateau()
		self.affiche_piece_sur_plateau()
		self.liaison_des_actions()

	def event_piece_deplace_gauche(self, event):
		"""Fonction appelée lorsque l'utilisateur appuie sur GAUCHE,
		Cette fonction déplace la piece sur le plateau vers la gauche"""

		if self.piece_x > 0: self.piece_x -= 1

		self.canvas.delete("all")
		self.affiche_plateau()
		self.affiche_piece_sur_plateau()

	def event_piece_deplace_droite(self, event):
		"""Fonction appelé lorsque l'utilisateur appuie sur DROITE,
		Cette fonction déplace la piece sur le plateau vers la gauche"""

		if self.plateau.piece_dans_plateau(self.joueur_actuel.pieces[self.indice_piece_actuelle], self.piece_x+1, self.piece_y):
			self.piece_x += 1

		self.canvas.delete("all")
		self.affiche_plateau()
		self.affiche_piece_sur_plateau()

	def event_piece_deplace_haut(self, event):
		"""Fonction appelé lorsque l'utilisateur appuie sur HAUT,
		Cette fonction déplace la piece sur le plateau vers la gauche"""

		if self.piece_y > 0: self.piece_y -= 1

		self.canvas.delete("all")
		self.affiche_plateau()
		self.affiche_piece_sur_plateau()

	def event_piece_deplace_bas(self, event):
		"""Fonction appelé lorsque l'utilisateur appuie sur BAS,
		Cette fonction déplace la piece sur le plateau vers la gauche"""

		if self.plateau.piece_dans_plateau(self.joueur_actuel.pieces[self.indice_piece_actuelle], self.piece_x, self.piece_y+1):
			self.piece_y += 1

		self.canvas.delete("all")
		self.affiche_plateau()
		self.affiche_piece_sur_plateau()

	def event_piece_pose(self, event):
		"""Fonction appelé lorsque l'utilisateur valide la position d'une piece sur le plateau,
		elle interoge la partie règle pour savoir si le choix respecte les règles.
		Si oui elle fait jouer le prochain joueur
		Sinon elle previent l'utilisateur qu'il doit jouer autre chose."""

		self.etat = 1
		# On test si la piece sur le plateau respecte les regles.
		erreur = regles.respect_regle(self.plateau, self.joueur_actuel.pieces[self.indice_piece_actuelle], self.piece_x, self.piece_y, self.numero_tour//2, 0)
		# S'il n'y a pas d'erreur
		if erreur == 0:
			# On pose la piece sur le plateau et on definit la derniere piece que le joueur a jouer
			self.plateau.pose_piece(self.joueur_actuel.pieces[self.indice_piece_actuelle], self.piece_x, self.piece_y)
			self.joueur_actuel.derniere_piece_jouee = self.joueur_actuel.pieces[self.indice_piece_actuelle]
			# On supprime la piece du joueur
			del self.joueur_actuel.pieces[self.indice_piece_actuelle]
			self.indice_piece_actuelle = 0
			self.numero_tour += 1
			# Les prochaines vérifications sont pour vérifier que un des deux joueurs peuvent jouer
			# et donc que ce n'est pas la fin de la partie. 
			if regles.joueur_peut_jouer(self.plateau, self.joueur_suivant, self.numero_tour//2):
				self.joueur_actuel, self.joueur_suivant = self.joueur_suivant, self.joueur_actuel
			elif regles.joueur_peut_jouer(self.plateau, self.joueur_actuel, self.numero_tour//2) == 0:
				# Si aucun des deux joueurs ne peut jouer, c'est la fin de la partie.
				self.resultat =  regles.fin_partie(self.joueur_actuel, self.joueur_suivant)
				self.etat = 3
		
		self.piece_x = 0
		self.piece_y = 0
		self.canvas.delete("all")
		self.affiche_message(erreur)
		self.affiche_plateau()
		self.affiche_selection_piece()
		self.liaison_des_actions()


	def liaison_des_actions(self):
		"""Cette fonction lie certaines touche à une action en fonction de l'etat de la partie."""
		
		self.unbind("<Up>")
		self.unbind("<Down>")
		self.unbind("<Left>")
		self.unbind("<Right>")
		self.unbind("r")
		self.unbind("<Return>")

		if self.etat == 1:
			self.bind("<Up>", self.event_piece_suivante)
			self.bind("<Down>", self.event_piece_precedente)
			self.bind("r", self.event_piece_rotation)
			self.bind("<Return>", self.event_piece_selectionne)
		
		elif self.etat == 2:
			self.bind("r", self.event_piece_rotation)
			self.bind("<Up>", self.event_piece_deplace_haut)
			self.bind("<Down>", self.event_piece_deplace_bas)
			self.bind("<Left>", self.event_piece_deplace_gauche)
			self.bind("<Right>", self.event_piece_deplace_droite)
			self.bind("<Return>", self.event_piece_pose)
