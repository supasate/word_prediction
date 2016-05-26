def add_to_corpus_index(key, next_word, corpus_index):
    if key not in corpus_index:
        corpus_index[key] = {next_word: 1}
    else:
        if next_word in corpus_index[key]:
            corpus_index[key][next_word] += 1
        else:
            corpus_index[key][next_word] = 1

corpus_index = {}
add_to_corpus_index('Today', 'is', corpus_index)
add_to_corpus_index('I', 'stay', corpus_index)
add_to_corpus_index('and', 'keep', corpus_index)
add_to_corpus_index('Today', 'is', corpus_index)
add_to_corpus_index('Today', 'I', corpus_index)
print(corpus_index)