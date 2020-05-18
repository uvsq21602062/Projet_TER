from mes_classes import arbre
from mes_classes import joueur
from mes_classes import plateau
from mes_classes import piece
import definition_des_pieces
import regles

j1 = joueur.Joueur(definition_des_pieces.pieces_rouge, "ROUGE", "HUMAIN")
j2 = joueur.Joueur(definition_des_pieces.pieces_bleu, "BLEU", "HUMAIN")

p = plateau.Plateau(14)

a = arbre.Arbre(1, j1, j2, p, 0)

a.construction_racine()

a.numero_tour += 1

a.nouvel_etage(a.noeud_racine, a.plateau, a.joueur)

a.nouvel_etage(a.noeud_racine, a.plateau, a.joueur)

a.afficher(a.noeud_racine, a.joueur)