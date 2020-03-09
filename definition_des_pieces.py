from mes_classes import piece

pieces_rouge = []
pieces_bleu = []

pieces_rouge.append(piece.Piece(1, "ROUGE"))
pieces_rouge.append(piece.Piece(2, "ROUGE"))
pieces_rouge.append(piece.Piece(2, "ROUGE"))
pieces_rouge.append(piece.Piece(2, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(3, "ROUGE"))
pieces_rouge.append(piece.Piece(4, "ROUGE"))
pieces_rouge.append(piece.Piece(4, "ROUGE"))
pieces_rouge.append(piece.Piece(4, "ROUGE"))
pieces_rouge.append(piece.Piece(4, "ROUGE"))
pieces_rouge.append(piece.Piece(5, "ROUGE"))

pieces_bleu.append(piece.Piece(1, "BLEU"))
pieces_bleu.append(piece.Piece(2, "BLEU"))
pieces_bleu.append(piece.Piece(2, "BLEU"))
pieces_bleu.append(piece.Piece(2, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(3, "BLEU"))
pieces_bleu.append(piece.Piece(4, "BLEU"))
pieces_bleu.append(piece.Piece(4, "BLEU"))
pieces_bleu.append(piece.Piece(4, "BLEU"))
pieces_bleu.append(piece.Piece(4, "BLEU"))
pieces_bleu.append(piece.Piece(5, "BLEU"))


pieces_rouge[0].forme = [[1]]
pieces_rouge[0].afficher()
pieces_rouge[1].forme = [[1, 1], [0, 0]]
pieces_rouge[1].afficher()
pieces_rouge[2].forme = [[1, 1], [1, 0]]
pieces_rouge[2].afficher()
pieces_rouge[3].forme = [[1, 1], [1, 1]]
pieces_rouge[3].afficher()
pieces_rouge[4].forme = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
pieces_rouge[4].afficher()
pieces_rouge[5].forme = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]
pieces_rouge[5].afficher()
pieces_rouge[6].forme = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
pieces_rouge[6].afficher()
pieces_rouge[7].forme = [[0, 1, 0], [1, 1, 0], [1, 0, 0]]
pieces_rouge[7].afficher()
pieces_rouge[8].forme = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]
pieces_rouge[8].afficher()
pieces_rouge[9].forme = [[1, 0, 1], [1, 1, 1], [0, 0, 0]]
pieces_rouge[9].afficher()
pieces_rouge[10].forme = [[1, 0, 0], [1, 1, 1], [1, 0, 0]]
pieces_rouge[10].afficher()
pieces_rouge[11].forme = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
pieces_rouge[11].afficher()
pieces_rouge[12].forme = [[0, 0, 1], [0, 1, 1], [1, 1, 0]]
pieces_rouge[12].afficher()
pieces_rouge[13].forme = [[0, 1, 1], [0, 1, 0], [1, 1, 0]]
pieces_rouge[13].afficher()
pieces_rouge[14].forme = [[0, 1, 1], [1, 1, 0], [0, 1, 0]]
pieces_rouge[14].afficher()
pieces_rouge[15].forme = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
pieces_rouge[15].afficher()
pieces_rouge[16].forme = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
pieces_rouge[16].afficher()
pieces_rouge[17].forme = [[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
pieces_rouge[17].afficher()
pieces_rouge[18].forme = [[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
pieces_rouge[18].afficher()
pieces_rouge[19].forme = [[1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
pieces_rouge[19].afficher()
pieces_rouge[20].forme = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
pieces_rouge[20].afficher()


pieces_bleu[0].forme = [[1]]
pieces_bleu[0].afficher()
pieces_bleu[1].forme = [[1, 1], [0, 0]]
pieces_bleu[1].afficher()
pieces_bleu[2].forme = [[1, 1], [1, 0]]
pieces_bleu[2].afficher()
pieces_bleu[3].forme = [[1, 1], [1, 1]]
pieces_bleu[3].afficher()
pieces_bleu[4].forme = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
pieces_bleu[4].afficher()
pieces_bleu[5].forme = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]
pieces_bleu[5].afficher()
pieces_bleu[6].forme = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
pieces_bleu[6].afficher()
pieces_bleu[7].forme = [[0, 1, 0], [1, 1, 0], [1, 0, 0]]
pieces_bleu[7].afficher()
pieces_bleu[8].forme = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]
pieces_bleu[8].afficher()
pieces_bleu[9].forme = [[1, 0, 1], [1, 1, 1], [0, 0, 0]]
pieces_bleu[9].afficher()
pieces_bleu[10].forme = [[1, 0, 0], [1, 1, 1], [1, 0, 0]]
pieces_bleu[10].afficher()
pieces_bleu[11].forme = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
pieces_bleu[11].afficher()
pieces_bleu[12].forme = [[0, 0, 1], [0, 1, 1], [1, 1, 0]]
pieces_bleu[12].afficher()
pieces_bleu[13].forme = [[0, 1, 1], [0, 1, 0], [1, 1, 0]]
pieces_bleu[13].afficher()
pieces_bleu[14].forme = [[0, 1, 1], [1, 1, 0], [0, 1, 0]]
pieces_bleu[14].afficher()
pieces_bleu[15].forme = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
pieces_bleu[15].afficher()
pieces_bleu[16].forme = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
pieces_bleu[16].afficher()
pieces_bleu[17].forme = [[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
pieces_bleu[17].afficher()
pieces_bleu[18].forme = [[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
pieces_bleu[18].afficher()
pieces_bleu[19].forme = [[1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
pieces_bleu[19].afficher()
pieces_bleu[20].forme = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
pieces_bleu[20].afficher()