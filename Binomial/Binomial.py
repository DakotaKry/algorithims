
class Binomial:

	def __init__(self, xmax, ymax):
		self.A = [ [None] * ymax for i in range(xmax) ]
		self.trace = False

	def setTrace(self, trace):
		self.trace = trace



	def b(self,  x , y ):
		# runs O(x*y) time

		A = self.A
		trace = self.trace

		for i in range ( x ):
			for j in range ( y ):
				if ( A[i][j] != None ):
					if (trace):
						continue
					
				elif ( i == 0 or j == 0 ):
					A[i][j] = 1;
					if (trace):
						print(1)
					
				else:
					A[i][j] = A[i-1][j] + A[i][j-1]
					if (trace):
						print(A[i][j])

		if (self.trace):
			print("="*5 + str(A[x-1][y-1]) + "="*5)
		return A[x][y]

	def fastRoute(self, xsrc, ysrc, xdest, ydest ):
		x = abs( xsrc - xdest )
		y = abs( ysrc - ydest )

		return self.b( x, y )

	def updateMax(self, xmax, ymax ):
		# Runs O(xmax*ymax) time

		B = [None] * xmax
		for i in range(xmax):
			Y = [None] * ymax
			for j in range(ymax):
				Y[j] + A[i][j]
		B[i] = Y 
		self.A = B
			
binom = Binomial(20,20)
binom.setTrace(True)
binom.fastRoute(1, 1, 8, 4)
