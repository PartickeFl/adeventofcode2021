
import copy
import statistics


def add_sum(sum_in, l):
	print(l)
	if l == ']':
		return sum_in + 57
	elif l == ')':
		return sum_in + 3
	elif l == '}':
		return sum_in + 1197
	else:
		return sum_in + 25137

def add_sum2(sum_in, l):
	if l == '[':
		return sum_in + 2
	elif l == '(':
		return sum_in + 1
	elif l == '{':
		return sum_in + 3
	else:
		return sum_in + 4

def main1():
	lines = []
	file = 'input'
	#file = 'input_test'
	#file = 'input_test2'
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	for l in lines:
		lines_s.append(l.strip()) 
	
	sum_list = []
	sum_letter = 0
	for l in lines_s:
		list_letter = []
		nf = False
		for letter in l:
			#print(list_letter)
			if letter == '[' or letter == '(' or letter == '{' or letter == '<':
				list_letter.append(letter)
			else:
				if len(list_letter) == 0:
					break
				if letter == ']' and list_letter[-1] == '[':
					list_letter.pop()
				elif letter == ')' and list_letter[-1] == '(':
					list_letter.pop()
				elif letter == '}' and list_letter[-1] == '{':
					list_letter.pop()
				elif letter == '>' and list_letter[-1] == '<':
					list_letter.pop()
				else:
					sum_letter = add_sum(sum_letter, letter)
					nf = True
					break
		if not nf:
			list_letter.reverse()
			tt = 0
			for e in list_letter:
				tt *= 5
				tt = add_sum2(tt, e)
			sum_list.append(tt)
	
	m = statistics.median(sum_list)
	m = int(m)
	print(m)
	print(sum_list)
	#print(sum_letter)

if __name__ == '__main__':
	main1()