# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from save import saveState

def trace(board, steps):
	fig = plt.figure()
	line, = plt.plot([], [], marker='s', markersize=5, color='black', linewidth=0) 
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
		#saveState(board, i)
		x, y = board.vectAlive()
		line.set_data(x, y)
		return line,
 
	ani = FuncAnimation(fig, animate, init_func=init, frames=steps, blit=True, interval=100, repeat=False)

	plt.show()
