from mes_classes import arbre
from mes_classes import joueur
from mes_classes import plateau
from mes_classes import piece
import definition_des_pieces
import regles

j1 = joueur.Joueur(definition_des_pieces.pieces_rouge, "ROUGE", "HUMAIN")
j2 = joueur.Joueur(definition_des_pieces.pieces_bleu, "BLEU", "HUMAIN")

p = plateau.Plateau(14)

a = arbre.Arbre(j1, j2, p, "DETERMINISTE", 5, 15)

valeur = a.evaluation_arbre(2, 0)

a.afficher()


print(valeur)
print(a.noeud_racine.indice_piece)
print(a.noeud_racine.rotation)
print(a.noeud_racine.x)
print(a.noeud_racine.y)