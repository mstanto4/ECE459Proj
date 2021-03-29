import numpy as np
import sys

signals = []
inputs = []
outputs = []

netlist = open(sys.argv[1], "r")
lines = netlist.readlines()

curline = 0
while(lines[curline][0] == "#"):
	curline = curline + 1

while(lines[curline][0] == "I"):
	temp = lines[curline].strip().split('(')
	temp = temp[1].split(')')
	inputs.append(temp[0])
	curline = curline + 1

while(lines[curline][0] == "O"):
	temp = lines[curline].strip().split('(')
	temp = temp[1].split(')')
	outputs.append(temp[0])
	curline = curline + 1

curline = curline + 1

for i in range(curline, len(lines)):
	temp = lines[i].strip().split('=')
	result = temp[0].strip()
	
	if(not(result in inputs) and not(result in outputs)):
		if(not(result in signals)):
			signals.append(result)

	temp2 = temp[1].strip().split('(')
	operation = temp2[0]
	
	if(operation != "buf" and operation != "not"):
		temp3 = temp2[1].split(',')
		input1 = temp3[0]

		temp4 = temp3[1].strip().split(')')
		input2 = temp4[0]	
		
		VHDL = result + " <= " + input1 + " " +  operation + " " + input2 + ";"
	else:
		
		temp3 = temp2[1].strip().split('(')
		temp3 = temp3[0].split(')')
		input1 = temp3[0]		

		if(operation == "not"):		
			VHDL = result + " <= " + operation + " " + input1 + ";" 
		else:
			VHDL = result + " <= " + input1 + ";"
	print(VHDL)
	curline = curline + 1	




