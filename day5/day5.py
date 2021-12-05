
import copy
import numpy as np

def main1():
	lines = []
	file = 'input'
	#file = 'input_test'
	with open(file) as f:
		lines = f.readlines()
	
	v_l  = []
	h_l =  []
	d_l = []
	max_x = -1
	max_y = -1
	for l in lines:
		vec1, vec2 = l.split('->')
		vec1 = vec1.strip()
		vec2 = vec2.strip()
		x1, y1 = vec1.split(',')
		x2, y2 = vec2.split(',')
		x1 = int(x1.strip())
		x2 = int(x2.strip())
		y1 = int(y1.strip())
		y2 = int(y2.strip())
		if x1 > max_x:
			max_x = x1
		if x2 > max_x:
			max_x = x2
		if y1 > max_y:
			max_y = y1
		if y2 > max_y:
			max_y = y2
		
		# Vert line
		yList = []
		xList = []
		if x1 == x2:
			if y1 > y2:
				yList = list(range(y2, y1+1))
			elif y2 > y1:
				yList = list(range(y1, y2+1))
			else:
				yList = [x1, y1]
			for y in yList:
				vec = [x1, y]
				v_l.append(vec)
		# Horz line
		elif y1 == y2:
			if x1 > x2:
				xList = list(range(x2, x1+1))
			elif x1 < x2:
				xList = list(range(x1, x2+1))
			for x in xList:
				vec = [x, y1]
				h_l.append(vec)
		# Diag line
		else:
			if x1 < x2:
				xList = list(range(x1, x2+1))
			else:
				xList = list(range(x1, x2-1, -1))
			if y1 < y2:
				yList = list(range(y1, y2+1))
			else:
				yList = list(range(y1, y2-1, -1))
			for x,y in zip(xList, yList):
				d_l.append([x,y])
	
	mask = np.zeros((max_x+1, max_y+1), dtype=int)
	for v in v_l:
		mask[v[0], v[1]] += 1
	for h in h_l:
		mask[h[0], h[1]] += 1
	for d in d_l:
		mask[d[0], d[1]] += 1
	
	n_p = 0
	size_x, size_y = mask.shape
	for e in range(size_x):
		for d in range(size_y):
			if mask[e,d] >= 2:
				n_p += 1
	print(n_p)
	
if __name__ == '__main__':
	main1()