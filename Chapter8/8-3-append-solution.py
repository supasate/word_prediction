# เขียนโปรแกรมให้นำคำว่า Hello ไปเพิ่มต่อท้ายเนื้อหาในไฟล์

with open("myfile.txt", "r+") as f:
    f.read()
    f.write(" Hello")
    f.seek(0)
    print(f.read())