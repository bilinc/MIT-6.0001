# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Bilin Chen
# Collaborators: None
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz

from ps5_punctuation_helper import remove_puncs

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
	"""
	Fetches news items from the rss url and parses them.
	Returns a list of NewsStory-s.
	"""
	feed = feedparser.parse(url)
	entries = feed.entries
	ret = []
	for entry in entries:
		guid = entry.guid
		title = translate_html(entry.title)
		link = entry.link
		description = translate_html(entry.description)
		pubdate = translate_html(entry.published)

		try:
			pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
			pubdate.replace(tzinfo=pytz.timezone("GMT"))
		  #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
		  #  pubdate.replace(tzinfo=None)
		except ValueError:
			pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

		newsStory = NewsStory(guid, title, description, link, pubdate)
		ret.append(newsStory)
	return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
	def __init__(self, guid, title, description, link, pubdate):
		self.guid = guid
		self.title = title
		self.description = description
		self.link = link
		self.pubdate = pubdate

	def get_guid(self):
		return self.guid

	def get_title(self):
		return self.title

	def get_description(self):
		return self.description

	def get_link(self):
		return self.link

	def get_pubdate(self):
		return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
	def evaluate(self, story):
		"""
		Returns True if an alert should be generated
		for the given news item, or False otherwise.
		"""
		# DO NOT CHANGE THIS!
		raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
	"""
	Takes in a string phrase as an argument in the class's constructor.
	
	PhraseTrigger has one new method is_phrase_in which takes one string argument. 
	Returns True or False
	"""
	def __init__(self, phrase):
		
		# We may assume that a phrase contains no punctuation
		self.phrase = phrase.lower()


	def is_phrase_in(self, text):
		self.text = text.lower()
		
		for s in self.text:
			if s in string.punctuation:
				self.text = self.text.replace(s, ' ')
		
		self.new_text_list = self.text.split()

		# counts the number of consecutive appearances of the words in phrase in text
		# returns true if the total count is the same as the number of words in phrase
		count = 0
		self.phrase_list = self.phrase.split()

		for i in range(len(self.new_text_list)):			
			if self.new_text_list[i] == self.phrase_list[count]:
				count += 1

				if count == len(self.phrase_list):
					return True
			else:
				count = 0
		return False

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
	def __init__(self, phrase):
		PhraseTrigger.__init__(self, phrase)

	def evaluate(self, story):
		return self.is_phrase_in(story.get_title())

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
	def __init__(self, phrase):
		PhraseTrigger.__init__(self, phrase)

	def evaluate(self, story):
		return self.is_phrase_in(story.get_description())


# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
	def __init__(self, time_trigger):
		"""
		Takes in time as an EST in string format and converts it to a datetime.
		"""
		self.time_trigger = datetime.strptime(time_trigger, '%d %b %Y %H:%M:%S')
		self.time_trigger = self.time_trigger.replace(tzinfo=pytz.timezone("EST"))

# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
	def __init__(self, time_trigger):
		TimeTrigger.__init__(self, time_trigger)

	def evaluate(self, story):
		self.story_pubdate = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

		if self.story_pubdate < self.time_trigger:
			return True
		else:
			return False

class AfterTrigger(TimeTrigger):
	def __init__(self, time_trigger):
		TimeTrigger.__init__(self, time_trigger)

	def evaluate(self, story):
		self.story_pubdate = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
		
		if self.story_pubdate > self.time_trigger:
			return True
		else:
			return False

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
	def __init__(self, other_trigger):
		# Takes another trigger as argument in its constructor
		self.other_trigger = other_trigger

	def evaluate(self, story):
		# returns the not value of the other trigger for a news item 'story'
		return not self.other_trigger.evaluate(story)
		


# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
	def __init__(self, trigger1, trigger2):
		self.trigger1 = trigger1
		self.trigger2 = trigger2

	def evaluate(self, story):
		if self.trigger1.evaluate(story) and self.trigger2.evaluate(story):
			return True
		else:
			return False

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
	def __init__(self, trigger1, trigger2):
		self.trigger1 = trigger1
		self.trigger2 = trigger2

	def evaluate(self, story):
		if self.trigger1.evaluate(story) or self.trigger2.evaluate(story):
			return True
		else:
			return False
#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
	"""
	Takes in a list of NewsStory instances.

	Returns: a list of only the stories for which a trigger in triggerlist fires.
	"""
	# TODO: Problem 10

	stories_triggered = []
	for trigger in triggerlist:
		for story in stories:
			# Checks if a trigger can fire on a story in the list, if it does save the story in a new list
			if trigger.evaluate(story):
				stories_triggered.append(story)

	return stories_triggered



