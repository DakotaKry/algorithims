
class Node:
	outNodes = [] # These are the nodes it points to
	inNodes = [] # Nodes pointing to it
	val = "" # values just for printing to screen

	# These are both just for printing to screen
	def	__init__(self, val):
		self.val = val


	def __repr__(self):
		return self.val


graph = [] # This is just a list of all nodes in our graph with spacial complexity O(n^2)


# Initalizing a graph for testing
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

# Initalizing the pointers
A.outNodes = [G, F, E, D, C, B]
A.inNodes = []

B.outNodes = [G, F, E, D, C]
B.inNodes = [A]

C.outNodes = [G, F, E, D]
C.inNodes = [B, A]

D.outNodes = [G, F, E]
D.inNodes = [C, B, A]

E.outNodes = [G, F]
E.inNodes = [D, C, B, A]

F.outNodes = [G]
F.inNodes = [A, B, C, D, E]

G.outNodes = []
G.inNodes = [A, B, C, D, E, F]


graph = [G, F, E, D, C, B, A]


# Below is the actual algo
# ------------------------

exclude = [] # global list of proccessed nodes

# Simple algo to concatinate two lists and a pivot
def merg (left, pivot, right):
	return left + [pivot] + right

# main algo, takes a graph as a list of Nodes, and returns a list of Nodes in a hamilton path order
def hamilton(graph):

	if ( len(graph) <= 1): # Base case
		print("base case: " + str(graph))
		return graph
	
	else:

		pivot = graph[0] # arbitrarly chosen to pivot around

		outNodes = pivot.outNodes # split into two sub graphs
		inNodes = pivot.inNodes

		for i in range( len(exclude) ): # Make's sure we are only working with
										# Nodes that we haven't already 'proccessed'
			# try to remove any exlucded nodes	
			try:						
				outNodes.remove(exclude[i]) 
			except:
				pass
			try:
				inNodes.remove(exclude[i])
			except:
				pass

		exclude.append(pivot) # Since we 'proccessed' the pivot, add it to exlcude list
		print("pivot chosen: " + str(pivot))

		left = hamilton(inNodes) # recursivly solve
		right = hamilton(outNodes)

		return merg(left, pivot, right) # return the merged value



def main():
	solution = hamilton(graph)

	print("solution: " + str(solution))

main()
