
import copy

def main1():
	lines = []
	with open('input') as f:
		lines = f.readlines()

	inputs = lines[0]
	numbers = inputs.strip().split(',')
	
	int_num = []
	for n in numbers:
		int_num.append(int(n.strip()))
	
	bool_boards = [[]]
	boards = [[]]
	n = 0
	c = 0
	for l in lines:
		if c >= 2 and c < 7:
			ll = l.strip().replace('  ', ' ').split(' ')
			boards[n].append(ll)
			b = [False] * len(ll)
			bool_boards[n].append(b)
		elif c >= 7:
			boards.append([])
			bool_boards.append([])
			n += 1
			c = 1
		c+=1
	#for b in boards:
	#	print('--------------------------')
	#	print(b)
	#for b in bool_boards:
	#	print('--------------------------')
	#	print(b)
	quadr_dist = len(bool_boards[0][0])
	for n in int_num:
		
		#  Set num
		for c in range(len(boards)):
			for d in range(len(boards[c])):
				for e in range(len(boards[c][d])):
					if int(boards[c][d][e]) == n:
						bool_boards[c][d][e] = True
		
		bingo = True
		#  Check bingo
		for c in range(len(bool_boards)):
			for d in range(len(bool_boards[c])):
				bingo = True
				for e in range(len(bool_boards[c][d])):
					if bool_boards[c][d][e] == False:
						bingo = False
						break
				if bingo:
					break
			
			#  Check columns
			if not bingo:
				for col in range(quadr_dist):
					bingo = True
					for d in range(len(bool_boards[c])):
						if bool_boards[c][d][col] == False:
							bingo = False
							break
					if bingo:
						break
			
			
			if bingo:
				s = 0
				for d in range(len(bool_boards[c])):
					for e in range(len(bool_boards[c][d])):
						if bool_boards[c][d][e] == False:
							s += int(boards[c][d][e])
				print(s*n)
				break
		if bingo:
			break

def main2():
	lines = []
	with open('input') as f:
		lines = f.readlines()

	inputs = lines[0]
	numbers = inputs.strip().split(',')
	
	int_num = []
	for n in numbers:
		int_num.append(int(n.strip()))
	
	bool_boards = [[]]
	boards = [[]]
	n = 0
	c = 0
	for l in lines:
		if c >= 2 and c < 7:
			ll = l.strip().replace('  ', ' ').split(' ')
			boards[n].append(ll)
			b = [False] * len(ll)
			bool_boards[n].append(b)
		elif c >= 7:
			boards.append([])
			bool_boards.append([])
			n += 1
			c = 1
		c+=1
	#for b in boards:
	#	print('--------------------------')
	#	print(b)
	#for b in bool_boards:
	#	print('--------------------------')
	#	print(b)
	l_boards = list(range(len(boards)))
	quadr_dist = len(bool_boards[0][0])
	global_break = False
	for n in int_num:
		
		#  Set num
		for c in range(len(boards)):
			for d in range(len(boards[c])):
				for e in range(len(boards[c][d])):
					if int(boards[c][d][e]) == n:
						bool_boards[c][d][e] = True
		
		bingo = True
		#  Check bingo
		for c in range(len(bool_boards)):
			if c not in l_boards:
				continue
			for d in range(len(bool_boards[c])):
				bingo = True
				for e in range(len(bool_boards[c][d])):
					if bool_boards[c][d][e] == False:
						bingo = False
						break
				if bingo:
					break
			
			#  Check columns
			if not bingo:
				for col in range(quadr_dist):
					bingo = True
					for d in range(len(bool_boards[c])):
						if bool_boards[c][d][col] == False:
							bingo = False
							break
					if bingo:
						break
			
			
			if bingo:
				s = 0
				for d in range(len(bool_boards[c])):
					for e in range(len(bool_boards[c][d])):
						if bool_boards[c][d][e] == False:
							s += int(boards[c][d][e])
				print(s*n)
				if c in l_boards:
					l_boards.remove(c)
					print(l_boards)
				if len(l_boards) == 0:
					global_break = True
		if global_break:
			break

if __name__ == '__main__':
	main2()