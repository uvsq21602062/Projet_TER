from mes_classes import piece

pieces_rouge = []
pieces_bleu = []

pieces_rouge.append(piece.Piece(1, "ROUGE", 0))
pieces_rouge.append(piece.Piece(2, "ROUGE", 1))
pieces_rouge.append(piece.Piece(2, "ROUGE", 2))
pieces_rouge.append(piece.Piece(2, "ROUGE", 3))
pieces_rouge.append(piece.Piece(3, "ROUGE", 4))
pieces_rouge.append(piece.Piece(3, "ROUGE", 5))
pieces_rouge.append(piece.Piece(3, "ROUGE", 6))
pieces_rouge.append(piece.Piece(3, "ROUGE", 7))
pieces_rouge.append(piece.Piece(3, "ROUGE", 8))
pieces_rouge.append(piece.Piece(3, "ROUGE", 9))
pieces_rouge.append(piece.Piece(3, "ROUGE", 10))
pieces_rouge.append(piece.Piece(3, "ROUGE", 11))
pieces_rouge.append(piece.Piece(3, "ROUGE", 12))
pieces_rouge.append(piece.Piece(3, "ROUGE", 13))
pieces_rouge.append(piece.Piece(3, "ROUGE", 14))
pieces_rouge.append(piece.Piece(3, "ROUGE", 15))
pieces_rouge.append(piece.Piece(4, "ROUGE", 16))
pieces_rouge.append(piece.Piece(4, "ROUGE", 17))
pieces_rouge.append(piece.Piece(4, "ROUGE", 18))
pieces_rouge.append(piece.Piece(4, "ROUGE", 19))
pieces_rouge.append(piece.Piece(5, "ROUGE", 20))

pieces_bleu.append(piece.Piece(1, "BLEU", 0))
pieces_bleu.append(piece.Piece(2, "BLEU", 1))
pieces_bleu.append(piece.Piece(2, "BLEU", 2))
pieces_bleu.append(piece.Piece(2, "BLEU", 3))
pieces_bleu.append(piece.Piece(3, "BLEU", 4))
pieces_bleu.append(piece.Piece(3, "BLEU", 5))
pieces_bleu.append(piece.Piece(3, "BLEU", 6))
pieces_bleu.append(piece.Piece(3, "BLEU", 7))
pieces_bleu.append(piece.Piece(3, "BLEU", 8))
pieces_bleu.append(piece.Piece(3, "BLEU", 9))
pieces_bleu.append(piece.Piece(3, "BLEU", 10))
pieces_bleu.append(piece.Piece(3, "BLEU", 11))
pieces_bleu.append(piece.Piece(3, "BLEU", 12))
pieces_bleu.append(piece.Piece(3, "BLEU", 13))
pieces_bleu.append(piece.Piece(3, "BLEU", 14))
pieces_bleu.append(piece.Piece(3, "BLEU", 15))
pieces_bleu.append(piece.Piece(4, "BLEU", 16))
pieces_bleu.append(piece.Piece(4, "BLEU", 17))
pieces_bleu.append(piece.Piece(4, "BLEU", 18))
pieces_bleu.append(piece.Piece(4, "BLEU", 19))
pieces_bleu.append(piece.Piece(5, "BLEU", 20))

pieces_rouge[0].forme = [[1]]								# 0
pieces_rouge[1].forme = [[1, 1], [0, 0]]					# 1
pieces_rouge[2].forme = [[1, 1], [1, 0]]					# 2
pieces_rouge[3].forme = [[1, 1], [1, 1]]					# 3
pieces_rouge[4].forme = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]	# 4
pieces_rouge[5].forme = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]	# 5
pieces_rouge[6].forme = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]	# 6
pieces_rouge[7].forme = [[1, 0, 0], [1, 1, 0], [0, 1, 0]]	# 7
pieces_rouge[8].forme = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]	# 8
pieces_rouge[9].forme = [[1, 0, 1], [1, 1, 1], [0, 0, 0]]	# 9
pieces_rouge[10].forme = [[1, 0, 0], [1, 1, 1], [1, 0, 0]]	# 10
pieces_rouge[11].forme = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]	# 11
pieces_rouge[12].forme = [[0, 0, 1], [0, 1, 1], [1, 1, 0]]	# 12
pieces_rouge[13].forme = [[0, 1, 1], [0, 1, 0], [1, 1, 0]]	# 13
pieces_rouge[14].forme = [[0, 1, 1], [1, 1, 0], [0, 1, 0]]	# 14
pieces_rouge[15].forme = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]	# 15
pieces_rouge[16].forme = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]	#16  # changer l'ordre
pieces_rouge[17].forme = [[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]	#17
pieces_rouge[18].forme = [[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]	#18
pieces_rouge[19].forme = [[1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]	#19
pieces_rouge[20].forme = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]	#20


pieces_bleu[0].forme = [[1]]								# 0
pieces_bleu[1].forme = [[1, 1], [0, 0]]					# 1
pieces_bleu[2].forme = [[1, 1], [1, 0]]					# 2
pieces_bleu[3].forme = [[1, 1], [1, 1]]					# 3
pieces_bleu[4].forme = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]	# 4
pieces_bleu[5].forme = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]	# 5
pieces_bleu[6].forme = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]	# 6
pieces_bleu[7].forme = [[1, 0, 0], [1, 1, 0], [0, 1, 0]]	# 7
pieces_bleu[8].forme = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]	# 8
pieces_bleu[9].forme = [[1, 0, 1], [1, 1, 1], [0, 0, 0]]	# 9
pieces_bleu[10].forme = [[1, 0, 0], [1, 1, 1], [1, 0, 0]]	# 10
pieces_bleu[11].forme = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]	# 11
pieces_bleu[12].forme = [[0, 0, 1], [0, 1, 1], [1, 1, 0]]	# 12
pieces_bleu[13].forme = [[0, 1, 1], [0, 1, 0], [1, 1, 0]]	# 13
pieces_bleu[14].forme = [[0, 1, 1], [1, 1, 0], [0, 1, 0]]	# 14
pieces_bleu[15].forme = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]	# 15
pieces_bleu[16].forme = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]	#16  # changer l'ordre
pieces_bleu[17].forme = [[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]	#17
pieces_bleu[18].forme = [[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]	#18
pieces_bleu[19].forme = [[1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]	#19
pieces_bleu[20].forme = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]	#20
