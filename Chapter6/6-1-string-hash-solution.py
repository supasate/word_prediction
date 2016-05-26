# เขียนฟังก์ชัน string_hash โดยรับตัวแปร key เป็นสตริง
# แล้วคำนวณค่า hash ที่เกิดจากผลรวมของค่า ASCII ของแต่ละอักษร

def string_hash(key):
    hashed_value = 0
    for char in key:
        hashed_value += ord(char)
    return hashed_value

print(string_hash("Today"))
print(string_hash("HelloWorld"))