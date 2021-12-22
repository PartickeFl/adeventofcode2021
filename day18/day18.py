import copy
import numpy as np
import math
import statistics
from collections import defaultdict
from enum import Enum
import string
import random
 
import sys

from bitstring import BitArray, BitStream

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

class Snailfish:
	def __init__(self):
		self.left = None
		self.right = None
		self.parent = None
		self.name = id_generator()
		#self.layer = layer
	def __str__(self):
		#return(self.name + "[" + str(self.left) + "," + str(self.right) + "]")
		s = self.name
		#if self.parent:
		#	s2 = self.parent.name
		#else:
		#	s2 = "None"
		#return(s + '||' + s2 + "[" + str(self.left) + "," + str(self.right) + "]")
		return("[" + str(self.left) + "," + str(self.right) + "]")
	def magnitude(self):
		number = 0
		if isinstance(self.left, int):
			number += 3*self.left
		else:
			number += 3*self.left.magnitude()
		if isinstance(self.right, int):
			number += 2*self.right
		else:
			number += 2*self.right.magnitude()
		return number

class Snailfish_Handler:
	@staticmethod
	def init_snailfish_graph(s):
		g_top = Snailfish()
		g = g_top
		first = False
		for e in s:
			if e == '[':
				if first == False:
					first = True
					continue
				obj = Snailfish()
				if g.left == None:
					g.left = obj
				else:
					g.right = obj
				obj.parent = g
				g = obj
			elif e == ',':
				pass
			elif e == ']':
				g = g.parent
			else:
				if g.left == None:
					g.left = int(e)
				else:
					g.right = int(e)
		if isinstance(g_top.left, Snailfish):
			g_top.left.parent = g_top
		if isinstance(g_top.right, Snailfish):
			g_top.right.parent = g_top
		return g_top

	@staticmethod
	def add_snailfish_numbers(g1, g2):
		g = Snailfish()
		g.left = g1
		g.right = g2
		if isinstance(g.left, Snailfish):
			g.left.parent = g
		if isinstance(g.right, Snailfish):
			g.right.parent = g
		return g

	@staticmethod
	def explode(g):
		layer = 1
		obj = g
		visited = [obj.name]
		found = False
		while True:
			if isinstance(obj.left, Snailfish) and obj.left.name not in visited:
				obj = obj.left
				visited.append(obj.name)
				layer += 1
				if layer == 5:
					found = True
					break
			elif isinstance(obj.right, Snailfish) and obj.right.name not in visited:
				obj = obj.right
				visited.append(obj.name)
				layer += 1
				if layer == 5:
					found = True
					break
			else:
				obj = obj.parent
				layer -= 1
			if obj == None:
				break
		#print(found)
		#print(visited)

		if found:
			number_left = obj.left
			print(number_left)
			number_right = obj.right
			#  Find left
			obj_left = obj.parent
			visited = [obj.name, obj_left.name]
			once_left = False
			while True:
				if once_left == False:
					if isinstance(obj_left.left, int):
						obj_left.left += number_left
						break
					elif isinstance(obj_left.left, Snailfish) and obj_left.left.name not in visited:
						once_left = True
						obj_left = obj_left.left
						visited.append(obj_left.name)
					else:
						obj_left = obj_left.parent
						if obj_left == None:
							break
						visited.append(obj_left.name)
				else:
					if isinstance(obj_left.right, int):
						obj_left.right += number_left
						break
					elif isinstance(obj_left.right, Snailfish) and obj_left.right.name not in visited:
						obj_left = obj_left.right
						visited.append(obj_left.name)
					else:
						obj_left = obj_left.parent
						if obj_left == None:
							break
						visited.append(obj_left.name)

			#  Find right
			obj_right = obj.parent
			visited = [obj.name, obj_right.name]
			once_right = False
			while True:
				#print(once_right)
				#print(obj_right.name)
				#print(obj_right.parent.name)
				if once_right == False:
					if isinstance(obj_right.right, int):
						obj_right.right += number_right
						break
					elif isinstance(obj_right.right, Snailfish) and obj_right.right.name not in visited:
						once_right = True
						obj_right = obj_right.right
						visited.append(obj_right.name)
					else:
						obj_right = obj_right.parent
						if obj_right == None:
							break
						visited.append(obj_right.name)
				else:
					if isinstance(obj_right.left, int):
						obj_right.left += number_right
						break
					elif isinstance(obj_right.left, Snailfish) and obj_right.left.name not in visited:
						obj_right = obj_right.left
						visited.append(obj_right.name)
					else:
						obj_right = obj_right.parent
						if obj_right == None:
							break
						visited.append(obj_right.name)

			if obj.parent.left == obj:
				obj.parent.left = 0
			elif obj.parent.right == obj:
				obj.parent.right = 0
		return g, found
	
	@staticmethod
	def split(g):
		obj = g
		visited = [obj.name]
		found = False
		number = None
		while True:
			if isinstance(obj.left, int) and obj.left >= 10:
				number = obj.left
				found = True
				break
			elif isinstance(obj.left, Snailfish) and obj.left.name not in visited:
				obj = obj.left
				visited.append(obj.name)
			elif isinstance(obj.right, int) and obj.right >= 10:
				number = obj.right
				found = True
				break
			elif isinstance(obj.right, Snailfish) and obj.right.name not in visited:
				obj = obj.right
				visited.append(obj.name)
			else:
				obj = obj.parent
			if obj == None:
				break
		#print(found)
		#print(visited)

		if found:
			number_left = math.floor(number / 2.0)
			number_right = math.ceil(number / 2.0)
			x = Snailfish()
			x.left = number_left
			x.right = number_right
			if number == obj.left:
				obj.left = x
			else:
				obj.right = x
			x.parent = obj
			
		return g, found

