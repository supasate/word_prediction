# แก้ไขฟังก์ชัน find_next_word ให้รองรับกรณีที่คำค้นไม่มีอยู่
# 1. แสดงค่าคำที่อยู่ถัดจาก word ใน text โดยเริ่มค้นหาจากตำแหน่ง start_pos
#    และ return text และ ค่าตำแหน่งจุดเริ่มหาถัดไป
# 2. ถ้าไม่มี word ปรากฎใน text ให้แสดงสตริงว่าง "" แล้ว return text และ -1
def find_next_word(text, word, start_pos):
    text = text[text.find(word, start_pos) + len(word) + 1: ]
    next_word = text[: text.find(' ')]
    print(next_word)
    start_pos = text.find(' ') + 1
    return text, start_pos
    
text = "Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning but still keep singing."
word = "keep"
start_pos = 0
text, start_pos = find_next_word(text, word, start_pos)
text, start_pos = find_next_word(text, word, start_pos)
text, start_pos = find_next_word(text, word, start_pos)
print(start_pos)
