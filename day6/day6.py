
import copy
import numpy as np

def main1():
	lines = []
	file = 'input'
	#file = 'input_test'
	with open(file) as f:
		lines = f.readlines()
	
	f_inp = lines[0].strip().split(',')
	f_inp_new = []
	for i in f_inp:
		f_inp_new.append(int(i))
	f_inp = copy.copy(f_inp_new)

	calc_dict = {}
	row_dict = {}
	for num in range(0,9):
		print(num)
		inp = [num]
		for day in range(128):
			inp_new = []
			for i in inp:
				if i == 0:
					inp_new.append(6)
					inp_new.append(8)
				else:
					i -= 1
					inp_new.append(i)
			inp = copy.copy(inp_new)
		print(len(inp))
		calc_dict[num] = len(inp)
		row_dict[num] = inp
	
	s = 0
	for f in f_inp:
		for e in row_dict[f]:
			s += calc_dict[e]
	print(s)
	
if __name__ == '__main__':
	main1()