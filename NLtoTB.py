import numpy as np
import sys

signals = []

netlist = open(sys.argv[1], "r")
lines = netlist.readlines()

#skip comment sections
curline = 0
while(lines[curline][0] == "#"):
	curline = curline + 1

#save inputs
while(lines[curline][0] == "I" or lines[curline][0] == "O"):
	temp = lines[curline].strip().split('(')
	temp = temp[1].split(')')
	signals.append(temp[0])
	curline = curline + 1

if(lines[len(lines)-1][0] == "#"):
	tempkey = lines[len(lines)-1].split("#")
	keysig = tempkey[1][1:len(tempkey[1])-1]
	keylen = len(keysig)
	key = True
else:
	key = False

#print in correct output for VHDL file
print("library IEEE;")
print("use IEEE.STD_LOGIC_1164.ALL;\n")

titlefirst = sys.argv[1].split('.')
title = titlefirst[0].split('/')
print("entity " + title[1] + "_tb is")
print("-- Port ();")
print("end " + title[1] + "_tb;\n")

print("architecture behavioral of " + title[1] + " is")


signal = "  signal "
for i in range(0, len(signals) - 1):
	if(i % 10 == 0 and i != 0):
		signal = signal + "\n  "
	signal = signal + "T" + signals[i] + ", "
		
signal = signal + "T" + signals[len(signals) - 1] + ": std_logic;"
print(signal)

if(key == True):
	if(keylen > 1):
		print("  signal Tkey: std_logic_vector(" + str(keylen-1) + " downto 0) := \"" + keysig + "\";")
	else:
		print("  signal Tkey: std_logic := '" + keysig + "';")

print("begin")
print("  L1: entity work." + title[1] + "(behavioral)")
portmap = "  port map("
for i in range(0, len(signals) - 1):
        if(i % 10 == 0 and i != 0):
                portmap = portmap + "\n  "
        portmap = portmap + signals[i] + "=> T" + signals[i] + ", "
if(key == True):
	portmap = portmap + "key => Tkey" + ", "

portmap = portmap + signals[len(signals) - 1] + "=> T" + signals[len(signals) - 1] + ");"

print(portmap)

print("  process")
print("  begin\n\n")

print("  end process;")
print("end behavioral;")






