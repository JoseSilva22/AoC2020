import re
pwds = open('input2.txt').read().splitlines()
count = 0

# part 1
for pwd in pwds:
	tokens = pwd.split(' ')
	_min, _max = list(map(int, tokens[0].split('-')))
	matches = len(re.findall(tokens[1][0], tokens[2]))
	if matches >= _min and matches <= _max:
		count+=1

print(count)

# part 2
count = 0
for pwd in pwds:
	tokens = pwd.split(' ')
	pos = list(map(int, tokens[0].split('-')))
	matches = [i for i in pos if tokens[2][i-1] == tokens[1][0]]
	if len(matches) == 1:
		count+=1

print(count)
