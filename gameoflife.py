# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


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

	def vectAlive(self):
		vect_i = [] 
		vect_j = []
		for i in range(1, self.nbr_lin-1):
			for j in range(1, self.nbr_col-1):
				if self.cells[i][j].alive is True:
					vect_i.append(i+1)
					vect_j.append(j+1)
				else:
					pass
		return vect_i, vect_j	
	

if __name__ == "__main__":

	# Init
	board = Board(10, 10)
	board.cells[board.nbr_lin/2-1][board.nbr_col/2-2].alive = True
	board.cells[board.nbr_lin/2-1][board.nbr_col/2-1].alive = True
	board.cells[board.nbr_lin/2-1][board.nbr_col/2].alive = True
	
	# Steps and animation
	fig = plt.figure()
	line, = plt.plot([], [], marker='s', markersize=board.nbr_lin, color='black', linewidth=0) 
	plt.xlim(0, board.nbr_lin)
	plt.ylim(0, board.nbr_col)
	plt.xticks(np.arange(.5, board.nbr_lin+.5, 1.0), size=0)
	plt.yticks(np.arange(.5, board.nbr_col+.5, 1.0), size=0)
	plt.grid(True)
	plt.axes().set_aspect('equal', 'datalim')

	def init():
		line.set_data([], [])
		return line,

	def animate(i):
		board.countNeigh()
		board.nextStep()
		x, y = board.vectAlive()
		line.set_data(x, y)
		return line,
 
	ani = FuncAnimation(fig, animate, init_func=init, frames=10, blit=True, interval=1000, repeat=False)

	plt.show()
