input = "input.txt"
pairs = []
updates = []
with open(input) as file:
	for line in file:
		
			
		x= line.strip().split("|")
		if len(x) == 1:
			x = line.strip().split(",")
			updates.append(x)
		if len(x) == 2:
			pairs.append(x)

if len(updates[0]) == 1:
	del updates[0]

def check_pair(lists, a, b):
	
	for item in lists:
		if a in item and b in item:
			if (item[0] == a) and (item[1] == b):
				return True
			else:
				return False
	return True		
				
filtered_lists = []

for item in updates:
	keep_item = True
	for i in range(len(item) -1):
		a = item[i]
		b = item[i + 1]
		if not check_pair(pairs, a, b):
			keep_item = False
			break
	if keep_item:
		filtered_lists.append(item)
numb = [[int(x) for x in i] for i in filtered_lists]
middle = [sublist[len(sublist) // 2] for sublist in numb]
sum = 0
for i in middle:
	sum += i
print(sum)
#part2
failed_list = [item for item in updates if item not in filtered_lists]


for item in failed_list:
	correct = False
	while correct is False:
		correct = True
		for i in range(len(item) -1):
			
			a = item[i]
			b = item[i+1]
			if not check_pair(pairs, a ,b):
				
				item[i] = b
				item[i+1] = a
				correct = False
				break
		

numb = [[int(x) for x in i] for i in failed_list]
middle = [sublist[len(sublist) // 2] for sublist in numb]

sum = 0
for i in middle:
	sum += i
print(sum)
