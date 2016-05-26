# แก้ไขโปรแกรมในกรณีคำที่ต้องการหาอยู่คำสุดท้าย
text = "Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning. keep"
word = "keep"
splitted_text = text.split()
for i in range(len(splitted_text) - 1):
    if (splitted_text[i] == word):
        print(splitted_text[i + 1])