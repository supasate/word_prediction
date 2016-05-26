# กำหนดตัวแปร text ซึ่งเป็นสตริงต่อไปนี้มาให้
# text = "Today is Sunday. I stay at home and keep coding."
# word = "keep"
# ให้เขียนโปรแกรมหาคำที่อยู่ถัดจากตัวแปร word และพิมพ์ออกทางหน้าจอ

text = "Today is Sunday. I stay at home and keep coding. "
word = "keep"
text = text[text.find(word) + len(word) + 1: ]
next_word = text[: text.find(' ')]
print(next_word)