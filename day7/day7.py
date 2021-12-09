
import copy
import numpy as np
import statistics

def calc_dist(m, f_inp):
	s = 0
	for i in f_inp:
		d = int(abs(i-m))
		t = (d * (d-1) / 2) + d
		s += int(t)
	return s

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

	m = statistics.median(f_inp)
	m = int(m)
	min_dist = calc_dist(m, f_inp)
	
	m_search = copy.copy(m)
	m_up = copy.copy(m)
	while True:
		m_up += 1
		dist = calc_dist(m_up, f_inp)
		if dist > min_dist:
			break
		else:
			min_dist = dist
			m_search = m_up
	
	m_down = copy.copy(m)
	while True:
		m_down -= 1
		dist = calc_dist(m_down, f_inp)
		if dist > min_dist:
			break
		else:
			min_dist = dist
			m_search = m_down
	
	print(m_search)
	print(min_dist)
	
if __name__ == '__main__':
	main1()