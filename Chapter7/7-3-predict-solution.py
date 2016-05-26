# เขียนฟังก์ชัน predict เพื่อคืนผลลัพธ์เป็นคำทำนายถัดไป หรือ "" ถ้าไม่มีคำถัดไป
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

def predict(word, corpus_stats):
    if word in corpus_stats:
        return max(corpus_stats[word], key=corpus_stats[word].get)
    else:
        return ""

corpus_stats = {'Monday.': {'I': 1}, 'and': {'keep': 2}, 'Today': {'is': 2, 'I': 1}, 'Sunday.': {'I': 1}, 'coding.': {'Today': 1}, 'I': {'stay': 3}}
print(predict('Monday.', corpus_stats))
print(predict('Today', corpus_stats))