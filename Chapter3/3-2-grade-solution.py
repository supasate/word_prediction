# เพิ่มโค้ดคำนวณเกรดด้านล่างโดยพิมพ์เกรดที่ได้ออกทางหน้าจอ
def grade(score):
    if (score >= 80):
        print("A")
    elif (score >= 70):
        print("B")
    elif (score >= 60):
        print("C")
    elif (score >= 50):
        print("D")
    else:
        print("F")
grade(100)
grade(80)
grade(79)
grade(70)
grade(69)
grade(60)
grade(50)
grade(49)