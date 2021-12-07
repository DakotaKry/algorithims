def qs(a, start, end):
	less = start
	more = start + 1
	pivot = end

	#       | more
	#	[0, 1, 2, . . . , n - 1, n]  Where this can be any partition from start to end
	#	 | less			   pivot |
	# left of less if less than pivot. less to more if more than pivot. pivot is at end

	if ( (end - start) > 0): # If list  <= 1, then it's sorted

		for index in range(start,end):
			if (a[index] < a[pivot]):

				# swap
				a[less], a[index] = a[index], a[less]

				# move both partitions up one as element was added to less
				less += 1
				more += 1

			elif ( a[index] >= a[pivot] ):

				# move more partition up one as element was added to more
				more += 1
	

		# Swap the pivot between less and more so it is sorted
		a[less], a[pivot] = a[pivot], a[less]

		qs(a, start, less - 1) # sort the less partition
		qs(a, less + 1, end) # sort the right partition

def quicksort(a):
	print(a)
	qs(a, 0, len(a) - 1)
	print(a)


a = [1,3,2,8,5,7,9]
quicksort(a)

b = [999,324,1245,432,124,6346,765,1234,7654,34,65,1424,7675,97865,23]
quicksort(b)

