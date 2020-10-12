# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
	'''
	file_name (string): the name of the file containing 
	the list of words to load    
	
	Returns: a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	'''

	# print("Loading word list from file...")
	# inFile: file
	inFile = open(file_name, 'r')
	# wordlist: list of strings
	wordlist = []
	for line in inFile:
		wordlist.extend([word.lower() for word in line.split(' ')])
	# print("  ", len(wordlist), "words loaded.")
	return wordlist

def is_word(word_list, word):
	'''
	Determines if word is a valid word, ignoring
	capitalization and punctuation

	word_list (list): list of words in the dictionary.
	word (string): a possible word.
	
	Returns: True if word is in word_list, False otherwise

	Example:
	>>> is_word(word_list, 'bat') returns
	True
	>>> is_word(word_list, 'asdf') returns
	False
	'''
	word = word.lower()
	word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
	return word in word_list

def get_story_string():
	"""
	Returns: a story in encrypted text.
	"""
	f = open("story.txt", "r")
	story = str(f.read())
	f.close()
	return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
	def __init__(self, text):
		'''
		Initializes a Message object
				
		text (string): the message's text

		a Message object has two attributes:
			self.message_text (string, determined by input text)
			self.valid_words (list, determined using helper function load_words)
		'''
		self.message_text = text
		self.valid_words = load_words(WORDLIST_FILENAME)

		


	def get_message_text(self):
		'''
		Used to safely access self.message_text outside of the class
		
		Returns: self.message_text
		'''
		return self.message_text

	def get_valid_words(self):
		'''
		Used to safely access a copy of self.valid_words outside of the class.
		This helps you avoid accidentally mutating class attributes.
		
		Returns: a COPY of self.valid_words
		'''
		self.valid_words_copy = self.valid_words.copy()

		return self.valid_words_copy

	def build_shift_dict(self, shift):
		'''
		Creates a dictionary that can be used to apply a cipher to a letter.
		The dictionary maps every uppercase and lowercase letter to a
		character shifted down the alphabet by the input shift. The dictionary
		should have 52 keys of all the uppercase letters and all the lowercase
		letters only.        
		
		shift (integer): the amount by which to shift every letter of the 
		alphabet. 0 <= shift < 26

		Returns: a dictionary mapping a letter (string) to 
				 another letter (string). 
		'''
		self.alpha = 'abcdefghijklmnopqrstuvwxyz'
		self.ALPHA = self.alpha.upper()
		

		self.shift_dict = {}

		# every letter in alpha should be shifted with the specified amount        

		# the dict key should be the original letter, the dict value should be the shifted letter
		for letter in self.alpha:
			try:
				self.shift_dict[letter] = self.alpha[self.alpha.index(letter) + shift]
		
			# if the shift takes the letter 'beyond' the alphabet, it shall start again from the beginning    
			except IndexError:
				self.shift_dict[letter] = self.alpha[(self.alpha.index(letter) + shift) - 26]

		for letter in self.ALPHA:
			try:
				self.shift_dict[letter] = self.ALPHA[self.ALPHA.index(letter) + shift]
			
			# if the shift takes the letter 'beyond' the alphabet, it shall start again from the beginning
			except IndexError:
				self.shift_dict[letter] = self.ALPHA[(self.ALPHA.index(letter) + shift) - 26]


		return self.shift_dict

	def apply_shift(self, shift):
		'''
		Applies the Caesar Cipher to self.message_text with the input shift.
		Creates a new string that is self.message_text shifted down the
		alphabet by some number of characters determined by the input shift        
		
		shift (integer): the shift with which to encrypt the message.
		0 <= shift < 26

		Returns: the message text (string) in which every character is shifted
			 down the alphabet by the input shift
		'''
		self.cipher_text = ''

		# dict containing the shifted letters
		self.applied_shift = self.build_shift_dict(shift)

		for letter in self.message_text:
			if letter.isalpha():
				self.cipher_text += self.applied_shift[letter]

			else:
				self.cipher_text += letter

		return self.cipher_text


