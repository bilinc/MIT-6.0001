# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print("\nLoading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist



def choose_word(wordlist):
	"""
	wordlist (list): list of words (strings)
	
	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing; assumes all letters are
	  lowercase
	letters_guessed: list (of letters), which letters have been guessed so far;
	  assumes that all letters are lowercase
	returns: boolean, True if all the letters of secret_word are in letters_guessed;
	  False otherwise
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"

	secret_letters = list(secret_word)
	
	if set(secret_letters).issubset(letters_guessed):
		return True
	else:
		return False

#word = 'apple'
#guess = ['e', 'i', 'a', 'p', 's', 'a', 'l']
#
#print(is_word_guessed(word, guess))



def get_guessed_word(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string, comprised of letters, underscores (_), and spaces that represents
	  which letters in secret_word have been guessed so far.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	
	secret_letters = list(secret_word)
	result = ''
	for char in secret_letters:
		if char in letters_guessed:
			result += ' ' + char
			
		else:
			result += ' _'

	return result


# word = 'apple'
# guess = ['e', 'i', 'k', 'r', 's', 'a', 'p']

# print(get_guessed_word(word, guess))

def get_available_letters(letters_guessed):
	'''
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string (of letters), comprised of letters that represents which letters have not
	  yet been guessed.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	all_letters = list(string.ascii_lowercase)

	for i, letter in enumerate(letters_guessed):
		for j, char in enumerate(all_letters): 
			if letter == char:
				all_letters.pop(j)

	return ' '.join(all_letters)

#guess = ['e', 'i', 'k', 'r', 's', 'a', 'p']
#
#print(get_available_letters(guess))


def hangman(secret_word):
	'''
	secret_word: string, the secret word to guess.
	
	Starts up an interactive game of Hangman.
	
	* At the start of the game, let the user know how many 
	  letters the secret_word contains and how many guesses s/he starts with.
	  
	* The user should start with 6 guesses

	* Before each round, you should display to the user how many guesses
	  s/he has left and the letters that the user has not yet guessed.
	
	* Ask the user to supply one guess per round. Remember to make
	  sure that the user puts in a letter!
	
	* The user should receive feedback immediately after each guess 
	  about whether their guess appears in the computer's word.

	* After each guess, you should display to the user the 
	  partially guessed word so far.
	
	Follows the other limitations detailed in the problem write-up.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	word = secret_word
	number_of_guesses = 6
	warnings = 3
	vowel = 'aeiou'
	
	print('\n~~~~~~~~The World of Hangman~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('Welcome to the beautiful world of Hangman!')
	print("You know the drill. I'm thinking of a word and you have to guess it. Or the fat man hangs...")
	print(f'The word is {len(word)} letters long.')
	print('------------------')
	
	guessed_letters = []
	
	while number_of_guesses > 0 and not(is_word_guessed(word, guessed_letters)):
		print('You have %s gueses left.' % (number_of_guesses))
		print('You have %s warnings left.' % (warnings))
		
		print('Available letter: %s' % (get_available_letters(guessed_letters)))
		
		guess = input('Please guess a letter: ').lower()
		guessed_letters.append(guess)
		
		# Check if the word is a letter	
		if guess.isalpha():
			if guess in word:
				print(f'Good guess! {get_guessed_word(word, guessed_letters)}')
			else:
				# If the guess is a vowel, lose 2 guesses
				if guess in vowel:
					print(f'Ops! That letter is not in my word: {get_guessed_word(word, guessed_letters)}')
					number_of_guesses -= 2
				# If the guess is a consonant, lose 1 guess
				else:
					print(f'Ops! That letter is not in my word: {get_guessed_word(word, guessed_letters)}')
					number_of_guesses -= 1
			print('------------------')
	
		# If the word is not a letter the player gets a warning
		else:
			if number_of_guesses <= 1:
				number_of_guesses -= 1
				print('You lose. The fat man hangs.')
			elif warnings == 0:
				number_of_guesses -= 1
				print('Opsie! Please type a letter.')
			else:
				print('Opsie! Please type a letter.')
				warnings -= 1
	
	if is_word_guessed(word, guessed_letters):
		print('Congratulations, you saved him!')
		print('Your total score is: %d' % (number_of_guesses * len(set(word))))
	
	else:
		print('You lost, the fat man hangs! The correct word was "%s".' % (word))


#hangman('poo')

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
	'''
	my_word: string with _ characters, current guess of secret word
	other_word: string, regular English word
	returns: boolean, True if all the actual letters of my_word match the 
		corresponding letters of other_word, or the letter is the special symbol
		_ , and my_word and other_word are of the same length;
		False otherwise: 
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	
	# Remove blankspace in the guessed word
	my_word = my_word.replace(" ", "")
	
	if len(my_word) == len(other_word):
		for i in range(len(my_word)):
			if my_word[i] == "_":
				pass
			elif my_word[i] == other_word[i]:
				pass
			else:
				return False
		return True
	else:
		return False

#print(match_with_gaps("a_ _ le", "apple"))



def show_possible_matches(my_word):
	'''
	my_word: string with _ characters, current guess of secret word
	returns: nothing, but should print out every word in wordlist that matches my_word
			 Keep in mind that in hangman when a letter is guessed, all the positions
			 at which that letter occurs in the secret word are revealed.
			 Therefore, the hidden letter(_ ) cannot be one of the letters in the word
			 that has already been revealed.

	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	
	my_word = my_word.replace(" ", "")
	hints = []
	
	for word in wordlist:
		if match_with_gaps(my_word, word):
			hints.append(word)
	
	hints_str = " ".join(hints)
	if len(hints) > 0:
		print("\nSo you've asked for a hint ey? Just because I'm so kind I will give it to you.")
		print('Possible matches: \n{}\n'.format(hints_str))
	else:
		print('No matches found.')

show_possible_matches('t_ t')



def hangman_with_hints(secret_word):
	'''
	secret_word: string, the secret word to guess.
	
	Starts up an interactive game of Hangman.
	
	* At the start of the game, let the user know how many 
	  letters the secret_word contains and how many guesses s/he starts with.
	  
	* The user should start with 6 guesses
	
	* Before each round, you should display to the user how many guesses
	  s/he has left and the letters that the user has not yet guessed.
	
	* Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
	  
	* The user should receive feedback immediately after each guess 
	  about whether their guess appears in the computer's word.

	* After each guess, you should display to the user the 
	  partially guessed word so far.
	  
	* If the guess is the symbol *, print out all words in wordlist that
	  matches the current guessed word. 
	
	Follows the other limitations detailed in the problem write-up.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"

	word = secret_word
	number_of_guesses = 6
	warnings = 3
	vowel = 'aeiou'
	
	print('\n~~~~~~~~The World of Hangman~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('Welcome to the beautiful world of Hangman!')
	print("You know the drill. I'm thinking of a word and you have to guess it. Or the fat man hangs...")
	print(f'The word is {len(word)} letters long.')
	print('------------------')
	
	guessed_letters = []
	
	while number_of_guesses > 0 and not(is_word_guessed(word, guessed_letters)):
		print('You have %s gueses left.' % (number_of_guesses))
		print('You have %s warnings left.' % (warnings))
		
		print('Available letter: %s' % (get_available_letters(guessed_letters)))
		
		guess = input('Please guess a letter: ').lower()
		guessed_letters.append(guess)
		
		# Check if the word is a letter	
		if guess.isalpha():
			if guess in word:
				print(f'Good guess! {get_guessed_word(word, guessed_letters)}')
			else:
				# If the guess is a vowel, lose 2 guesses
				if guess in vowel:
					print(f'Ops! That letter is not in my word: {get_guessed_word(word, guessed_letters)}')
					number_of_guesses -= 2
				# If the guess is a consonant, lose 1 guess
				else:
					print(f'Ops! That letter is not in my word: {get_guessed_word(word, guessed_letters)}')
					number_of_guesses -= 1
			print('------------------')
		
		# Give a hint if the user asks for it
		elif guess == '*':
			show_possible_matches(get_guessed_word(word, guessed_letters))
		
		# If the word is not a letter the player gets a warning
		else:
			if number_of_guesses <= 1:
				number_of_guesses -= 1
				print('You lose. The fat man hangs.')
			elif warnings == 0:
				number_of_guesses -= 1
				print('Opsie! Please type a letter.')
			else:
				print('Opsie! Please type a letter.')
				warnings -= 1
	
	if is_word_guessed(word, guessed_letters):
		print('Congratulations, you saved him!')
		print('Your total score is: %d' % (number_of_guesses * len(set(word))))
	
	else:
		print('You lost, the fat man hangs! The correct word was "%s".' % (word))
		

#hangman_with_hints('tact')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#	pass

	# To test part 2, comment out the pass line above and
	# uncomment the following two lines.
	
#	secret_word = choose_word(wordlist)
#	hangman(secret_word)

###############
	
	# To test part 3 re-comment out the above lines and 
	# uncomment the following two lines. 
	
	secret_word = choose_word(wordlist)
	hangman_with_hints(secret_word)
