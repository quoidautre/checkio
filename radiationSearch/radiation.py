
class Node():
	def __init__(self, value):
		self.value = value
		self.neighbours = []

def checkio(arr):
	uncheckedNodes = []
	nodes = []

	for x in range(5):
		row = []
		for y in range(5):
			node = Node(arr[x][y])
			uncheckedNodes.append(node)
			row.append(node)

		nodes.append(row)

	for x in range(5):
		for y in range(5):
			if x != 0:
				nodes[x-1][y].neighbours.append(nodes[x][y])
				nodes[x][y].neighbours.append(nodes[x-1][y])
			if x != 4:
				nodes[x+1][y].neighbours.append(nodes[x][y])
				nodes[x][y].neighbours.append(nodes[x+1][y])
			if y != 0:
				nodes[x][y-1].neighbours.append(nodes[x][y])
				nodes[x][y].neighbours.append(nodes[x][y-1])
			if y != 4:
				nodes[x][y+1].neighbours.append(nodes[x][y])
				nodes[x][y].neighbours.append(nodes[x][y+1])

	stack = []
	while len(uncheckedNodes) != 0:
		if len(stack) > 0:
			node = stack.pop()
		else:
			node = uncheckedNodes.pop()

		print filter(lambda x: node.value == x, node.neighbours)

if __name__ == '__main__':
	assert checkio([
		[1,2,3,4,5],
		[1,1,1,2,3],
		[1,1,1,2,2],
		[1,2,2,2,1],
		[1,1,1,1,1]
		]) == [14,1]
