import numpy as np
import sys
import random

key = []
nodes = []
FI = []
gateStr = "gate"

#sys.argv[1] = netlist
#sys.argv[2] = faultImpact
#sys.argv[3] = # of gates

faultImpact = open(sys.argv[2], "r")
FIlines = faultImpact.readlines()

for line in FIlines:
	text = line.split(' ')
	nodes.append(text[0])
	FI.append(int(text[1][0:len(text[1])-1]))

#sorted greatest to least	
FI, nodes = (list(t) for t in zip(*sorted(zip(FI, nodes), reverse = True)))


netlist = open(sys.argv[1], "r")
lines = netlist.readlines()

for i in range(0, len(lines)):
	lines[i] = lines[i][0:len(lines[i])-1]

#skip comment sections and inputs and outputs
curline = 0
while(len(lines[curline]) > 0):
	curline = curline + 1
#skip empty line
curline = curline + 1

lineLen = len(lines)

for i in range(0, int(sys.argv[3])):
	if("->" in nodes[i]):
		print("one")		
	else:	
		indicies = []
		for j in range(curline, lineLen):
			if(nodes[i] in lines[j]):
				index = lines[j].index(nodes[i])
				#not an output
				if(index > 0):
					indicies.append(j)
					
		randop = random.randint(0,1)
		#insert xnor
		if(randop == 1):
			op = "xnor"
		else:
			op = "xor"

		randinv = random.randint(0,1)
		newgateStr = gateStr + str(i+1)
		invStr = newgateStr + "inv"
		for k in range(0, len(indicies)):
			temp = lines[indicies[k]].split(nodes[i])
			if(randinv == 0):
				lines[indicies[k]] = temp[0] + newgateStr + temp[1]
			else:		
				lines[indicies[k]] = temp[0] + invStr + temp[1]
		#node is output
		if(len(indicies) == 0):
			for l in range(curline, lineLen):
				if(nodes[i] in lines[l]):
					temp = lines[l].split(nodes[i])
					if(randinv == 0):
						lines[l] = newgateStr + temp[1]	
						lines.append(nodes[i] + " = buf(" + newgateStr + ")")	
					else:
						lines[l] = invStr + temp[1]	
						lines.append(nodes[i] + " = buf(" + invStr + ")")	

		#do not add inverter
		if(randinv == 0):
			key.append(0)	
			lines.append(newgateStr + " = " + op + "(" + nodes[i] + ", key(" + str(i) + "))") 
		#add inverter
		else:
			key.append(1)
			lines.append(newgateStr + " = " + op + "(" + nodes[i] + ", key(" + str(i) + "))") 
			lines.append(invStr + " = not(" + newgateStr + ")")

for line in lines:
	print(line)

keyStr = "# "
for bit in key:
	keyStr = keyStr + str(bit)
print(keyStr)
	
