# จงเขียนโปรแกรมเพื่อแสดงคำที่อยู่ถัดจากคำที่กำหนด
# โดยที่
# ตัวแปร text คือประโยคทั้งหมดไว้
# ตัวแปร word คือคำที่ต้องการหาคำที่อยู่ถัดไป
# เช่น text = "A white cat" และ word = "white" 
# โปรแกรมจะต้องแสดงคำว่า cat เพราะเป็นคำถัดจาก "white"
text = "Today is Sunday. I stay at home and keep coding."
word = "keep"
sub_text = text[text.find(word) + len(word) + 1:]
print(sub_text[: sub_text.find(' ')])