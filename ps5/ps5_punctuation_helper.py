# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Bilin Chen
# Self created helper function
# ---------------------------------
import string

def remove_puncs(text):
	"""
	Strips an input text string of all string punctuations.
	Also makes the string into lowercase.
	"""
	string_temp = ""
	for s in text:
		# if s not in string.punctuation:
		s.strip(string.punctuation)
		string_temp += s.lower()

	return string_temp