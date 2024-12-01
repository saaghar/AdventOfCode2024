import fileinput

list_1, list_2 = [], []

for line in fileinput.input(files='data.txt'):
    list_1.append(int(line.split(None)[0]))
    list_2.append(int(line.split(None)[1]))

list_1.sort()
list_2.sort()

part_1 = 0
for i in range(len(list_1)):
    part_1 += abs(list_1[i] - list_2[i])
    
print(part_1)
