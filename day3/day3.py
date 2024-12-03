import re

#works for part 1 and 2, just need to comment out one line

pattern = r'mul\((\d+),(\d+)\)'
start = r"do\(\)"
stop = r"don\'t\(\)"
accepting = True
buffer = ""
list_of_muls= []
accepting = True
with open("input.txt", "r") as file:
	while True:
		c=file.read(1)
		buffer += c
		if accepting is True:
			check = re.search(pattern, buffer)
			if check:
				list_of_muls.append(check.group(0))
				buffer = ""
			match = re.search(stop, buffer)
			if match:
				#comment out this next line for part 1
				accepting = False
				buffer = ""
				
		if accepting is False:
			match = re.search(start, buffer)
			if match:
				buffer = ""
				accepting = True
				
		if not c:
			break

valid_ints = []
for item in list_of_muls:
	match = re.search(pattern, item.strip())
	if match:
		x,y = map(int, match.groups())
		z = x * y
		valid_ints.append(z)
sum = 0
for i in valid_ints:
	sum = i + sum
print(sum)
