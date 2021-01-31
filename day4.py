import re

def get_doc(a):
	return re.split('[ \n]', a)

def get_fields(b):
	new_dict = {}
	for i in b:
		pair = i.split(':')
		new_dict[pair[0]] = pair[1]
	return new_dict

docs = list(map(get_fields, map(get_doc, open('input4.txt').read().split('\n\n'))))

def part1():
	valids = 0
	for doc in docs:
		if len(doc) == 8:
			valids += 1
		elif len(doc) == 7:
			if 'cid' not in doc:
				valids += 1

	return valids

def part2():
	valids = 0
	for doc in docs:
		if len(doc) == 8:
			valids += 1
		elif len(doc) == 7:
			if 'cid' not in doc:
				valids += 1

	return valids

if __name__ == "__main__":
	print(part1())
	print(part2())
