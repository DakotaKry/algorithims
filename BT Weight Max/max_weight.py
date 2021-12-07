class MaxWeight():
	S = []
	def __init__(self, T):
		self.S = T # Init Solution Tree
		print(self.S)

	def maxWeight(self):
		S = self.S
		print(self.S)
		n = len(S)
		
		i = n-1
		while ( i >= 1 ):
			print(i)
			if ( (i % 2) == 0 ): # Two leafs
				print (str(S[i]) + " + " + str(S[i-1]) + " : " + str( S[ int( i/2 )-1 ]))
				if (S[i] + S[i-1] <= S[ int(i/2) -1 ]):	
					S.pop(i)
					S.pop(i-1)
					print("popped")

				else:
					S[ int( i/2 ) - 1 ] = S[i] + S[i-1]

				i = i-2 # Go to next leafs

			else:
				if( S[i] <= S[ int( (i-1)/2)-1 ] ):
					S.pop(i)
				else:
					S[ int((i-1)/2) -1 ] = S[i]
				i = i-1
			print(S)

		return S[0]

	def solution(self):
		S = self.S
		print(S)
		A = []
		allLeaves = False

		for i in range(len(S)-1, 0-1, -1):
			print(S[i])
			if ( S[i] != None ):
				if ( 2*(i+1)-1 >= len(S) ):
					# i is leaf
					A.extend([S[i]])
				elif ( S[2*(i+1)-1] == None ):
					A.extend([S[i]])
				else:
					break
					
		return A

	def getSolution(self):
		sol = self.maxWeight()
		leafs = self.solution()

		print( str(sol) + " : " + str(leafs) )


I = []
for i in range(20):
	if ((i+1)%2==0):
		I.extend([2*(20 - (i+1) + 1) + 1 ])
	else:
		I.extend([2*(20-(i+1)+1)])
print(I)

IWeight = MaxWeight(I)
IWeight.getSolution()











