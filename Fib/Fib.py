sol = [0,1]
disBS = False

def disG(n: int):

	print( "Sequence number " + str(n) + " is " + str(get(n)) )

def disS(n: int):

	print( str(n) + " is sequence " + str(search(n)) )


def solT():
	print( "Solution Table: \n" + "\t" + str(sol) )



def get(n: int) -> int:
	if(len(sol) - 1 >= n):
		# Then we have the solution
		return sol[n]
	else:
		# We must find the solution
		sol.append( get(n-1) + get(n-2))
		return sol[n]
	
def search(n: int) -> int:
	size = len(sol) - 1

	try:
		if(sol[size] <= n):
			# We must find the solution
			while(sol[size] < n):
				# We get the next fib number until we calculate it
				print("sol: " + str(sol[size]) + " | n: " + str(n) )
				print(get(size + 1))
				size += 1

			if (sol[-1] == n):
				return len(sol) - 1
			else:
				# Invalid Fib number
				raise Exception("Invalid Fib Number")
		else:
			val = bs(n)
			return val
	except Exception as e:
		print(str(e) + ": " + str(n))
	else:
		return None

def bs(n: int) -> int:
	size = len(sol)
	c = 0
	midP = 0
	mid = int(size/2)

	while True:

		if (disBS):
			print("mid: " + str(mid) 
					+ " | midP: " + str(midP)
					+ " | diff: " + str(abs(mid-midP))
					+ " | c: " + str(c)
					+ " | n: " + str(n))

		c = sol[mid]
	
		if (c == n):
			return mid
		elif (c < n):
			print(mid)
			mid = mid + int(abs(mid-midP)/2)
			print(mid)
			print(midP)
		else:
			mid = mid - int(abs(mid-midP)/2)
		
		if ( midP == mid or mid < 0 or mid >= size):
			# invalid value
			raise Exception("Invalid Fib Number")

		midP = mid
		
	raise Exception("Invalid Fib Number")

def getS(n: int) -> int:

	if(len(sol) - 1 >= n):
		# Then we have the solution
		return sol[n]

	
	if(n <= 0):
		return 0
	elif(n == 1):
		return 1
	else:

		a = sol[-2]
		b = sol[-1]

		for i in range (len(sol) - 1,n):

			c = a + b
			a = b
			b = c

		return c	


