# เขียนฟังก์ชัน lookup โดย return ลิสต์ของคำถัดไปทั้งหมดของ word
def lookup(corpus_index, word):
    for el in corpus_index:
        if el[0] == word:
            return el[1]
    return None

corpus = "Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning. Today I stay awake."
corpus_index = [['Today', ['is', 'is', 'I']], ['is', ['Sunday.', 'Monday.']], ['Sunday.', ['I']], ['I', ['stay', 'stay', 'stay']], ['stay', ['at', 'at', 'awake.']], ['at', ['home', 'office']], ['home', ['and']], ['and', ['keep', 'keep']], ['keep', ['coding.', 'cleaning.']], ['coding.', ['Today']], ['Monday.', ['I']], ['office', ['and']], ['cleaning.', ['Today']]]
print(lookup(corpus_index, "stay"))