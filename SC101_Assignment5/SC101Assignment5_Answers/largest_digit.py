"""
File: largest_digit.py
Name: Rebecca
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n, max_dig=None):
	"""
	:param n: int, the number given in the question
	:param max_dig: int, track the largest digit found during recursion
	:return: int, the largest digit in the absolute value of 'n'
	"""
	# Convert n to a positive number if it is negative
	if n < 0:
		n = -n

	# Initialize max_dig with the last digit of n if max_dig is None
	if max_dig is None:
		max_dig = n % 10

	# Base case: if n is a single digit, return the larger one
	if n < 10:
		return max(n, max_dig)

	# Recursive case: compare max_dig with the last digit of n
	else:
		return find_largest_digit(n//10, max(max_dig, n % 10))


if __name__ == '__main__':
	main()



