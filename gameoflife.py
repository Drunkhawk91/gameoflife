# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import ImageTk, ImageDraw, Image
import numpy as np


class Cell:
	
	def __init__(self, i, j, alive=False):
		self.i = i
		self.j = j
		self.alive = alive
		self.nbr_neigh = 0


class Board:

	def __init__(self, nbr_lin=10, nbr_col=10):
		self.nbr_lin = nbr_lin
		self.nbr_col = nbr_col
		self.matrix = np.zeros((self.nbr_lin, self.nbr_col))
		self.cells = []
		self.newcells = []
		for i in range(0, nbr_lin):
			tmp = []
			for j in range(0, nbr_col):
				tmp.append(Cell(i, j))
			self.cells.append(tmp)
			self.newcells.append(tmp)

	def countNeigh(self):
		for i in range(1, self.nbr_lin-1):
			for j in range(1, self.nbr_col-1):
				if self.cells[i-1][j-1].alive is True:
					self.cells[i][j].nbr_neigh += 1
				if self.cells[i-1][j].alive is True:
					self.cells[i][j].nbr_neigh += 1
				if self.cells[i-1][j+1].alive is True:
					self.cells[i][j].nbr_neigh += 1
				if self.cells[i][j-1].alive is True:
					self.cells[i][j].nbr_neigh += 1
				if self.cells[i][j+1].alive is True:
					self.cells[i][j].nbr_neigh += 1
				if self.cells[i+1][j-1].alive is True:
					self.cells[i][j].nbr_neigh += 1
				if self.cells[i+1][j].alive is True:
					self.cells[i][j].nbr_neigh += 1
				if self.cells[i+1][j+1].alive is True:
					self.cells[i][j].nbr_neigh += 1
	
	def nextStep(self):
		for i in range(1, self.nbr_lin-1):
			for j in range(1, self.nbr_col-1):
				# Overpopulation
				if self.cells[i][j].alive is True and self.cells[i][j].nbr_neigh > 3:
					self.newcells[i][j].alive = False
				# Stasis				
				if self.cells[i][j].alive is True and (self.cells[i][j].nbr_neigh == 2 or self.cells[i][j].nbr_neigh == 3):
					self.newcells[i][j].alive = True
				# Underpopulation
				if self.cells[i][j].alive is True and self.cells[i][j].nbr_neigh < 2:
					self.newcells[i][j].alive = False
				# Reproduction
				if self.cells[i][j].alive is not True and self.cells[i][j].nbr_neigh == 3:
					self.newcells[i][j].alive = True
		self.cells = self.newcells					


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


if __name__ == "__main__":

	board = Board(10, 10)
	board.cells[4][3].alive = True
	board.cells[4][4].alive = True
	board.cells[4][5].alive = True
	createImage(board)

	fenetre = Tk()

	img = ImageTk.PhotoImage(Image.open("image.png"))
	panel = Label(fenetre, image = img)
	panel.pack(side="bottom", fill="both", expand="yes")


	def clickNextStep(board):
		board.nextStep()
		createImage(board)

	button_nextStep = Button(fenetre, text=">>", command=clickNextStep(board))
	button_nextStep.pack()

	fenetre.mainloop()
