# แก้ไขฟังก์ชัน lookup ให้คืนค่า value ที่คู่กับ key หรือคืนค่า None ถ้าไม่มี key อยู่

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

def add_to_hash_table(key, value, hash_table):
    slot = string_hash(key, hash_table)
    hash_table[slot] = [key, value]
    
def lookup(key, hash_table):
    slot = string_hash(key, hash_table)
    if (hash_table[slot] == None):
        return None
    else:
        return hash_table[slot][1]

hash_table = create_hash_table(10)
add_to_hash_table('Somchai', 40, hash_table)
add_to_hash_table('Somsri', 20, hash_table)
add_to_hash_table('hello', 'world', hash_table)
print(lookup('Somchai', hash_table))
print(lookup('hello', hash_table))
print(lookup('siam', hash_table))