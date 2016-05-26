# เขียนฟังก์ชัน lookup เพื่อ return ตำแหน่งที่ key อยู่ใน hash_table

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

def lookup(key, hash_table):






hash_table = create_hash_table(10)
add_to_hash_table('Today', hash_table)
add_to_hash_table('hello', hash_table)
add_to_hash_table('coding', hash_table)
print(lookup('hello', hash_table))
print(lookup('siam', hash_table))