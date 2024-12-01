list1 = []
list2 = []
distance = []
similarity = []

with open("puzzleinp1.txt", "r") as file:
        for line in file:
                test = line.strip().split()
                c = True
                for i in test:
                        i = int(i)
                        if c == True:
                                list1.append(i)
                                c = False
                        else:
                                list2.append(i)
                                c = True


#part 2 of puzzle
'''for i in list1:
        simc = 0
        for n in list2:

                if i == n:
                        simc += 1
        similarity.append(i * simc)

total = 0
for i in similarity:
        total = total + i
print(total)
list1.sort()
list2.sort()'''


#part 1 of puzzle
'''for x, y in zip(list1, list2):
        z = abs(x - y)
        distance.append(z)
print(distance)
total = 0
for i in distance:
        total = total + i
print(total)'''                                                                                                                                        
