# Problem Set 4C
# Name: Bilin Chen
# Collaborators: None
# Time Spent: x:xx

import string
from ps4a import get_permutations

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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
	def __init__(self, text):
		'''
		Initializes a SubMessage object
				
		text (string): the message's text

		A SubMessage object has two attributes:
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
				
	def build_transpose_dict(self, vowels_permutation):
		'''
		vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
		
		Creates a dictionary that can be used to apply a cipher to a letter.
		The dictionary maps every uppercase and lowercase letter to an
		uppercase and lowercase letter, respectively. Vowels are shuffled 
		according to vowels_permutation. The first letter in vowels_permutation 
		corresponds to a, the second to e, and so on in the order a, e, i, o, u.
		The consonants remain the same. The dictionary should have 52 
		keys of all the uppercase letters and all the lowercase letters.

		Example: When input "eaiuo":
		Mapping is a->e, e->a, i->i, o->u, u->o
		and "Hello World!" maps to "Hallu Wurld!"

		Returns: a dictionary mapping a letter (string) to 
				 another letter (string). 
		'''
		
		self.vowels_permutation = vowels_permutation
		self.dict_cipher = {}
		
		for i, vl in enumerate(VOWELS_LOWER):
			self.dict_cipher[vl] = self.vowels_permutation[i]
			self.dict_cipher[vl.upper()] = self.vowels_permutation[i].upper()

		for cons in CONSONANTS_LOWER:
			self.dict_cipher[cons] = cons
			self.dict_cipher[cons.upper()] = cons.upper()
		
		return self.dict_cipher

	def apply_transpose(self, transpose_dict):
		'''
		transpose_dict (dict): a transpose dictionary
		
		Returns: an encrypted version of the message text, based 
		on the dictionary
		'''
		self.transpose_dict = transpose_dict
		self.encrypted_message = ''

		for letter in self.message_text:
			# check the letter is alphabet and not other character
			if letter.isalpha():
				self.encrypted_message += self.transpose_dict[letter]
			else:
				self.encrypted_message += letter

		return self.encrypted_message

		
class EncryptedSubMessage(SubMessage):
	def __init__(self, text):
		'''
		Initializes an EncryptedSubMessage object

		text (string): the encrypted message text

		An EncryptedSubMessage object inherits from SubMessage and has two attributes:
			self.message_text (string, determined by input text)
			self.valid_words (list, determined using helper function load_words)
		'''
		SubMessage.__init__(self, text)

	def decrypt_message(self):
		'''
		Attempt to decrypt the encrypted message 
		
		Idea is to go through each permutation of the vowels and test it
		on the encrypted message. For each permutation, check how many
		words in the decrypted text are valid English words, and return
		the decrypted message with the most English words.
		
		If no good permutations are found (i.e. no permutations result in 
		at least 1 valid word), return the original string. If there are
		multiple permutations that yield the maximum number of words, return any
		one of them.

		Returns: the best decrypted message    
		
		Hint: use your function from Part 4A
		'''
		
		# get the permutations for the vowels
		self.VOWELS_PERMUTATIONS_LOWER = get_permutations(VOWELS_LOWER)
		# self.VOWELS_PERMUTATIONS_UPPER = get_permutations(VOWELS_UPPER)
		
		# total number of valid words, the associated permutation, and the string
		self.total_valid_words = 0
		# use each permutation as a cipher
		for permutation in self.VOWELS_PERMUTATIONS_LOWER:
			self.cipher = self.build_transpose_dict(permutation)
			# get the deciphered message as a string, then splits it for each word into a list
			self.decipher_msg = self.apply_transpose(self.cipher)
			self.decrypted_msg_list = self.decipher_msg.split(
				)
			# try each cipher on the words in the ciphertext
			self.valid_word_count = 0
			for word in self.decrypted_msg_list:
				# check the word to see if it's valid
				if is_word(self.get_valid_words(), word):
					self.valid_word_count += 1

			if self.total_valid_words < self.valid_word_count:
				self.total_valid_words = self.valid_word_count
				self.decipher_msg_best = self.decipher_msg
				self.best_cipher = permutation

		# if no good cipher exist, return the original string
		if self.total_valid_words == 0:
			return self.message_text
		# return the cipher that gives the maximum number of valid words
		else:
			return (self.total_valid_words, self.best_cipher, self.decipher_msg_best)


	

if __name__ == '__main__':

	# # Example test case
	# message = SubMessage("Hello World!")
	# permutation = "eaiuo"
	# enc_dict = message.build_transpose_dict(permutation)
	# # print(len(message.build_transpose_dict(permutation)))

	# print("Original message:", message.get_message_text(), "Permutation:", permutation)
	# print("Expected encryption:", "Hallu Wurld!")
	# print("Actual encryption:", message.apply_transpose(enc_dict))
	# enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
	# print("Decrypted message:", enc_message.decrypt_message())
	 
	#TODO: WRITE YOUR TEST CASES HERE
	
	# print("\nTesting SubMessage...\n", "Test 1")
	# message_test1 = SubMessage("I love to program and code!")
	# permutation = "oiuae"
	# enc_dict = message_test1.build_transpose_dict(permutation)
	# print("Original message:", message_test1.get_message_text(), "Permutation:", permutation)
	# print("Expected encryption:", "U lavi ta pragrom ond cadi!")
	# print("Actual encryption:", message_test1.apply_transpose(enc_dict))


	# Test EncryptedSubMessage
	message_test2 = SubMessage('''Akira Tachibana, a reserved high school student and former track runner, has not been able to race the same as she used to since she experienced a severe foot injury. And although she is regarded as attractive by her classmates, she is not interested in the boys around school.''')
	permutation = "oiuae"
	enc_dict = message_test2.build_transpose_dict(permutation)
	print("Original message:", message_test2.get_message_text(), "Permutation:", permutation)
	# print("Expected encryption:", "U lavi ta pragrom ond cadi!")
	print("\nEncrypted Message:", message_test2.apply_transpose(enc_dict))

	msg_string = '''Okuro Tochubono, o risirvid hugh schaal stedint ond farmir trock rennir, hos nat biin obli ta roci thi somi os shi esid ta sunci shi ixpiruincid o siviri faat unjery. Ond olthaegh shi us rigordid os ottroctuvi by hir clossmotis, shi us nat untiristid un thi bays oraend schaal.'''
	print()
	print('Decrypting message...')
	print()
	decrypted_msg = EncryptedSubMessage(msg_string)
	nr_valid_words, cipher_permutation, msg = decrypted_msg.decrypt_message()
	print('Number of valid words: %d\nPermutation: %s\nThe deciphered message:\n%s' % (nr_valid_words, cipher_permutation, msg))
