import numpy as np
import sys

signals = []
inputs = []
outputs = []

netlist = open(sys.argv[1], "r")
lines = netlist.readlines()

print(lines)

