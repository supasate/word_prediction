# เขียนโปรแกรมเพื่อแทรกคำว่า Hello ไว้ด้านหน้าไฟล์โดยไม่ทับของเก่า

with open("myfile.txt", "r+") as f:
    f.write("Hello")
    f.seek(0)
    print(f.read())