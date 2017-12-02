# -*- coding: utf-8 -*-
import numpy as np
import wx
from ihm import MyFrame1


def boolean2binary(val):
	if val is True:
		out = 1
	else:
		out = 0
	return out


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


class MaFrame(MyFrame1):

	def __init__(self, parent):
		MyFrame1.__init__(self, parent)


class App(wx.App):

	def __init__(self, parent):
		wx.App.__init__(self,parent)

	def OnInit(self):
		frame = MaFrame(None)
		self.SetTopWindow(frame)
		frame.Show(True)
		return True	


if __name__ == "__main__":

	# Initialization
	board = Board(10,10)
	board.cells[4][3].alive = True
	board.cells[4][4].alive = True
	board.cells[4][5].alive = True

	# Matrix
	matrix = []
	for i in range(0, board.nbr_lin):
		tmp = []
		for j in range(0, board.nbr_col):
			tmp.append(boolean2binary(board.cells[i][j].alive))
		matrix.append(tmp)
	print(matrix)

	# Wx show
	app = App(0)
	app.MainLoop()
