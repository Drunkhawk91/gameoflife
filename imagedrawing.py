# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw


def createImage(board):
	
	px = 10*board.nbr_lin
	py = 10*board.nbr_col
	size_x = px/board.nbr_lin
	size_y = py/board.nbr_col

	image = Image.new('RGBA', (px, py), (255, 255, 255, 0))
	draw = ImageDraw.Draw(image)

	for i in range(1, board.nbr_lin-1):
		for j in range(1, board.nbr_col-1):
			if board.cells[i][j].alive is True:
				draw.rectangle(((size_x*i-5, size_y*j-5),(size_x*i+5, size_y*j+5)), fill="black")

	image.save('image.png')	
