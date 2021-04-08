import numpy as np
import sys

signals = []
inputs = []
outputs = []
code = []

netlist = open(sys.argv[1], "r")
lines = netlist.readlines()

#skip comment sections
curline = 0
while(lines[curline][0] == "#"):
	curline = curline + 1

#save inputs
while(lines[curline][0] == "I"):
	temp = lines[curline].strip().split('(')
	temp = temp[1].split(')')
	inputs.append(temp[0])
	curline = curline + 1

#save outputs
while(lines[curline][0] == "O"):
	temp = lines[curline].strip().split('(')
	temp = temp[1].split(')')
	outputs.append(temp[0])
	curline = curline + 1

#skip empty line
curline = curline + 1
keynum = 0
keyin = False
#convert to VHDL code
for i in range(curline, len(lines)-1):
	temp = lines[i].strip().split('=')
	result = temp[0].strip()
	
	if(not(result in inputs) and not(result in outputs)):
		if(not(result in signals)):
			signals.append(result)
	
	temp2 = temp[1].strip().split('(')
	operation = temp2[0]
	
	if(operation != "buf" and operation != "not"):
		temp3 = temp2[1].split(',')
		if(" key" in temp3):
			key = True
			keyin = True
		else:
			key = False
			temp3[len(temp3) - 1] = temp3[len(temp3) - 1][0:len(temp3[len(temp3) - 1]) - 1]
		if(operation == "nand" and len(temp3) > 2):
			newop = True
			operation = "and"
		elif(operation == "nor" and len(temp3) > 2):
			newop = True
			operation = "or"		
		else:
			newop = False
	
		codeStr = result + " <= "
	
		if(newop == True):
			if(temp3[0] == " key"):
				codeStr = codeStr + "not (" + temp3[0] + "(" + str(keynum) + ") "
			else:
				codeStr = codeStr + "not (" + temp3[0] + " "
		else:
			if(temp3[0] == " key"):
				codeStr = codeStr + temp3[0] + "(" + str(keynum) + ") "
			else:
				codeStr = codeStr + temp3[0] + " "
					
		for i in range(1, len(temp3) - 1):
			if(temp3[i] == " key"):
				codeStr = codeStr + operation + " " + temp3[i] + "(" + str(keynum) + ") "
			else:
				codeStr = codeStr + operation + " " + temp3[i] + " "
		
		if(temp3[len(temp3) - 1] == " key"):
			codeStr = codeStr + operation + " " + temp3[len(temp3) - 1] + "(" + str(keynum) + ")"		
		else:		
			codeStr = codeStr + operation + " " + temp3[len(temp3) - 1] 	
	
		if(newop == True):
			codeStr = codeStr + ");"
		else:
			codeStr = codeStr + ";"

		code.append(codeStr)
		if(key == True):
			keynum = keynum + 1

	else:
		
		temp3 = temp2[1].strip().split('(')
		input1 = temp3[0][0:len(temp3[0])-1]		
		
		if(operation == "not"):		
			code.append(result + " <= " + operation + " " + input1 + ";") 
		else:
			code.append(result + " <= " + input1 + ";")
	curline = curline + 1	

#print in correct output for VHDL file
print("library IEEE;")
print("use IEEE.STD_LOGIC_1164.ALL;\n")

titlefirst = sys.argv[1].split('.')
title = titlefirst[0].split('/')
print("entity " + title[1] + " is")

print("  port (")

#print inputs
for i in range(0, len(inputs)):
	print("    " + inputs[i] + " : in std_logic := '0';")
if(keyin == True):
	tempkey = lines[len(lines)-1].split("#")
	keysig = tempkey[1][1:len(tempkey[1])-1]
	keylen = len(keysig)
	if(keylen > 1):
		print("    key: in std_logic_vector(" + str(keylen-1) + " downto 0) := \"" + keysig + "\";")
	else:
		print("    key: in std_logic := '" + keysig + "';")

#print outputs
for i in range(0, len(outputs) - 1):
	print("    " + outputs[i] + " : out std_logic;")

print("    " + outputs[len(outputs) - 1] + " : out std_logic")
print("  );")
print("end " + title[1] + ";\n")

print("architecture behavioral of " + title[1] + " is")

#print signals
signal = "  signal "
for i in range(0, len(signals) - 1):
	if(i % 10 == 0 and i != 0):
		signal = signal + "\n"
	signal = signal + signals[i] + ", "
		
signal = signal + signals[len(signals) - 1] + ": std_logic;"
print(signal)

print("begin")

#print converted code
for i in range(0, len(code)):
	print("  " + code[i])

print("end behavioral;")







