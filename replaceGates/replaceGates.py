import numpy as np
import sys

key = []
nodes = []
FI = []

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




