
def main1():
	lines = []
	with open('input') as f:
		lines = f.readlines()

	count = 0
	pnum = None
	num = None
	fN = False
	for line in lines:
		num = int(line)
		if fN == False:
			pnum = num
			fN = True
			continue
		else:
			if num > pnum:
				count += 1
			pnum = num
	print(count)

def main2():
	lines = []
	with open('input') as f:
		lines = f.readlines()
	
	countMeas = -1
	sl = [0, 0, 0]
	numSL = [0, 0, 0]
	counter = 0
	prevSum = -1
	for line in lines:
		num = int(line)
		if counter == 0:
			sl[0] += num
			numSL[0] += 1
		elif counter == 1:
			sl[0] += num
			sl[1] += num
			
			numSL[0] += 1
			numSL[1] += 1
		elif counter >= 2:
			sl[0] += num
			sl[1] += num
			sl[2] += num
			
			numSL[0] += 1
			numSL[1] += 1
			numSL[2] += 1
		
		for i in range(len(numSL)):
			if numSL[i] >= 3:
				dispStr = ""
				if sl[i] > prevSum:
					countMeas += 1
					dispStr = "increased"
				prevSum = sl[i]
				print(str(sl[i]) + ": " + dispStr)
				numSL[i] = 0
				sl[i] = 0
		counter += 1
	print(countMeas)

if __name__ == '__main__':
	main2()