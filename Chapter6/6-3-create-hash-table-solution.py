# เขียนฟังก์ชัน create_hash_table เพื่อสร้างตารางแฮชเปล่าที่ทุก element เป็นค่า None

def create_hash_table(size):
    hash_table = []
    for i in range(size):
        hash_table.append(None)
    return hash_table

hash_table = create_hash_table(10)
print(hash_table)