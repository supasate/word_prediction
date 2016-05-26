# แก้ไขฟังก์ชัน string_hash ให้ได้ค่าไม่เกินขนาดของตารางแฮชที่มี
# โดยรับตัวแปร hash_table เพิ่ม ซึ่งเป็นลิสต์ที่ใช้ทำตารางแฮช

def string_hash(key, hash_table):
    hashed_value = 0
    for char in key:
        hashed_value += ord(char)
    hashed_value = hashed_value % len(hash_table)
    return hashed_value

hash_table = ['hello', None, 'Sunday', None]
print(string_hash("good", hash_table))