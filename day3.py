le_map = open('input3.txt').read().splitlines()

def count_trees(slope):
	row_len = len(le_map[0])
	row, pos = 0, 0
	trees = 0

	while row < len(le_map):
		if le_map[row][pos] == '#':
			trees += 1
		pos = (pos+slope[0]) % row_len
		row += slope[1]
		
	return trees

def part1():
	return count_trees([3,1])

def part2():
	slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
	total_trees = 1
	for slope in slopes:
		total_trees *= count_trees(slope)
	return total_trees

if __name__ == "__main__":
	print(part1())
	print(part2())