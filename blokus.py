from mes_classes import IA
from mes_classes import joueur
from mes_classes import piece
from mes_classes import plateau
import regles
import definition_des_pieces


def jeu():
	"""Fonction qui déroule toute une partie."""
	joueur_rouge = joueur.Joueur(definition_des_pieces.pieces_rouge, "ROUGE", "HUMAIN")
	joueur_bleu = joueur.Joueur(definition_des_pieces.pieces_bleu, "BLEU", "MACHINE")
	plateau_jeu = plateau.Plateau(14)

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
			ret = regles.tour(plateau_jeu, joueur_rouge, numero_tour)
			plateau_jeu.afficher()

		# On verifie que le joueur rouge peut jouer
		if not regles.joueur_peut_jouer(plateau_jeu, joueur_bleu, numero_tour):
			joueur_bleu_peut_jouer = 0;
		# Au joueur bleu de jouer
		if  joueur_bleu_peut_jouer and ret != 'q':
			print("Au joueur bleu de jouer !")
			ret = regles.tour(plateau_jeu, joueur_bleu, numero_tour)
			plateau_jeu.afficher()

		# On augmente le numero du tour;
		numero_tour = numero_tour + 1

	regles.fin_partie(joueur_rouge, joueur_bleu)

jeu()
