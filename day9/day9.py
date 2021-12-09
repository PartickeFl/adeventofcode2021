
import copy
import numpy as np
import statistics


def main1():
	lines = []
	file = 'input'
	#file = 'input_test'
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	for l in lines:
		lines_s.append(l.strip()) 

	r_len = len(lines_s)
	c_len = len(lines_s[0])
	m_arr = np.zeros((r_len,c_len), dtype=int)
	for r in range(r_len):
		for c in range(c_len):
			m_arr[r, c] = int(lines_s[r][c])
	
	risk = 0
	possib_basins = []
	for r in range(r_len):
		for c in range(c_len):
			v_min = True
			n_min = m_arr[r,c]
			if r-1 >= 0:
				if m_arr[r-1, c] <= n_min:
					v_min = False
			if r+1 < r_len:
				if m_arr[r+1, c] <= n_min:
					v_min = False
			if c-1 >= 0:
				if m_arr[r, c-1] <= n_min:
					v_min = False
			if c+1 < c_len:
				if m_arr[r, c+1] <= n_min:
					v_min = False
			if v_min:
				risk += n_min + 1
				possib_basins.append([r,c])

	return possib_basins, m_arr, r_len, c_len

def main2(possib_basins, m_arr, r_len, c_len):

	all_basins = []
	while len(possib_basins) > 0:
		p = possib_basins[0]
		r = p[0]
		c = p[1]
		possib_basins.remove(p)

		this_basin = []
		possib_this_basin = []
		while True:

			#  Look down
			r_old = copy.copy(r)
			c_old = copy.copy(c)
			while True:
				r += 1
				if r >= r_len:
					break
				if m_arr[r,c] == 9:
					break
				else:
					if [r,c] not in this_basin:
						this_basin.append([r,c])
						possib_this_basin.append([r,c])
					if [r,c] in possib_basins:
						possib_basins.remove([r,c])

			#  Look up
			r = copy.copy(r_old)
			c = copy.copy(c_old)
			while True:
				r -= 1
				if r < 0:
					break
				if m_arr[r,c] == 9:
					break
				else:
					if [r,c] not in this_basin:
						this_basin.append([r,c])
						possib_this_basin.append([r,c])
					if [r,c] in possib_basins:
						possib_basins.remove([r,c])
			
			#  Look right
			r = copy.copy(r_old)
			c = copy.copy(c_old)
			while True:
				c += 1
				if c >= c_len:
					break
				if m_arr[r,c] == 9:
					break
				else:
					if [r,c] not in this_basin:
						this_basin.append([r,c])
						possib_this_basin.append([r,c])
					if [r,c] in possib_basins:
						possib_basins.remove([r,c])

			#  Look left
			r = copy.copy(r_old)
			c = copy.copy(c_old)
			while True:
				c -= 1
				if c < 0:
					break
				if m_arr[r,c] == 9:
					break
				else:
					if [r,c] not in this_basin:
						this_basin.append([r,c])
						possib_this_basin.append([r,c])
					if [r,c] in possib_basins:
						possib_basins.remove([r,c])

			if len(possib_this_basin) == 0:
				break
			
			r = possib_this_basin[0][0]
			c = possib_this_basin[0][1]
			possib_this_basin.remove([r,c])

		all_basins.append(this_basin)
	
	x = []
	for basin in all_basins:
		x.append(len(basin))
	x.sort(reverse=True)
	y = x[0:3]
	mult = 1
	for z in y:
		mult *= z
	print(mult)

if __name__ == '__main__':
	possib_basins, m_arr, r_len, c_len = main1()
	main2(possib_basins, m_arr, r_len, c_len)