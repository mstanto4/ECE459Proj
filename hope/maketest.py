import sys

for num in range(0, pow(2,int(sys.argv[1]))):
	test = num + 1
	print(str(test) + ": " + format(num, '033b'))




