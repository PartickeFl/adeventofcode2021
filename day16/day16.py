import copy
import numpy as np
import math
import statistics
from collections import defaultdict
from enum import Enum
 
import sys

from bitstring import BitArray, BitStream

class TYPE(Enum):
	LIT = 0
	OP_SP = 1
	OP_BITS = 2
	HEADER = 3

class Literal:
	def __init__(self):
		self.typ = TYPE.LIT
		self.parent = None
		self.ver = None
		self.number = None
		self.type_id = 4
	
	def __str__(self):
		return("LIT: Type: " + str(self.type_id) + ", Ver: " + str(self.ver) + ", Number: " + str(self.number) + ", Type: " + str(self.type_id) + '\n')
	
	def quit():
		if self.parent == None:
			return True
		else:
			return False
	
	def add_ver(self):
		return self.ver
	
	def process(self):
		return self.number

class Operator:
	def __init__(self):
		self.parent = None
		self.ver = None
		self.sub_packs = []
		self.type_id = None
	
	def process(self):
		if self.type_id == 0:
			addValue = 0
			for p in self.sub_packs:
				addValue += p.process()
			return addValue
		elif self.type_id == 1:
			multValue = 1
			for p in self.sub_packs:
				multValue *= p.process()
			return multValue
		elif self.type_id == 2:
			minValue = sys.maxsize
			for p in self.sub_packs:
				v = p.process()
				if v < minValue:
					minValue = v
			return minValue
		elif self.type_id == 3:
			maxValue = -1
			for p in self.sub_packs:
				v = p.process()
				if v > maxValue:
					maxValue = v
			return maxValue
		elif self.type_id == 5:
			if self.sub_packs[0].process() > self.sub_packs[1].process():
				return 1
			else:
				return 0
		elif self.type_id == 6:
			if self.sub_packs[0].process() < self.sub_packs[1].process():
				return 1
			else:
				return 0
		elif self.type_id == 7:
			if self.sub_packs[0].process() == self.sub_packs[1].process():
				return 1
			else:
				return 0
		else:
			print("Invalid version: " + str(self.ver))

class Operator_SubPack(Operator):
	def __init__(self):
		super(Operator_SubPack, self).__init__()
		self.typ = TYPE.OP_SP
		self.num_sub_packets = None
		self.counter_sub_packets = 0
	
	def __str__(self):
		s = "OP_SP: Type: " + str(self.type_id) + ", Ver: " + str(self.ver) + ", Counter: " + str(self.num_sub_packets) + '\n'
		for p in self.sub_packs:
			s += str(p)
		return s + '\n'
	
	def add_ver(self):
		ver = copy.copy(self.ver)
		for p in self.sub_packs:
			ver += p.add_ver()
		return ver
	
class Operator_Bits(Operator):
	def __init__(self):
		super(Operator_Bits, self).__init__()
		self.typ = TYPE.OP_BITS
		self.length = None
		self.start_c = None
	
	def __str__(self):
		s = "OP_Bits: Type: " + str(self.type_id) + ", Ver: " + str(self.ver) + ", Counter: " + str(self.length) + '\n'
		for p in self.sub_packs:
			s += str(p)
		return s
	
	def add_ver(self):
		ver = copy.copy(self.ver)
		for p in self.sub_packs:
			ver += p.add_ver()
		return ver

def main1():
	lines = []
	file = 'input'
	#NCN
	#NBCCN
	#file = 'input_test'
	#file = 'input_opb'
	#file = 'input_hex_2'
	#file = 'input_lit'
	#file = 'input_test3'
	with open(file) as f:
		lines = f.readlines()
	
	s_hex = lines[0].strip()
	print(s_hex)
	o_head = None
	ot = None
	scale = 16 ## equals to hexadecimal

	num_of_bits = int(len(s_hex) * math.log2(scale))
	s = bin(int(s_hex, scale))[2:].zfill(num_of_bits)
	print(s)
	
	c = 0
	typ = TYPE.HEADER
	while True:
		print(typ)
		if typ == TYPE.HEADER:
			ver = int(s[c:c+3], 2)
			typ_int = int(s[c+3:c+6], 2)
			c += 6
			ot_c = None
			if typ_int == 4:
				ot_c =  Literal()
				typ = TYPE.LIT
			else:
				if s[c] == '0':
					ot_c = Operator_Bits()
				else:
					ot_c = Operator_SubPack()
				c+=1
			ot_c.ver = ver
			ot_c.type_id = typ_int
			typ = ot_c.typ
			if o_head == None:
				o_head = ot_c
				ot = ot_c
			else:
				ot_c.parent = ot
				ot.sub_packs.append(ot_c)
				ot = ot_c
		elif typ == TYPE.LIT:
			bit_s = ''
			while True:
				break_bit = s[c]
				bit_s += s[c+1:c+5]
				c += 5
				if break_bit == '0':
					break
			ot.number = int(bit_s, 2)
			if ot.parent == None:
				break
			else:
				ot = ot.parent
				typ = ot.typ
		elif typ == TYPE.OP_BITS:
			if ot.length == None:
				n = int(s[c:c+15], 2)
				ot.length = n
				c += 15
				ot.start_c = c
			if c-ot.start_c >= ot.length:
				if ot.parent == None:
					break
				else:
					ot = ot.parent
					typ = ot.typ
			else:
				typ = TYPE.HEADER
		elif typ == TYPE.OP_SP:
			if ot.num_sub_packets == None:
				n = int(s[c:c+11], 2)
				ot.num_sub_packets = n
				c += 11
			else:
				ot.counter_sub_packets += 1
			if ot.counter_sub_packets >= ot.num_sub_packets:
				if ot.parent == None:
					break
				else:
					ot = ot.parent
					typ = ot.typ
			else:
				typ = TYPE.HEADER
		else:
			pass
		
	print(o_head)
	print(o_head.add_ver())
	print(o_head.process())

if __name__ == '__main__':
	main1()
