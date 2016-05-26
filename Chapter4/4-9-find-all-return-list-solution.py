# แก้ไขคำสั่ง find_all ให้ return ลิสต์ของทุกคำถัดไป

def find_all(text, word):
    next_word_list = []
    splitted_text = text.split()
    for i in range(len(splitted_text) - 1):
        if (splitted_text[i] == word):
            next_word_list.append(splitted_text[i + 1])
    return next_word_list

text = "Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning."
result = find_all(text, "keep")
print(result)