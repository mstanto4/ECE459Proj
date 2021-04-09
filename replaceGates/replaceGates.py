import numpy as np
import sys
import random

key = []
nodes = []
FI = []
gateStr = "gate"
tempStr = "temp"

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
		indicies = []
		arrow = nodes[i].split("->")
		for j in range(curline, lineLen):
			if(arrow[0] in lines[j]):
				index = lines[j].index(arrow[0])

				#not an output
				if(index > 0 and (lines[j][index+len(arrow[0])] == "," or lines[j][index+len(arrow[0])] == ")")):
					if(arrow[1] in lines[j]):
						indicies.append(j)
				
		randop = random.randint(0,1)

		#insert xnor
		if(randop == 1):
			op = "xnor"
			value = 1
		else:
			op = "xor"
			value = 0

		randinv = random.randint(0,1)

		newgateStr = gateStr + str(i+1)
		invStr = newgateStr + "inv"

		for k in range(0, len(indicies)):
			curindex = lines[j].index(arrow[0])
			while(lines[j][curindex+len(arrow[0])] != "," or lines[j][curindex+len(arrow[0])] != ")"):
				curindex = lines[j].index(arrow[0], curindex)

			if(randinv == 0):
				lines[indicies[k]] = lines[indicies[k]][0:curindex] + newgateStr + lines[indicies[k]][curindex+len(arrow[0]):len(lines[indicies[k]])]
			else:		
				lines[indicies[k]] = lines[indicies[k]][0:curindex] + invStr + lines[indicies[k]][curindex+len(arrow[0]):len(lines[indicies[k]])]

		#do not add inverter
		if(randinv == 0):
			key.insert(0,value)
			insertVal = newgateStr + " = " + op + "(" + arrow[0] + ", key(" + str(i) + "))"

			#TEST
			#print("insert val is", insertVal)

			lines.append(insertVal)
		#add inverter
		else:

			#TEST
			#print("invertor?")

			if(value == 1):
				key.insert(0,0)
			else:
				key.insert(0,1)
			lines.append(newgateStr + " = " + op + "(" + arrow[0] + ", key(" + str(i) + "))") 
			lines.append(invStr + " = not(" + newgateStr + ")")
	else:	
		indicies = []
		for j in range(curline, lineLen):
			if(nodes[i] in lines[j]):
				index = lines[j].index(nodes[i])
				#not an output
				print(lines[j])
				print(lines[j][index+len(nodes[i])])
				if(index > 0 and (lines[j][index+len(nodes[i])] == "," or lines[j][index+len(nodes[i])] == ")")):
					indicies.append(j)
					
		randop = random.randint(0,1)

		#insert xnor
		if(randop == 1):
			op = "xnor"
			value = 1
		else:
			op = "xor"
			value = 0

		randinv = random.randint(0,1)

		newgateStr = gateStr + str(i+1)

		invStr = newgateStr + "inv"
		for k in range(0, len(indicies)):
			print(lines[indicies[k]])
			print(nodes[i])
			curindex = lines[indicies[k]].index(nodes[i])
			print(lines[indicies[k]][curindex+len(nodes[i])])
			while(lines[indicies[k]][curindex+len(nodes[i])] != "," or lines[indicies[k]][curindex+len(nodes[i])] != ")"):
				curindex = lines[indicies[k]].index(nodes[i], curindex)
			#insert fix here
			#temp = lines[indicies[k]].split(nodes[i])

			if(randinv == 0):
				lines[indicies[k]] = lines[indicies[k]][0:curindex] + newgateStr + lines[indicies[k]][curindex+len(arrow[0]):len(lines[indicies[k]])]
				#lines[indicies[k]] = temp[0] + newgateStr + temp[1]
			else:		
				lines[indicies[k]] = lines[indicies[k]][0:curindex] + invStr + lines[indicies[k]][curindex+len(arrow[0]):len(lines[indicies[k]])]
				#lines[indicies[k]] = temp[0] + invStr + temp[1]

		#node is output
		if(len(indicies) == 0):
			for l in range(curline, lineLen):
				if(nodes[i] in lines[l]):
					#insert fix here
					temp = lines[l].split(nodes[i])
					lines[l] = tempStr + str(i) + temp[1]	
					if(randinv == 0):
						lines.append(nodes[i] + " = buf(" + newgateStr + ")")	
					else:
						lines.append(nodes[i] + " = buf(" + invStr + ")")
			#do not add inverter
			if(randinv == 0):
				key.insert(0,value)	
				lines.append(newgateStr + " = " + op + "(" + tempStr + str(i) + ", key(" + str(i) + "))") 
			#add inverter
			else:
				if(value == 1):
					key.insert(0,0)
				else:
					key.insert(0,1)
				key.insert(0,1)
				lines.append(newgateStr + " = " + op + "(" + tempStr + str(i) + ", key(" + str(i) + "))") 
				lines.append(invStr + " = not(" + newgateStr + ")")
		
		else:
			#do not add inverter
			if(randinv == 0):
				key.insert(0,value)	
				lines.append(newgateStr + " = " + op + "(" + nodes[i] + ", key(" + str(i) + "))") 
			#add inverter
			else:
				if(value == 1):
					key.insert(0,0)
				else:
					key.insert(0,1)
				lines.append(newgateStr + " = " + op + "(" + nodes[i] + ", key(" + str(i) + "))") 
				lines.append(invStr + " = not(" + newgateStr + ")")

for line in lines:
	print(line)
#
# TEST
keyStr = "# "
for bit in key:
	keyStr = keyStr + str(bit)
print(keyStr)
	
