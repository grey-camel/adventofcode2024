mainlist = []


with open("input.txt", "r") as file:
	for line in file:
		x = line.strip().split()
		secondlist = []
		for i in x:
			i = int(i)
			secondlist.append(i)
		mainlist.append(secondlist)

def steady_check(sub):
    return all(sub[i] < sub[i+1] for i in range(len(sub) - 1)) or all(sub[i] > sub[i+1] for i in range(len(sub) - 1))

def safe_count_lists(sub):
	for i in range(0, len(sub)-1):
		if steady_check(sub):
			if abs(sub[i]-sub[i+1]) >= 1 and abs(sub[i]-sub[i+1]) <= 3:
				continue
			else:
				return False
			
			
		else:
			return False
	return True

safecount = 0

for sub in mainlist:
	if safe_count_lists(sub) is True:
		safecount += 1

print(safecount)
recount = 0
def errorcheck(sublist):
	for i in range(len(sublist)):
		new_sub_list = sublist[:i] + sublist[i+1:]
		if safe_count_lists(new_sub_list):
			return True
	return False
for sub in mainlist:
	print(errorcheck(sub))
	if errorcheck(sub) is True:
		recount +=1
print(recount)
