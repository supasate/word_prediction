#######################################
#  Author: Supasate Choochaisri       #
#  Contact: supasate@larngeartech.com #
#  License: GNU GPL                   #
#######################################
import curses

# Add key (word) and next_word into corpus_index 
def add_to_corpus_index(key, next_word, corpus_index):
	# Check that current word already exists or not
	if key not in corpus_index: # if this is a new word, add the next word and start counting
		corpus_index[key] = {next_word: 1}
	else: # if this word already exists
		# Check that next word is new for this current word or not
		if next_word in corpus_index[key]: # If not new, increment counting
			corpus_index[key][next_word] += 1
		else: # If new, start counting
			corpus_index[key][next_word] = 1

# Init corpus statistics
def init_corpus_stats(corpus_index, corpus):
	splitted_text = corpus.split()
	for i in range(len(splitted_text) - 1):
		word, next_word = splitted_text[i], splitted_text[i + 1]
		add_to_corpus_index(word, next_word, corpus_index)

# Predict next word based on current word
def predict(word, corpus_stats):
	if word in corpus_stats:
		return max(corpus_stats[word], key=corpus_stats[word].get)
	else:		
		return ""

# Initialize corpus from a file
def load_corpus(file_name):
	corpus = ""
	with open(file_name, "r") as corpus_file:
		corpus = corpus_file.read()
	return corpus	

corpus = load_corpus("corpus.txt")
corpus_stats = {}
init_corpus_stats(corpus_stats, corpus)

screen = curses.initscr()
curses.noecho()
text_buffer = ''

while True:
	c = screen.getkey()

	if ord(c) == 27:
		break 
	elif c == '\t':
		last_word_begin = text_buffer.strip().rfind(' ') + 1
		last_word = text_buffer[last_word_begin: ].strip()
		next_word = predict(last_word, corpus_stats)
		screen.addstr(' ' + next_word)
		text_buffer = next_word
	else:	
		screen.addch(c)
		text_buffer += c