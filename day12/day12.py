
import copy
import numpy as np
import statistics

class Cave:
	def __init__(self):
		self.small_caves = []
		self.big_caves = []
	
	def __str__(self):
		return ("Small: " + ' '.join(self.small_caves) + "\nBig: " + ' '.join(self.big_caves))

def det_lower(s):
	return all(c.islower() for c in s)

def visit_cave(cd, s_caves, curr_cave):
	print(curr_cave)
	print(s_caves)
	if det_lower(curr_cave):
		s_caves.remove(curr_cave)
	
	if curr_cave == 'end':
		return 1
		
	num = 0
	for c in cd[curr_cave].small_caves:
		if c in s_caves:
			num += visit_cave(cd, copy.copy(s_caves), c)
	
	for c in cd[curr_cave].big_caves:
		num += visit_cave(cd, copy.copy(s_caves), c)
	return num

def can_be_entered(s_caves, c):
	if s_caves[c] == 0:
		return True
	if s_caves[c] == 1:
		if c == 'start' or c == 'end':
			return False
		if all(i < 2 for i in list(s_caves.values())):
			return True
		else:
			return False
	else:
		return False

def visit_cave2(cd, s_caves, curr_cave):
	#print(curr_cave)
	#print(s_caves)
	if det_lower(curr_cave):
		s_caves[curr_cave] += 1
	
	if curr_cave == 'end':
		return 1
		
	num = 0
	for c in cd[curr_cave].small_caves:
		if can_be_entered(s_caves, c):
			num += visit_cave2(cd, copy.copy(s_caves), c)
	
	for c in cd[curr_cave].big_caves:
		num += visit_cave2(cd, copy.copy(s_caves), c)
	return num
	

def main1():
	lines = []
	#file = 'input'
	#file = 'input_test'
	#file = 'input_test2'
	#file = 'input_test3'
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	for l in lines:
		lines_s.append(l.strip()) 

	cd = {}
	s_caves = set()
	for l in lines_s:
		c1, c2 = l.split('-')
		c1 = c1.strip()
		c2 = c2.strip()
		cave = None
		
		#  c1 cave
		if c1 not in cd.keys():
			cave = Cave()
			cd[c1] = cave
		if det_lower(c2):
			cd[c1].small_caves.append(c2)
			s_caves.add(c2)
		else:
			cd[c1].big_caves.append(c2)
		
		#  c2 cave
		if c2 not in cd.keys():
			cave = Cave()
			cd[c2] = cave
		if det_lower(c1):
			cd[c2].small_caves.append(c1)
			s_caves.add(c1)
		else:
			cd[c2].big_caves.append(c1)
	
	#print(s_caves)
	#for s in cd.keys():
	#	print(s)
	#	print(cd[s])
	
	num = visit_cave(cd, s_caves, curr_cave="start")
	print(num)

def main2():
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

	cd = {}
	s_caves = {}
	for l in lines_s:
		c1, c2 = l.split('-')
		c1 = c1.strip()
		c2 = c2.strip()
		cave = None
		
		#  c1 cave
		if c1 not in cd.keys():
			cave = Cave()
			cd[c1] = cave
		if det_lower(c2):
			cd[c1].small_caves.append(c2)
			if c2 not in s_caves.keys():
				s_caves[c2] = 0
		else:
			cd[c1].big_caves.append(c2)
		
		#  c2 cave
		if c2 not in cd.keys():
			cave = Cave()
			cd[c2] = cave
		if det_lower(c1):
			cd[c2].small_caves.append(c1)
			if c1 not in s_caves.keys():
				s_caves[c1] = 0
		else:
			cd[c2].big_caves.append(c1)
	
	#print(s_caves)
	#for s in cd.keys():
	#	print(s)
	#	print(cd[s])
	
	print(list(s_caves.values()))
	num = visit_cave2(cd, s_caves, curr_cave="start")
	print(num)

if __name__ == '__main__':
	main2()