class PlaintextMessage(Message):
	def __init__(self, text, shift):
		'''
		Initializes a PlaintextMessage object        
		
		text (string): the message's text
		shift (integer): the shift associated with this message

		A PlaintextMessage object inherits from Message and has five attributes:
			self.message_text (string, determined by input text)
			self.valid_words (list, determined using helper function load_words)
			self.shift (integer, determined by input shift)
			self.encryption_dict (dictionary, built using shift)
			self.message_text_encrypted (string, created using shift)

		'''
		Message.__init__(self, text)
		# self.valid_words = self.get_valid_words()
		self.shift = shift
		self.encryption_dict = self.build_shift_dict(self.shift)
		self.message_text_encrypted = self.apply_shift(self.shift)

	def get_shift(self):
		'''
		Used to safely access self.shift outside of the class
		
		Returns: self.shift
		'''
		return self.shift

	def get_encryption_dict(self):
		'''
		Used to safely access a copy self.encryption_dict outside of the class
		
		Returns: a COPY of self.encryption_dict
		'''
		
		return self.encryption_dict.copy()

	def get_message_text_encrypted(self):
		'''
		Used to safely access self.message_text_encrypted outside of the class
		
		Returns: self.message_text_encrypted
		'''
		
		return self.message_text_encrypted

	def change_shift(self, shift):
		'''
		Changes self.shift of the PlaintextMessage and updates other 
		attributes determined by shift.        
		
		shift (integer): the new shift that should be associated with this message.
		0 <= shift < 26

		Returns: nothing
		'''
		self.shift = shift
		self.encryption_dict = self.build_shift_dict(self.shift)		# the method self.build_shift_dict() is from the superclass
		self.message_text_encrypted = self.apply_shift(self.shift)		# the method self.apply_shift() is from the superclass


class CiphertextMessage(Message):
	def __init__(self, text):
		'''
		Initializes a CiphertextMessage object
				
		text (string): the message's text

		a CiphertextMessage object has two attributes:
			self.message_text (string, determined by input text)
			self.valid_words (list, determined using helper function load_words)
		'''
		Message.__init__(self, text)
		# self.valid_words = self.get_valid_words()


	def decrypt_message(self):
		'''
		Decrypt self.message_text by trying every possible shift value
		and find the "best" one. We will define "best" as the shift that
		creates the maximum number of real words when we use apply_shift(shift)
		on the message text. If s is the original shift value used to encrypt
		the message, then we would expect 26 - s to be the best shift value 
		for decrypting it.

		Note: if multiple shifts are equally good such that they all create 
		the maximum number of valid words, you may choose any of those shifts 
		(and their corresponding decrypted messages) to return

		Returns: a tuple of the best shift value used to decrypt the message
		and the decrypted message text using that shift value
		'''
		
		
		self.word_count = 0
		# choose a shift

		for s in range(27):
			self.shift = 26 - s
			# create a decipher dict with the shift

			# self.decipher_dict = self.build_shift_dict(self.shift)
			
			# apply the shift to all the letters in the text and store it as a string
			self.message_text_decrypted = self.apply_shift(self.shift)
			self.message_text_decrypted_list = self.message_text_decrypted.split()
			
			# check if the words are valid
			self.valid_word_count = 0
			for word in self.message_text_decrypted_list:
				if is_word(self.valid_words, word):
					self.valid_word_count += 1
			
			if self.valid_word_count > 0 and self.valid_word_count > self.word_count:
				self.word_count = self.valid_word_count
				self.best_shift = self.shift
				self.message_text_decrypted_best = self.message_text_decrypted

		return (self.best_shift, self.message_text_decrypted_best)


		# make a note if all the words are valid
		# the more words that are valid the better, choose the s which gives the most valid words
		# return the s and deciphered text as string



if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

	#TODO: WRITE YOUR TEST CASES HERE

	print('========================')
	print('Testing PlaintextMessage')
	print('========================')

	print('Test 1')
	plain_txt = PlaintextMessage('We love, programing', 3)
	print('Expected output: Zh oryh, surjudplqj')
	print('Actual output:', plain_txt.get_message_text_encrypted())
	print()
	print('Test 2')
	plain_txt = PlaintextMessage('Bilin', 5)
	print('Expected output: Gnqns')
	print('Actual output:', plain_txt.get_message_text_encrypted())
	print()
	print('========================')
	print('Testing CiphertextMessage')
	print('========================')
	print('Test 1')
	cipher_text = CiphertextMessage('Gnqns')
	print('Expected output: (21, Bilin)')
	print('Actual output:', cipher_text.decrypt_message())
	print()
	print('Test 2')
	cipher_text = CiphertextMessage('lipps xlivi!!! Qc- asvPH')
	print('Expected output: (22, hello there!!! My- worLD')
	print('Actual output:', cipher_text.decrypt_message())

	#TODO: best shift value and unencrypted story
	print('\nDecrypting the story...\n')
	cipher_story = CiphertextMessage(get_story_string())
	decrypted = cipher_story.decrypt_message()
	
	print('The best shift value is: %s\n' % decrypted[0])
	print('The story: %s' % decrypted[1])
