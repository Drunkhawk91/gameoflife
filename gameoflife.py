# -*- coding: utf-8 -*-
import os, sys
import numpy as np
import matplotlib.pyplot as plt
from init import initBoard
from trace import trace


# Parameters
nbr_lin = 50
nbr_col = 50
steps   = 1000
rules   = 'simple'


if __name__ == "__main__":

	board = initBoard(nbr_lin, nbr_col)		
	trace(board, steps)