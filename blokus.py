from mes_classes import IA
from mes_classes import joueur
from mes_classes import piece
from mes_classes import plateau
from mes_classes import interface
import regles
import definition_des_pieces


def jeu_sans_ihm(joueur_rouge, joueur_bleu, plateau_jeu):
	"""Fonction qui déroule toute une partie en ligne de commande."""

	joueur_rouge_peut_jouer = 1
	joueur_bleu_peut_jouer = 1
	numero_tour = 0
	ret = ""
	plateau_jeu.afficher()
	while ret != 'q' and (joueur_rouge_peut_jouer or joueur_bleu_peut_jouer):
		# On verifie que le joueur rouge peut jouer
		if not regles.joueur_peut_jouer(plateau_jeu, joueur_rouge, numero_tour):
			joueur_rouge_peut_jouer = 0;
		# Au joueur rouge de jouer
		if joueur_rouge_peut_jouer:
			print("Au joueur rouge de jouer !")
			if joueur_rouge.type_joueur == "HUMAIN":
				ret = regles.tour(plateau_jeu, joueur_rouge, numero_tour)
			else:
				regles.tour_machine(plateau_jeu, joueur_rouge, joueur_bleu, numero_tour)
			plateau_jeu.afficher()

		numero_tour += 1

		# On verifie que le joueur rouge peut jouer
		if not regles.joueur_peut_jouer(plateau_jeu, joueur_bleu, numero_tour):
			joueur_bleu_peut_jouer = 0;
		# Au joueur bleu de jouer
		if  joueur_bleu_peut_jouer and ret != 'q':
			print("Au joueur bleu de jouer !")
			if joueur_rouge.type_joueur == "HUMAIN":
				ret = regles.tour(plateau_jeu, joueur_bleu, numero_tour)
			else:
				regles.tour_machine(plateau_jeu, joueur_bleu, joueur_rouge, numero_tour)
			plateau_jeu.afficher()

		numero_tour += 1

	regles.fin_partie(joueur_rouge, joueur_bleu)


def choix_jeu():
	"""Fonction demandant à l'utilisateur de quelle manière il souhaite jouer."""

	type_interface = ""
	type_joueur_rouge = ""
	type_joueur_bleu = ""

	# On demande à l'utilisateur s'il souhaite jouer dans le terminal ou avec une interface graphique.
	while type_interface != 'g' and type_interface != 't':
		print("Tapez (g) pour jouer avec une interface graphique ou (t) pour jouer dans le terminal.")
		type_interface = input()

	# On demande le type du joueur rouge
	while type_joueur_rouge != 'm' and type_joueur_rouge != 'h':
		print("Tapez (m) pour definir le joueur rouge en machine (probabiliste) ou (h) sinon.")
		type_joueur_rouge = input()

	# On demande le type du joueur bleu
	while type_joueur_bleu != 'm' and type_joueur_bleu != 'h':
		print("Tapez (m) pour definir le joueur bleu en machine (deterministe) ou (h) sinon.")
		type_joueur_bleu = input()

	# Joueur rouge :
	if type_joueur_rouge == 'm':
		joueur_rouge = IA.IA(definition_des_pieces.pieces_rouge, "ROUGE", "MACHINE", "PROBABILISTE", 4, 6, 16)
	else: 
		joueur_rouge = joueur.Joueur(definition_des_pieces.pieces_rouge, "ROUGE", "HUMAIN")
	# Joueur bleu :
	if type_joueur_bleu == 'm':
		joueur_bleu = IA.IA(definition_des_pieces.pieces_bleu, "BLEU", "MACHINE", "DETERMINISTE", 1, 6, 16)
	else: 
		joueur_bleu = joueur.Joueur(definition_des_pieces.pieces_bleu, "BLEU", "HUMAIN")
	# Plateau :
	plateau_jeu = plateau.Plateau(14)

	if type_interface == 't':
		jeu_sans_ihm(joueur_rouge, joueur_bleu, plateau_jeu)
	else:
		interface_graphique = interface.Interface(plateau_jeu, 1000, joueur_rouge, joueur_bleu)
		interface_graphique.mainloop()

choix_jeu()


