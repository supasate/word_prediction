# เขียนฟังก์ชัน add_to_hash_table เพื่อเพิ่ม key เข้า hash_table

def string_hash(key, hash_table):
    hashed_value = 0
    for char in key:
        hashed_value += ord(char)
    hashed_value = hashed_value % len(hash_table)
    return hashed_value

def create_hash_table(size):
    hash_table = []
    for i in range(size):
        hash_table.append(None)
    return hash_table

def add_to_hash_table(key, hash_table):
    slot = string_hash(key, hash_table)
    hash_table[slot] = key

hash_table = create_hash_table(10)
add_to_hash_table('Today', hash_table)
add_to_hash_table('hello', hash_table)
add_to_hash_table('coding', hash_table)
print(hash_table)