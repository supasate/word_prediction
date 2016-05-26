# เขียนฟังก์ชัน load_corpus เพื่ออ่าน corpus จากไฟล์ชื่อ corpus.txt

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
        current_word, next_word = splitted_text[i], splitted_text[i + 1]
        add_to_corpus_index(current_word, next_word, corpus_index)

def load_corpus(file_name):





corpus = load_corpus("corpus.txt")
corpus_stats = {}
init_corpus_stats(corpus_stats, corpus)
print(corpus_stats)