#======================
# User-Specified Triggers
#======================
# Problem 11
# Helper function
def create_trigger(config, trigger_dict):
	"""
	config: a string containing information on how the title should be created
	
	Returns: the requested trigger object
	"""
	config = config.split(',')
	keyword = config[1]	# Second element in the configuration
	type_info = config[2]

	# Now I'm instantiating all classes, and some of them will have incorrect values. I only want to instantiate the right class at the right time.
	keyword_dict = {'TITLE':TitleTrigger(type_info), 'DESCRIPTION':DescriptionTrigger(type_info), 'AFTER':AfterTrigger(type_info), 'BEFORE':BeforeTrigger(type_info), 'NOT':NotTrigger(type_info), 'AND':AndTrigger(trigger_dict[config[2]], trigger_dict[config[3]]), 'OR':OrTrigger(trigger_dict[config[2]], trigger_dict[config[3]])}
	
	trigger = []
	
	if keyword in keyword_dict.keys():
		trigger_object = keyword_dict[keyword]

	return trigger_object

def read_trigger_config(filename):
	"""
	filename: the name of a trigger configuration file

	Returns: a list of trigger objects specified by the trigger configuration
		file.
	"""
	# We give you the code to read in the file and eliminate blank lines and
	# comments. You don't need to know how it works for now!
	trigger_file = open(filename, 'r')
	lines = []
	for line in trigger_file:
		line = line.rstrip()
		if not (len(line) == 0 or line.startswith('//')):
			lines.append(line)

	# TODO: Problem 11
	# line is the list of lines that you need to parse and for which you need
	# to build triggers
	
	# dictionary hint: key: trigger name, value: trigger object
	trigger_name = {}
	triggerlist = []
	for item in lines:
		if item[0] != 'ADD':
			trigger_name[item[0]] = create_trigger(item, trigger_name)
		elif item[0] == 'ADD':
			item = item.split()
			for i in range(len(item[1:])):
				triggerlist.append(item[i])

	print(lines) # for now, print it so you see what it contains!
	print(triggerlist)

	return triggerlist

read_trigger_config('triggers.txt')

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
	# A sample trigger list - you might need to change the phrases to correspond
	# to what is currently in the news
	try:
		t1 = TitleTrigger("election")
		t2 = DescriptionTrigger("Trump")
		t3 = DescriptionTrigger("Clinton")
		t4 = AndTrigger(t2, t3)
		triggerlist = [t1, t4]

		# Problem 11
		# TODO: After implementing read_trigger_config, uncomment this line 
		# triggerlist = read_trigger_config('triggers.txt')
		
		# HELPER CODE - you don't need to understand this!
		# Draws the popup window that displays the filtered stories
		# Retrieves and filters the stories from the RSS feeds
		frame = Frame(master)
		frame.pack(side=BOTTOM)
		scrollbar = Scrollbar(master)
		scrollbar.pack(side=RIGHT,fill=Y)

		t = "Google & Yahoo Top News"
		title = StringVar()
		title.set(t)
		ttl = Label(master, textvariable=title, font=("Helvetica", 18))
		ttl.pack(side=TOP)
		cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
		cont.pack(side=BOTTOM)
		cont.tag_config("title", justify='center')
		button = Button(frame, text="Exit", command=root.destroy)
		button.pack(side=BOTTOM)
		guidShown = []
		def get_cont(newstory):
			if newstory.get_guid() not in guidShown:
				cont.insert(END, newstory.get_title()+"\n", "title")
				cont.insert(END, "\n---------------------------------------------------------------\n", "title")
				cont.insert(END, newstory.get_description())
				cont.insert(END, "\n*********************************************************************\n", "title")
				guidShown.append(newstory.get_guid())

		while True:

			print("Polling . . .", end=' ')
			# Get stories from Google's Top Stories RSS news feed
			stories = process("http://news.google.com/news?output=rss")

			# Get stories from Yahoo's Top Stories RSS news feed
			stories.extend(process("http://news.yahoo.com/rss/topstories"))

			stories = filter_stories(stories, triggerlist)

			list(map(get_cont, stories))
			scrollbar.config(command=cont.yview)


			print("Sleeping...")
			time.sleep(SLEEPTIME)

	except Exception as e:
		print(e)


if __name__ == '__main__':
	root = Tk()
	root.title("Some RSS parser")
	t = threading.Thread(target=main_thread, args=(root,))
	t.start()
	root.mainloop()

