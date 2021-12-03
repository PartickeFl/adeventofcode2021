
def main1():
	lines = []
	with open('input') as f:
		lines = f.readlines()

	horz = 0
	depth = 0
	for line in lines:
		d, val = line.split()
		val = int(val)
		d = d.strip()
		if d == 'forward':
			horz += val
		elif d == 'up':
			depth -= val
		elif d == 'down':
			depth += val
	print(horz*depth)

def main2():
	lines = []
	with open('input') as f:
		lines = f.readlines()

	horz = 0
	depth = 0
	aim = 0
	for line in lines:
		d, val = line.split()
		val = int(val)
		d = d.strip()
		if d == 'forward':
			horz += val
			depth += aim*val
		elif d == 'up':
			aim -= val
		elif d == 'down':
			aim += val
	print(horz*depth)

if __name__ == '__main__':
	main2()