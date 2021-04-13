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

#convert to VHDL code
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
			codeStr = codeStr + "not (" + temp3[0] + " "
		else:
			codeStr = codeStr + temp3[0] + " "

		for i in range(1, len(temp3) - 1):
			codeStr = codeStr + operation + " " + temp3[i] + " "
		codeStr = codeStr + operation + " " + temp3[len(temp3) - 1] 	
	
		if(newop == True):
			codeStr = codeStr + ");"
		else:
			codeStr = codeStr + ";"

		code.append(codeStr)
	else:
		
		temp3 = temp2[1].strip().split('(')
		temp3 = temp3[0].split(')')
		input1 = temp3[0]		
		
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

print("    clock: in std_logic;")
print("    Anodes: out std_logic_vector(3 downto 0);")
print("    seg: out std_logic_vector(6 downto 0)")

print("  );")
print("end " + title[1] + ";\n")

print("architecture behavioral of " + title[1] + " is")

#print signals
signal = "  signal "
for i in range(0, len(signals) - 1):
	if(i % 10 == 0 and i != 0):
		signal = signal + "\n"
	signal = signal + signals[i] + ", "
		
signal = signal + signals[len(signals) - 1] + ": std_logic := '0';"
print(signal)

signal = "  signal "
for i in range(0, len(inputs) - 1):
	if(i % 10 == 0 and i != 0):
		signal = signal + "\n"
	signal = signal + inputs[i] + ", "
		
signal = signal + inputs[len(inputs) - 1] + ": std_logic;"
print(signal)

signal = "  signal "
for i in range(0, len(outputs) - 1):
	if(i % 10 == 0 and i != 0):
		signal = signal + "\n"
	signal = signal + outputs[i] + ", "
		
signal = signal + outputs[len(outputs) - 1] + ": std_logic;"
print(signal)

print("  signal output: std_logic_vector(" + str(len(outputs) - 1) + " downto 0);")

print("begin")

#print converted code
for i in range(0, len(code)):
	print("  " + code[i])

for i in range(0, len(outputs)):
	print("  output(" + str(i)+") <= " + outputs[i] + ";")

print("end behavioral;")







