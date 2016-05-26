# เขียนโปรแกรมหา key ที่มี value มากที่สุด

hash_table = {'a': 15, 'b': 2, 'c': 10}
max_key = ''
max_val = 0
for k,v in hash_table.items():
    if max_val < v:
        max_key = k
        max_val = v
print(max_key + ":" + str(max_val))