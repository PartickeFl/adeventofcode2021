
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
	#file = 'input'
	#NCN
	#NBCCN
	file = 'input_test'
	#file = 'input_test2'
	#file = 'input_test3'
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	for l in lines:
		lines_s.append(l.strip()) 
	
	s = ''
	c = 0
	d = {}
	for l in lines_s:
		if c == 0:
			s = l
		elif c == 1:
			pass
		else:
			p1, p2 = l.split('->')
			p1 = p1.strip()
			p2 = p2.strip()
			p3 = p1[0] + p2 + p1[1]
			d[p1] = p3
		c+=1
	
	steps = 10
	char_list = []
	for ns in range(steps):
		final_s = ''
		for idx in range(len(s)):
			if idx >= len(s)-1:
				break
			s2 = s[idx] + s[idx+1]
			if final_s == '':
				final_s += d[s2]
			else:
				final_s = final_s[:-1] + d[s2]
		s = copy.copy(final_s)
		if ns == 0:
			for c in s:
				if c not in char_list:
					char_list.append(c)
		print(ns+1)
		print(s)
	
	print(char_list)
	#print(final_s)
	num_list = []
	for c in char_list:
		num_list.append(final_s.count(c))
	print(num_list)
	print(max(num_list) - min(num_list))

def call_rec(d2, d3, c, arr):
	

def main2():
	lines = []
	#file = 'input'
	#NCN
	#NBCCN
	file = 'input_test'
	#file = 'input_test2'
	#file = 'input_test3'
	#char_list = ['K', 'H', 'F', 'B', 'V', 'O', 'S', 'N', 'P', 'C']
	char_list = ['N', 'B', 'C', 'H']
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	for l in lines:
		lines_s.append(l.strip()) 
	
	s = ''
	c = 0
	d = {}
	for l in lines_s:
		if c == 0:
			s = l
		elif c == 1:
			pass
		else:
			p1, p2 = l.split('->')
			p1 = p1.strip()
			p2 = p2.strip()
			p3 = p1[0] + p2 + p1[1]
			d[p1] = p3
		c+=1
	
	num_d = {}
	sub_ranges = []
	for idx in range(len(s)):
		if idx >= len(s)-1:
			break
		s2 = s[idx] + s[idx+1]
		sub_ranges.append(s2)
	
	d2 = {}
	for s_up in sub_ranges:
		print(s_up)
		if s_up not in d2.keys():
			steps = 10
			s = copy.copy(s_up)
			for ns in range(steps):
				final_s = ''
				for idx in range(len(s)):
					if idx >= len(s)-1:
						break
					s2 = s[idx] + s[idx+1]
					if final_s == '':
						final_s += d[s2]
					else:
						final_s = final_s[:-1] + d[s2]
				s = copy.copy(final_s)
				print(ns+1)
				print(s)
			d2[s_up] = s

	d3 = {}
	first = True
	for s_up in d2.keys():
		s = d2[s_up]
		d3[s_up] = []
		for c in char_list:
			num = s.count(c)
			#if c == s_up[0] and not first:
			#	num -= 1
			d3[s_up].append(num)
		first = False
	
	print(d3)
	arr = np.zeros((len(char_list), 1))
	for key in d3.keys():
		for i in range(len(char_list)):
			arr[i] += d3[key][i]
	print(arr)
	
	#print(char_list)
	#print(final_s)
	#num_list = []
	#for c in char_list:
	#num_list.append(final_s.count(c))
	#print(num_list)
	#print(max(num_list) - min(num_list))
	#865, 298, 1749, 161

if __name__ == '__main__':
	main2()