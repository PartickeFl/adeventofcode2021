
import copy
import numpy as np
import statistics


def main1():
	lines = []
	file = 'input'
	#file = 'input_test'
	#file = 'input_test2'
	#file = 'input_test3'
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	for l in lines:
		lines_s.append(l.strip()) 

	r_len = 10
	c_len = 10
	m_arr = np.zeros((r_len,c_len), dtype=int)
	for r in range(r_len):
		for c in range(c_len):
			m_arr[r, c] = int(lines_s[r][c])
	print(m_arr)
	
	num_flashes = 0
	steps = 1000
	for s in range(steps):
		
		# Increase by 1
		for r in range(r_len):
			for c in range(c_len):
				m_arr[r, c] += 1
		
		#print(m_arr)
		#  Flash all
		f_list = []
		while True:
			flashed = False
			for r in range(r_len):
				for c in range(c_len):
					if m_arr[r, c] > 9 and [r,c] not in f_list:
						flashed = True
						if r-1 >= 0:
							if c-1 >= 0:
								m_arr[r-1, c-1] += 1
							if c+1 < c_len:
								m_arr[r-1, c+1] += 1
							m_arr[r-1, c] += 1
						if r+1 < r_len:
							if c-1 >= 0:
								m_arr[r+1, c-1] += 1
							if c+1 < c_len:
								m_arr[r+1, c+1] += 1
							m_arr[r+1, c] += 1
						if c-1 >= 0:
							m_arr[r, c-1] += 1
						if c+1 < c_len:
							m_arr[r, c+1] += 1
						
						f_list.append([r,c])
			if not flashed:
				break
		
		#  Set all > 9 to zero
		num_temp = 0
		for r in range(r_len):
			for c in range(c_len):
				if m_arr[r, c] > 9:
					m_arr[r, c] = 0
					num_flashes += 1
					num_temp += 1
		if num_temp == r_len * c_len:
			print(s+1)
			break
	
	print(m_arr)
	print(num_flashes)

if __name__ == '__main__':
	main1()