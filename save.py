# -*- coding: utf-8 -*-
import os, sys
import pickle


os.chdir('data')


def saveState(board, step):
	
	with open('state{}.dat'.format(step), 'wb') as state:
		pickler = pickle.Pickler(state)
		pickler.dump(board)
		#state.write('State #{}/n'.format(step))

	with open('stateRLE{}.rle'.format(step), 'w') as stateRLE:
		stateRLE.write('#N') #...	
