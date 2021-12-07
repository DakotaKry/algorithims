import Fib
import sys

def main():

	args = sys.argv
	args = args[1:]

	if len(args) == 0:
		help()
	else:
		for i in range(len(args)):
			if args[i] == '--help' or args[i] == '--h':
				h()
			elif args[i] == '--dbs':
					# Set disBS to true
					Fib.disBS = true
					i = i+1 # Skip the next arg

			elif args[i] == 'run':
				r()
			else:
				print("Invalid argument passed!")


def h():
	help = """
	 === HELP ===
	
	 Excecution Arguments:

		--help or --h
			Displays this page

		--dbs
			Enables binary search display

		--run or -r
			Runs the command section

	 Commands:

		help
			Displays this page

		get <int>
			gets the fib number of the passed sequence

		search <int>
			gets the sequence number of the passed fib number

		T
			gets the current solution table

		C
			clears the current soltuon table

		exit 
			Exits
	"""

	print(help)

def r():
	cont = True;

	while (cont):
		inp = input("Enter Command: ")

		if (inp[:3] == "get"):
			try:
				n = int(inp[3:])
			except Exception as e:
				print(e)
				r()

			size = len(Fib.sol)
			diff = n - size

			# Prevents stack overflow 
			if ( diff ) > 100:
				if ( diff ) > 100000:
					auth = input("Warning, large values of n can use up large amounts of memory\n enter S to compute space safe\n C to continue\n anything else to cancel\n\n : ")
					if (auth == "S"):
						print(Fib.getS(n))
						continue

					elif (auth == "C"):
						print("\nUser Ctrl+X or Cmnd+X to stop, ps aux to list proccesses, and kill <PID>")
						print("continuing...")

					else:
						continue	

				for i in range (size, n):
					Fib.get(i)
					i = i + 20

		
			print(Fib.get(n))

		elif (inp[:6] == "search"):
			try:
				n = int(inp[6:])
			except Exception as e:
				print(e)
				r()
			print(Fib.search(n))
		
		elif(inp[:4] == "help"):
			h()


		elif (inp[0] == "T"):
			print(Fib.sol)

		elif (inp[0] == "C"):
			Fib.sol = [0,1]
			print(Fib.sol)
		
		if (inp[:4] == "exit"):
			cont = False;
	

main()
