"""variables manual"""

# เช็คประเภทข้อมูล

# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# # # ผลลัพธ์
# <class 'int'>
# <class 'str'>

# ----------------------------------------------------------------------------------------------------#

# One Value to Multiple Variables

# x = y = z = "Orange"

# print(x)
# print(y)
# print(z)

# # # ผลลัพธ์
# Orange
# Orange
# Orange

# ----------------------------------------------------------------------------------------------------#

# การปลด list

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# # # ผลลัพธ์
# apple
# banana
# cherry

# ----------------------------------------------------------------------------------------------------#

# ถ้าตัวเเปรข้างนอกfunctionกับข้างในfunctionเหมือนกัน ตัวเเปรจะเเยกกัน

# x = "awesome"

# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)

# myfunc()

# print("Python is " + x)

# # # ผลลัพธ์
# Python is fantastic
# Python is awesome

# ----------------------------------------------------------------------------------------------------#

# global จะทำให้คำสั่งใน local scope กลายเป็น global scope

# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()

# print("Python is " + x)

# # # ผลลัพธ์
# Python is fantastic

# ----------------------------------------------------------------------------------------------------#

# เปลี่ยน variables ใน global scope ให้เป็น variables ใน local scope เเทน

# x = "awesome"

# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()

# print("Python is " + x)

# # # ผลลัพธ์
# Python is fantastic

# ----------------------------------------------------------------------------------------------------#

