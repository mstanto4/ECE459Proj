
f = open("c17EncNetlist.txt")

lines = f.readlines()
listofNums = []

for index, line in enumerate(lines):
    count = 0
    if index == 2:
        answer = line
    elif index > 2 and index % 2 == 0:
        count = 0

        for i in range(len(answer)-1):
            if answer[i] == line[i]:
                count = count + 1

        listofNums.append(count)

sum = 0
for item in listofNums:
    sum = sum + item/(len(answer)-1)

result = sum / len(listofNums)

print(result)