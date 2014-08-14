from sys import stdin
import msvcrt

def init_stats(record):
	corpus_file = open("small_corpus.txt", 'r')
	words = corpus_file.read().split()
	for i in range(len(words) - 1):
		if words[i] in record:
			if words[i + 1] in record[words[i]]:
				record[words[i]][words[i + 1]] += 1
			else:
				record[words[i]][words[i + 1]] = 1
		else:
			record[words[i]] = {words[i + 1]: 1}

def next_word(current_word):
	max_freq_word = ''
	if current_word in record:
		max_freq_word = max(record[current_word], key=record[current_word].get)	
	return max_freq_word

record = dict()
init_stats(record) 
buff = ''
while True:
	c = msvcrt.getch()
	if ord(c) == 27: # ESC = exit
		break
	elif ord(c) == 9: # Tab = predict next word
		last_space_pos = buff.rindex(' ')
		last_word = buff[last_space_pos + 1:]
		nw = next_word(last_word)
		buff += (' ' + nw)
	else:
		buff += c.decode('utf-8')	
	print(buff)