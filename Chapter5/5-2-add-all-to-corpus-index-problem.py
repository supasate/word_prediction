# เขียนฟังก์ชัน add_to_corpus_index เพื่อเพิ่ม word และ next_word เข้าใน corpus_index

def add_to_corpus_index(corpus_index, word, next_word):
    for el in corpus_index:
        if el[0] == word:
            el[1].append(next_word)
            return
    corpus_index.append([word, [next_word]])

def add_all_to_corpus_index(corpus_index, corpus):
    splitted_text = corpus.split()



corpus = "Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning. Today I stay awake."
corpus_index = []
add_all_to_corpus_index(corpus_index, corpus)
print(corpus_index)    