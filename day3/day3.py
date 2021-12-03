
import copy

def main1():
	lines = []
	with open('input') as f:
		lines = f.readlines()

	# counter
	l_length = len(lines[0])
	counter = [0] * l_length
	counter_inv = [0] * l_length
	for line in lines:
		c = 0
		for l in line:
			if l == '1':
				counter[c] += 1
			elif l == '0':
				counter_inv[c] += 1
			c += 1
	
	counter.pop()
	counter_inv.pop()
	gamma = ''
	diag = ''
	for c in range(len(counter)):
		if counter[c] > counter_inv[c]:
			gamma += '1'
			diag += '0'
		else:
			gamma += '0'
			diag += '1'
	
	print(gamma)
	print(diag)
	gamma_int = int(gamma, 2)
	diag_int = int(diag, 2)
	print(gamma_int*diag_int)
	return lines, gamma, diag

def main3():
	orig_lines, most_prob, least_prob = main1()
	lines = copy.copy(orig_lines)
	
	# counter / up
	l_length = len(lines[0].strip())
	for c in range(l_length):
		
		counter = 0
		counter_inv = 0
		new_lines_up =  []
		for line in lines:
			line = line.strip()
			if line[c] == '1':
				counter += 1
			elif line[c] == '0':
				counter_inv += 1
		
		if counter >= counter_inv:
			target = '1'
		else:
			target = '0'
		
		for line in lines:
			line = line.strip()
			if line[c] == target:
				new_lines_up.append(line)
	
		if len(new_lines_up) == 1:
			break
		
		lines = new_lines_up
		#print('---------------------')
		#print(lines)
	
	print(new_lines_up[0])
	
	# counter / down
	lines = copy.copy(orig_lines)
	l_length = len(lines[0].strip())
	for c in range(l_length):
		
		counter = 0
		counter_inv = 0
		new_lines_down =  []
		for line in lines:
			line = line.strip()
			if line[c] == '1':
				counter += 1
			elif line[c] == '0':
				counter_inv += 1
		
		if counter < counter_inv:
			target = '1'
		else:
			target = '0'
		
		for line in lines:
			line = line.strip()
			if line[c] == target:
				new_lines_down.append(line)
	
		if len(new_lines_down) == 1:
			break
		
		lines = new_lines_down
		#print('---------------------')
		#print(lines)
		
	
	print(new_lines_down[0])
	
	m = int(new_lines_up[0], 2)
	l = int(new_lines_down[0], 2)
	print(m*l)
	

if __name__ == '__main__':
	main3()