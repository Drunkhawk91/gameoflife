# -*- coding: utf-8 -*-
from rules import Board
import random


def initBoard(nbr_lin, nbr_col):
	board = Board(nbr_lin, nbr_col)
	
	# Random init
	for i in range(0, board.nbr_lin-1):
		for j in range(0, board.nbr_col-1):
			board.cells[i][j].alive = bool(random.getrandbits(1)) 	

	board.countNeigh()
	x,y = board.vectAlive()

	return board