def add_two_snailfishs(g1, g2):
	g = Snailfish_Handler.add_snailfish_numbers(g1, g2)
	print("Add")
	print(g)

	while True:
		print("Loop")
		found_explode_once = False
		found_split_once = False
		while True:
			g, found_explode = Snailfish_Handler.explode(g)
			if not found_explode:
				break
			else:
				print("Explode")
				print(g)
				found_explode_once = True
		while True:
			g, found_splt = Snailfish_Handler.split(g)
			if not found_splt:
				break
			else:
				print("Split")
				print(g)
				found_split_once = True
				break
		if not found_explode_once and not found_split_once:
			break
	return g

def main1():
	lines = []
	file = 'input'
	#file = 'input_test'
	#file = 'input_opb'
	#file = 'input_hex_2'
	#file = 'input_lit'
	#file = 'input_test3'
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	for l in lines:
		lines_s.append(l.strip())
		
	#  Init with first line
	g = Snailfish_Handler.init_snailfish_graph(lines_s[0])
	for l in lines_s[1:]:
		g2 = Snailfish_Handler.init_snailfish_graph(l)
		g = add_two_snailfishs(g, g2)
	print(g.magnitude())

def main2():
	lines = []
	file = 'input'
	#file = 'input_test'
	#file = 'input_opb'
	#file = 'input_hex_2'
	#file = 'input_lit'
	#file = 'input_test3'
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	for l in lines:
		lines_s.append(l.strip())
		
	len_lines = len(lines_s)
	
	magnitude = -1
	for a in range(len_lines):
		for b in range(len_lines):
			if a == b:
				continue
			g1 = Snailfish_Handler.init_snailfish_graph(lines_s[a])
			g2 = Snailfish_Handler.init_snailfish_graph(lines_s[b])
			g = add_two_snailfishs(g1, g2)
			m_temp = g.magnitude()
			if m_temp > magnitude:
				magnitude = m_temp
	print(magnitude)
				
	
	#for l in lines_s:
	#	g = Snailfish_Handler.init_snailfish_graph(l)
		#print(g)
	#g1 = Snailfish_Handler.init_snailfish_graph(lines_s[0])
	#g2 = Snailfish_Handler.init_snailfish_graph(lines_s[1])
	#g = Snailfish_Handler.add_snailfish_numbers(g1, g2)
	#print(g)
	
	#g1 = Snailfish_Handler.init_snailfish_graph("[[[[4,3],4],4],[7,[[8,4],9]]]")
	#print(g1)
	#g2 = Snailfish_Handler.init_snailfish_graph("[1,1]")
	#print(g2)
	#g = Snailfish_Handler.add_snailfish_numbers(g1, g2)
	#print(g)
	#g = Snailfish_Handler.explode(g)
	#print(g)
	#g = Snailfish_Handler.explode(g)
	#print(g)
	#g = Snailfish_Handler.split(g)
	#print(g)
	#g = Snailfish_Handler.split(g)
	#print(g)
	#g = Snailfish_Handler.explode(g)
	#print(g)
	#g = Snailfish_Handler.init_snailfish_graph("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
	#print(g)
	#g = Snailfish_Handler.explode(g)
	#print(g)

if __name__ == '__main__':
	main2()
