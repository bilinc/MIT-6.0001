# Problem Set 4A
# Name: Bilin Chen
# Collaborators: None
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

	if len(sequence) == 1:
		# base case
		permutations = []
		permutations.append(sequence)
		
		return permutations

	else:
		first_character = sequence[0]
		rest_characters = sequence[1:]

		permutations = get_permutations(rest_characters)

		new_permutations = []

		for term in permutations:
			for i in range(len(term)+1):
				new_term = term[:i] + first_character + term[i:]

				new_permutations.append(new_term)

		return new_permutations


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
	
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
	
	print('========', 'Test 1', '========')
	test1 = 'a'
	print('Input:', test1)
	print('Expected Output:', ['a'])
	print('Actual Output', get_permutations(test1))
	print()

	print('========', 'Test 2', '========')
	test2 = 'abc'
	print('Input:', test2)
	print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
	print('Actual Output', get_permutations(test2))
	print()

	print('========', 'Test 3', '========')
	test3 = 'xyz'
	print('Input:', test3)
	print('Expected Output:', ['xyz', 'yxz', 'yzx', 'xzy', 'zxy', 'zyx'])
	print('Actual Output', get_permutations(test3))
	print()
	
	print(get_permutations('abcd'))
