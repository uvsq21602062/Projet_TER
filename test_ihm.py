from mes_classes import interface
from mes_classes import plateau
from mes_classes import piece
from mes_classes import joueur
import definition_des_pieces
import regles


plateau = plateau.Plateau(14)
interface = interface.Interface(plateau, 1000,\
	joueur.Joueur(definition_des_pieces.pieces_rouge, "ROUGE", "HUMAIN"),\
	joueur.Joueur(definition_des_pieces.pieces_bleu, "BLEU", "HUMAIN"))
interface.mainloop()

