# เขียนฟังก์ชัน add_to_corpus_index เพื่อเพิ่ม word และ next_word เข้าใน corpus_index

def add_to_corpus_index(corpus_index, word, next_word):
    for el in corpus_index:
        if el[0] == word:
            el[1].append(next_word)
            return
    corpus_index.append([word, [next_word]])

corpus_index = []
add_to_corpus_index(corpus_index, "keep", "coding")
add_to_corpus_index(corpus_index, "Today", "is")
add_to_corpus_index(corpus_index, "keep", "cleaning")
print(corpus_index)    