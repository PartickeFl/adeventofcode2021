
import copy
import numpy as np
import statistics


def main1():
	lines = []
	#file = 'input'
	file = 'input_test'
	with open(file) as f:
		lines = f.readlines()

	num = 0
	n_d = {1: 2, 4: 4, 7: 3, 8: 7}
	for l in lines:
		p1, p2 = l.split('|')
		p1 = p1.strip()
		p2 = p2.strip()
		
		dig = p2.split(' ')
		for d in dig:
			d = d.strip()
			if len(d) in n_d.values():
				num += 1
	print(num)

def main2():
	lines = []
	file = 'input'
	#file = 'input_test'
	#file = 'input_test2'
	with open(file) as f:
		lines = f.readlines()

	num = 0
	for l in lines:
		n_d = {}
		p1, p2 = l.split('|')
		p1 = p1.strip()
		p2 = p2.strip()
		
		p1_l = p1.split(' ')
		p2_l = p2.split(' ')
		
		# Find 1,4,7,8
		for e in p1_l:
			e2 = set(e)
			if len(e2) == 2:
				n_d[1] = e2
			elif len(e) == 3:
				n_d[7] = e2
			elif len(e) == 4:
				n_d[4] = e2
			elif len(e) == 7:
				n_d[8] = e2
		
		# Find 6, 9
		for e in p1_l:
			e2 = set(e)
			if len(e2) == 6:
				if n_d[4].issubset(e2):
					n_d[9] = e2
				elif n_d[1].issubset(e2):
					n_d[0] = e2
				else:
					n_d[6] = e2
		
		# Find 2, 3, 5
		for e in p1_l:
			e2 = set(e)
			if len(e) == 5:
				if n_d[1].issubset(e2):
					n_d[3] = e2
				elif (n_d[6].intersection(n_d[1])).issubset(e2):
					n_d[5] = e2
				else:
					n_d[2] = e2
		
		#  Calculate stuff
		s = ''
		for e in p2_l:
			e2 = set(e)
			for key in n_d.keys():
				if n_d[key] == e2:
					s += str(key)
		print(int(s))
		print(n_d)
		num += int(s)
	
	print(num)
	
if __name__ == '__main__':
	main2()