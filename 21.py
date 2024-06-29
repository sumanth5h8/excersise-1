# Python 3 implementation of the approach
import sys

# Utility function to print the 
# contents of the array
def printArr(b, n):
	for i in range(0, n, 1):
		print(b[i], end = " ")

# Function to build array B[]
def ModifiedArray(a, n):
	
	# Lower and upper limits
	l = 0
	r = sys.maxsize

	# To store the required array
	b = [0 for i in range(n)] 

	# Apply greedy approach
	for i in range(0, int(n / 2), 1):
		b[i] = max(l, a[i] - r)
		b[n - i - 1] = a[i] - b[i]
		l = b[i]
		r = b[n - i - 1]

	# Print the built array b[]
	printArr(b, n)

# Driver code
if __name__ == '__main__':
	a = [5, 6]
	n = len(a)
	ModifiedArray(a, 2 * n)

# This code is contributed by
# Shashank_Sharma
