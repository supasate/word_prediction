# แก้ไขคำสั่ง find_all ให้ return ลิสต์ของทุกคำถัดไป

def find_all(text, word):
    splitted_text = text.split()
    for i in range(len(splitted_text) - 1):
        if (splitted_text[i] == word):
            print(splitted_text[i + 1])

text = "Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning."
result = find_all(text, "keep")
print(result)