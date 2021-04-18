import numpy as np
import sys

nodes = []
fault1 = []
fault0 = []
faultOut1 = []
faultOut0 = []
faultImpact = []

fault = open(sys.argv[1], "r")
lines = fault.readlines()

for line in lines:
	#if line starts with t then it is the line that contains the testing information
	if(line[0] == 't'):
		temp = line.split(' ')
		output = temp[len(temp)-1][0:len(temp[len(temp)-1])-1]
	#otherwise it is a fault
	else:
		if('*' in line):
			temp = line.split(' ')
			#if node already in list
			if(temp[2] in nodes):
				index = nodes.index(temp[2])
				#stuck at 0
				if(temp[3][1] == '0'):
					fault0[index] = fault0[index] + 1
					diff = 0
					#calculate difference in outputs
					for num, x in enumerate(output):
						if(x != temp[5][num]):
							diff = diff + 1
					faultOut0[index] = faultOut0[index] + diff
				#stuck at 1
				else:
					fault1[index] = fault1[index] + 1
					diff = 0
					#calculate difference in outputs
					for num, x in enumerate(output):
						if(x != temp[5][num]):
							diff = diff + 1
					faultOut1[index] = faultOut1[index] + diff	
			else:
				nodes.append(temp[2])
				#stuck at 0
				if(temp[3][1] == '0'):
					fault0.append(1)
					fault1.append(0)
					diff = 0
					#calculate difference in outputs
					for num, x in enumerate(output):
						if(x != temp[5][num]):
							diff = diff + 1
					faultOut0.append(diff)
					faultOut1.append(0)
				else:
					fault1.append(1)
					fault0.append(0)
					diff = 0
					#calculate difference in outputs
					for num, x in enumerate(output):
						if(x != temp[5][num]):
							diff = diff + 1
					faultOut1.append(diff)
					faultOut0.append(0)

#calculate fault impact
for i in range(0, len(fault0)):
	FI = (fault0[i] * faultOut0[i]) + (fault1[i] * faultOut1[i])
	faultImpact.append(FI)

#print results 
for i in range(0, len(faultImpact)):
	print(nodes[i] + ' ' + str(faultImpact[i]))

