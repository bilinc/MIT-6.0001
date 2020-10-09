# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
	'''
	Enumerate all permutations of a given string

	sequence (string): an arbitrary string to permute. Assume that it is a
	non-empty string.  

	You MUST use recursion for this part. Non-recursive solutions will not be
	accepted.

	Returns: a list of all permutations of sequence

	Example:
	>>> get_permutations('abc')
	['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

	Note: depending on your implementation, you may return the permutations in
	a different order than what is listed here.
	'''
	def get_permutations_helper(some_list):
		permu = []

		for item in some_list:
			for i in range(len(item)+1):
				if len(item) == 1:	# base case
					print('item:', item)
					print()
					permu.append(item)
					return permu
				else:				# recursion attempt
					sliced_letter = item[0]
					the_rest = get_permuations_help(list(item[1:])) # item[1:]
					
					foo = the_rest[:i] + sliced_letter + the_rest[i:]
					permu.append(foo)
					
					return get_permutations_helper(permu)
	
	permutations = []
	if len(sequence) == 1:
		# base case
		# permutations.append(sequence)
		return sequence

	else:

		return get_permutations_helper(list(sequence))

	# elif len(sequence) == 2:
	# 	first = sequence[0]
	# 	piece = sequence[1:]

	# 	for i in range(len(piece)+1):
	# 		foo = piece[:i] + first + piece[i:]
	# 		permutations.append(foo)
	# 		# print(foo)
			
	# 		# print()
	# 	print(permutations)

	# else:
	# 	for items in 




if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
	
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

	# test1 = 'a'
	# print('Input:', test1)
	# print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
	# print('Actual Output', get_permutations(test1))

	print(get_permutations('abc'))

