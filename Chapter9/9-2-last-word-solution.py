# เติมโค้ดในลูป while เพื่อหาคำสุดท้ายก่อนกด tab

def add_to_corpus_index(key, next_word, corpus_index):
    if key not in corpus_index: 
        corpus_index[key] = {next_word: 1}
    else:
        if next_word in corpus_index[key]: 
            corpus_index[key][next_word] += 1
        else: 
            corpus_index[key][next_word] = 1

def init_corpus_stats(corpus_index, corpus):
    splitted_text = corpus.split()
    for i in range(len(splitted_text) - 1):
        word, next_word = splitted_text[i], splitted_text[i + 1]
        add_to_corpus_index(word, next_word, corpus_index)

def predict(word, corpus_stats):
    if word in corpus_stats:
        return max(corpus_stats[word], key=corpus_stats[word].get)
    else:       
        return ""

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

   