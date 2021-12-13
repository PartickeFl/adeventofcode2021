
import copy
import numpy as np
import statistics

def copy_rows(row1, row2):
	n_r = np.chararray(row1.shape)
	n_r[:] = '.'
	for r in range(row1.size):
		if row1[r] == b'#' or row2[r] == b'#':
			n_r[r] = b'#'
	return n_r

def main1():
	lines = []
	file = 'input'
	#file = 'input_test'
	#file = 'input_test2'
	#file = 'input_test3'
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	fold = []
	dots = []
	max_p1 = -1
	max_p2 = -1
	for l in lines:
		l = l.strip()
		if 'fold along' in l:
			p1,p2 = l.split('=')
			if 'y' in p1:
				fold.append(['y', int(p2.strip())])
			if 'x' in p1:
				fold.append(['x', int(p2.strip())])
		if ',' in l:
			p1,p2 = l.split(',')
			p1 = int(p1.strip())
			p2 = int(p2.strip())
			dots.append([p1,p2])
			if p1 > max_p1:
				max_p1 = p1
			if p2 > max_p2:
				max_p2 = p2
	
	#  Set #
	charar = np.chararray((max_p2+1, max_p1+1))
	charar[:] = b'.'
	for e in dots:
		charar[e[1], e[0]] = b'#'
	print(charar)
	

	#c3 = copy_rows(c1, c2)
	#  Fold x,y
	old_charar = copy.copy(charar)
	new_charar = None
	for f in fold:
		if f[0] == 'y': # up
			new_charar = np.chararray((f[1], old_charar.shape[1]))
			new_charar[:] = '.'
			c_up = copy.copy(f[1])
			c_down = copy.copy(f[1])
			c_down-=1
			c_up+=1
			while c_up < max_p2+1 and c_down >= 0:
				new_charar[c_down, :] = copy_rows(old_charar[c_down, :], old_charar[c_up, :])
				c_down-=1
				c_up+=1
		if f[0] == 'x': # up
			new_charar = np.chararray((old_charar.shape[0], f[1]))
			new_charar[:] = '.'
			c_up = copy.copy(f[1])
			c_down = copy.copy(f[1])
			c_down-=1
			c_up+=1
			while c_up < max_p1+1 and c_down >= 0:
				new_charar[:, c_down] = copy_rows(old_charar[:, c_down], old_charar[:, c_up])
				c_down-=1
				c_up+=1
		old_charar = copy.copy(new_charar)
		print(new_charar)
		#break
	
	s = 0
	for x in np.nditer(new_charar):
		if x == b'#':
			s+=1
	print(s)
	
	x, y = new_charar.shape
	s = ''
	for c1 in range(x):
		for c2 in range(y):
			s+= new_charar[c1, c2].decode("utf-8")
		s+='\n'
	print(s)
	

if __name__ == '__main__':
	main1()