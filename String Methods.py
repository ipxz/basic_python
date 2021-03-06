"""casefold"""

# คล้ายๆ lower เเต่จะได้เเค่อังกฤษเเละไม่หลายหลาย

# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x)

# ----------------------------------------------------------------------------------------------------#

"""center"""

# เติมข้อความ ซ้ายขวา เเล้้วคำหลักจะอยู่ตรงกลาง โดยจะเพิ่มจากด้านขวาก่อน
# ถ้าจะให้พอดีต้อง คู่ - คู่, คี่ - คี่

# txt = "0"
# x = txt.center(3) # อันนี้คือ เพิ่มช่องว่างป่าวๆ
# print(x)

# string.center(length, character)
# txt = "0"
# x = txt.center(3, "1") # 101
# z = txt.center(2, "") # 01
# print(x)
# print(z)

# ----------------------------------------------------------------------------------------------------#

"""count"""

# นับคำไม่สนตัวหน้าตัวหลัง

# txt = "apples, apple"
# x = txt.count("apple")
# print(x)

# string.count(value, start, end) # เริ่มที่ 0
# txt = "apples, apple"
# x = txt.count("apple", 1, 20) # 1
# print(x)

# ----------------------------------------------------------------------------------------------------#

"""endswith"""

# ตรวจสอบคำว่าอยู่ในนั้นไหม ผลที่ออกมาจะเป็นค่าความจริง

# txt = "Hello, welcome to my world."
# x = txt.endswith("my world.") # True
# print(x)

# string.endswith(value, start, end)

# txt = "Hello, welcome to my world."
# x = txt.endswith("my world.", 5, 11) # False
# print(x)

# ----------------------------------------------------------------------------------------------------#

"""expandtabs"""

# ตั้งค่าความห่างของ tab
# ถ้าระบุพารามิเตอร์ (tabsize) เป็น 5 จะเป็นการแทรกช่องว่าง (space) 4 ครั้ง ตามด้วยตัวอักษรตัวถัดไป

# txt = "H\te"
# print(txt)
# print("H       e")
# print(txt.expandtabs(8))

# ----------------------------------------------------------------------------------------------------#

"""find"""

# หาตำเเหน่งของคำ โดยจะได้เเค่ตัวเเรกที่เจอจากซ้ายไปขวา เเละถ้าหาไม่เจอจะเเสดงค่ามาเป็น -1

# string.find(value, start, end)

# txt = "qwe"
# print(txt.find("a"))

# ----------------------------------------------------------------------------------------------------#

"""format"""

# เเทรกคำ

# txt = "For only {:.2f} dollars!"
# print(txt.format(49))

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# ระบุค่าที่ต้องการเเทรกได้ด้วยเลข index

# txt2 = "My name is {0}, I'm {1}".format("John",36)
# print(txt2)

# :, จะเป็นการคั่น , ให้กับหลักของเลข
# txt = "The universe is {:,} years old."
# print(txt.format(1000))

# ----------------------------------------------------------------------------------------------------#

