#######################################
#  Author: Supasate Choochaisri       #
#  Contact: supasate@larngeartech.com #
#  License: GNU GPL                   #
#######################################
import curses

# Initialize corpus statistics for prediction
def init_bigram_stats(corpus_stats):
	# Read corpus file and split each word
	corpus_file = open("small_corpus.txt", 'r')
	words = corpus_file.read().split()

	# Make statistics for each word (except last word)
	for i in range(len(words) - 1):
		current_word, next_word = words[i], words[i + 1]

		# Check that current word already exists or not
		if current_word in corpus_stats: # if this word already exists

			# Check that next word is new for this current word or not
			if next_word in corpus_stats[current_word]: # If not new, increment counting
				corpus_stats[current_word][next_word] += 1
			else: # If new, start counting
				corpus_stats[current_word][next_word] = 1
		else: # if this is a new word, add the next word and start counting
			corpus_stats[current_word] = {next_word: 1}

# Predict next word based on current word
def predict(current_word):
	max_freq_word = ''
	if current_word in corpus_stats:
		max_freq_word = max(corpus_stats[current_word], key=corpus_stats[current_word].get)	
	return max_freq_word

# Get the index of the last white space character or -1 if not found
def get_last_space_index(string):
	try:
		last_space_pos = string.rindex(' ')
	except ValueError:
		last_space_pos = -1
	return last_space_pos

# Init corpus statistics
corpus_stats = dict()
init_bigram_stats(corpus_stats)

# Init command line screen 
stdscr = curses.initscr()
curses.noecho()

# Text buffer stores all previous typed texts
text_buffer = ''

# Program loop
while True:
	# Get character from keyboard
	c = stdscr.getch()

	# Check character
	if c == 27: # If character is ESC, exit program loop
		break	
	elif c == 9: # If character is Tab, predict next word
		# Get last word in text buffer
		last_word = text_buffer[get_last_space_index(text_buffer) + 1 : ]

		# Predict next word
		next_word = predict(last_word)

		# Add next word to screen and text buffer
		stdscr.addstr(' ' + next_word)
		text_buffer += (' ' + next_word)
	else: # Else, just show that character on screen and add it to text buffer
		stdscr.addch(chr(c))
		text_buffer += chr(c)	

	# Refresh screen to show latest output
	stdscr.refresh()