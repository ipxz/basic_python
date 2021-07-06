"""propro manual"""

# เรื่องตัวคั่นเเละตัวจบของข้อความที่เเสดงผล

"""test"""
# def main():
#     '''1'''
#     text1 = input()
#     text2 = input()
#     text3 = input()
#     print(text1, text2, text3, sep="/", end=".")
#     # sep คือ ระบุตัวคั่นเเต่ละข้อความ
#     # end คือ ตัวระบุตัวจบ

# main()

# ----------------------------------------------------------------------------------------------------#

# เเปลงเลขฐานให้เป็นจำนวนเต็ม(เลขฐานสิบ)

"""test"""
# def main():
#     '''1'''
#     text1 = input() # ชุดของข้อมูลที่ต้องการแปลง
#     text2 = int(input()) # ชนิดของเลขฐานที่รับเข้ามาจากบรรทัดที่ 1
#     print(int(text1, text2)) # รูปเเบบของการเเปลงเลขฐานให้เป็นจำนวนเต็ม(เลขฐานสิบ)

# main()

# ----------------------------------------------------------------------------------------------------#

# StatsPVP :3

"""test"""
# def main():
#     """def"""
#     input1 = input()
#     input2 = int(input())
#     input3 = int(input())
#     input4 = int(input())
#     input5 = input()
#     input6 = int(input())
#     input7 = int(input())
#     input8 = int(input())
#     print("##############")
#     print("# %10s #" %(input1))
#     print("# HP:%7s #" %("O"*input2))
#     print("# ATk || DEF #")
#     print("# %04d||%04d #" %(input3, input4))
#     print("############## VS ##############")
#     print("                  # %10s #" %(input5))
#     print("                  # HP:%7s #" %("O"*input6))
#     print("                  # ATk || DEF #")
#     print("                  # %04d||%04d #" %(input7, input8))
#     print("                  ##############")

# main()

# ----------------------------------------------------------------------------------------------------#

# minute to second ที่โจทย์มันเอาวินาทีมาด้วย

"""test"""
# def main():
#     """def"""
#     input1 = float(input())
#     input2 = (input1//1) * 60
#     input3 = (input1%1) * 100
#     print(int(input2+input3))

# main()

# ----------------------------------------------------------------------------------------------------#

# ดึงเอาค่าตัวเลขออกมาจากตำเเหน่งที่เราระบุเอง

"""test"""
# def main():
#     """def"""
#     num = int(input())
#     x02 = (num % 10**9 // 10**8) # เอาเฉพาะตัวที่ 9
#     x04 = (num % 10**7 // 10**6)
#     x06 = (num % 10**5 // 10**4)
#     x08 = (num % 10**3 // 10**2)
#     x10 = (num % 10) # ตัวหลังสุด เริ่มจาก 10
#     print("%d%d%d%d%d" %(x02, x04, x06, x08, x10))

# main()

# ----------------------------------------------------------------------------------------------------#

# U R Broken My Heart

"""test"""
# def main():
#     """def"""
#     heart1 = int(input())
#     heart2 = int(input())
#     heart3 = (heart1+heart2)
#     heart4 = 10 - (heart1+heart2) # ถ้าเกิน 10 จะไม่เเสดง _
#     print("My Heart", heart1, "Heart", "|"+"<3"*heart3+"_"*heart4+"|")
#     print("My Bonus", heart2, "Heart")

# main()

# ----------------------------------------------------------------------------------------------------#

# Spam (Extra)

"""test"""
# def main():
#     """def"""
#     weight = input() + "\n" # inputเสร็จ เว้นบรรทัดเลย
#     ans = int(input())
#     print(weight*ans)

# main()

# ----------------------------------------------------------------------------------------------------#

# เมื่อใช้ mod ไม่ได้

"""test"""
# def main():
#     """while func"""
#     num1 = int(input())
#     num2 = int(input())
#     ans = num1 - (num1//num2)*num2 # สูตรหา mod เลข 2 ตัว
#     print(ans)

# main()

# ----------------------------------------------------------------------------------------------------#

# Many in Town

"""test"""
# def main():
#     """while func"""
#     num = int(input())
#     ans = num**3 + num**2 + num
#     print(ans)

# main()

# ----------------------------------------------------------------------------------------------------#

# second to วัน:ชั่วโมง:นาที:วินาที

"""test"""
# def main():
#     """while func"""
#     num1 = int(input())
#     ans1 = (num1 // 86400) # อันนี้จะได้วัน
#     ans2 = num1 % 86400 // 3600 # อันเศษจากอันก่อนหน้ามาหาต่อ
#     ans3 = num1 % 86400 % 3600 // 60
#     ans4 = num1 % 86400 % 3600 % 60
#     print("%02d:%02d:%02d:%02d" %(ans1, ans2, ans3, ans4))

# main()

# ----------------------------------------------------------------------------------------------------#

# absolute ให้ค่าเป็นบวกเสมอ

"""test"""

# def main():
#     """"test"""
#     input1 = abs(float(input())) # abs = absolute
#     print("%.2f" %input1)

# main()

# ----------------------------------------------------------------------------------------------------#

# เเปลงตัวอักษรภาษาอังกฤษเป็นลำดับ 1-26

"""test"""

# def main():
#     """"test"""
#     input1 = str(input())
#     ans = input1.lower()
#     print(ord(ans)-96) # ord คือ เปลี่ยนค่าเป็นเลขฐานสิบตามตาราง ascii โดย ตัว a เริ่มที่ 97 จึงต้องลบ 96

# main()

# ----------------------------------------------------------------------------------------------------#

# Grandpa = clock

"""Fewfewfew"""

# import math

# def main():
#     """few"""
#     number1 = math.pi
#     number2 = float(input())
#     result = (1/(2* number1))*math.sqrt(9.81/number2)
#     print("%.2f Hz" %result)

# main()

# ----------------------------------------------------------------------------------------------------#

# ozzzzzy

"""test"""

# def main():
#     """"test"""
#     text = str(input())
#     text2 = len(text)-2 # ตัด Oกับy ออก
#     print("O"+text2*"z"+"y")

# main()

# ----------------------------------------------------------------------------------------------------#

# ไม่ได้อยากถามเเค่อยากรู้ว่า

"""test"""
# def main():
#     """test"""
#     input1 = str(input())
#     ans = input1.count(".")
#     print("I love you. "*ans)
# main()

# ----------------------------------------------------------------------------------------------------#

# Just MAX it V.2

"""test"""

# def main():
#     """test"""
#     input1 = float(input())
#     input2 = float(input())
#     ans = input1+input2-min(input1, input2)
#     print("%.3f" % ans)

# main()

# ----------------------------------------------------------------------------------------------------#

# Richman V.2

"""test"""

# def main():
#     """test"""
#     number = input().replace(",", "") # replace เพื่อนที่จะเอาคำออกไป
#     number2 = abs(int(number))
#     print(len(str(number2)))

# main()

# ----------------------------------------------------------------------------------------------------#

# Composite Function

"""test"""

# def fog(number):
#     """"test"""
#     ans1 = (15+number-(number ** 3)) / (((number ** 2) / 3) + 11)
#     return ans1

# def gof(number):
#     """"test"""
#     ans2 = number**3 + (4*number) - 1
#     return ans2

# def main():
#     """test"""
#     num_input = float(input())
#     ans3 = float(fog(gof(num_input)))
#     ans4 = float(gof(fog(num_input)))
#     print("%.4f" %(ans3))
#     print("%.4f" %(ans4))

# main()

# ----------------------------------------------------------------------------------------------------#

"""Caesarrrrrrrrrrrrrrrrrrrrrrrr"""

# ขยับจากตัวอักษรที่รับเข้ามา n ตัวอักษร

# result = chr((ord(char) + n-65) % 26 + 65)  # n คือจำนวนที่ต้องการขยับ อันนี้พิมพ์ใหญ่
# result = chr((ord(char) + n-97) % 26 + 97) # พิมพืเล็ก

# ----------------------------------------------------------------------------------------------------#

"""Sandwich's Degrees"""

"""test"""
# import math

# def main():
#     """test"""
#     num1 = float(input())
#     num2 = float(input())
#     ans1 = num1/num2
#     ans2 = math.atan(ans1) # ได้มุม
#     ans3 = math.degrees(ans2) # ได้องศา
#     print("%.2f deg" % ans3)

# main()

# ----------------------------------------------------------------------------------------------------#

# Just MAX it V.3

"""test"""
# def main():
#     """test"""
#     num1 = float(input())
#     num2 = float(input())
#     num3 = float(input())
#     num4 = float(input())
#     num5 = float(input())
#     num6 = float(input())
#     num7 = float(input())
#     num8 = float(input())
#     ans1 = (num1+num2) - min(num1, num2)
#     ans2 = (num3+num4) - min(num3, num4)
#     ans3 = (num5+num6) - min(num5, num6)
#     ans4 = (num7+num8) - min(num7, num8)
#     ans5 = (ans1+ans2) - min(ans1, ans2)
#     ans6 = (ans3+ans4) - min(ans3, ans4)
#     ans7 = (ans5+ans6) - min(ans5, ans6)
#     print("%.2f" %(ans7))

# main()

# ----------------------------------------------------------------------------------------------------#

# VIP

"""test"""

# def main():
#     """test"""
#     input1 = float(input())
#     print("Welcome!"*(input1 > 0)+"Get out!"*(input1 == 0)) # ถ้า * ด้วย False ค่าที่ออกมาจะไม่มี

# main()

# ----------------------------------------------------------------------------------------------------#

# Kanomwhan Bakery

"""test"""

# def main():
#     """test"""
#     input1 = int(input())
#     input2 = float(input())
#     input3 = int(input())
#     ans1 = input1 * input2
#     ans2 = input1 * input2
#     if input1 >= 3:
#         ans1 = (input2*input1) - ((input2*input1) * (input3/100))
#     if input1 >= 4:
#         ans2 = (input1 // 4 * input2 * 3) + (input1 % 4 * input2)
#     if ans1 <= ans2:
#         print("Promotion 1 %.3f Baht" %(ans1))
#     else:
#         print("Promotion 2 %.3f Baht" %(ans2))
#     print("Purchase successfully !")
#     print("Have a good meal with \"Kanomwhan\"")

# main()

# ----------------------------------------------------------------------------------------------------#

"""Orange Cake"""

# def main():
#     """Orange Cake"""
#     input1 = int(input())
#     input2 = int(input())
#     if input1 // input2 != 0:
#         print("Orange Cake:", input1 // input2)
#         print("Money left:", input1 % input2)
#     else:
#         print("Not enough money;(")
#         print("Money left:", input1)

# main()

# ----------------------------------------------------------------------------------------------------#

"""เอ้า herb herb herb"""

# def herb(num):
#     """เอ้า herb herb herb"""
#     if num <= 100:
#         return num
#     else:
#         return 0

# def main():
#     """เอ้า herb herb herb"""
#     input1, input2 = herb(int(input())), herb(int(input()))
#     input3, input4 = herb(int(input())), herb(int(input()))
#     input5, input6 = herb(int(input())), herb(int(input()))
#     input7, input8 = herb(int(input())), herb(int(input()))
#     input9, input10 = herb(int(input())), herb(int(input()))
#     ans = input1 + input2 + input3 + input4 + input5 + input6 \
#     + input7 + input8 + input9 + input10
#     print(ans == 420 and 'herb' or ans)

# main()

# ----------------------------------------------------------------------------------------------------#

"""max it v.4"""
# def check_num(num1, num2):
#     """max it v.4"""
#     ans = (num1 * (num1 > num2) + num2 * (num2 > num1))
#     return ans

# def main():
#     """max it v.4"""
#     input1 = float(input())
#     result = check_num(input1, float(input()))
#     result = check_num(input1, float(input()))
#     result = check_num(input1, float(input()))
#     result = check_num(input1, float(input()))
#     result = check_num(input1, float(input()))
#     result = check_num(input1, float(input()))
#     result = check_num(input1, float(input()))
#     result = check_num(input1, float(input()))
#     result = check_num(input1, float(input()))
#     print("%.2f" %(result))

# main()

# ----------------------------------------------------------------------------------------------------#

"""Just a normal average day V.2"""

# def main():
#     """Just a normal average day V.2"""
#     input1 = int(input())
#     if 7 > input1 >= 0:
#         print("CHILD")
#     if 25 > input1 >= 7:
#         print("TEENAGER")
#     if 59 > input1 >= 25:
#         print("ADULT")
#     if input1 >= 59:
#         print("ELDER")

# main()
# main()
# main()
# main()
# main()

# ----------------------------------------------------------------------------------------------------#

"""What grade?"""

# def main():
#     """What grade?"""
#     input1 = int(float(input()))
#     if input1 >= 80:
#         print("A")
#     if 79 >= input1 >= 75:
#         print("B+")
#     if 74 >= input1 >= 70:
#         print("B")
#     if 69 >= input1 >= 65:
#         print("C+")
#     if 64 >= input1 >= 60:
#         print("C")
#     if 59 >= input1 >= 55:
#         print("D+")
#     if 54 >= input1 >= 50:
#         print("D")
#     if input1 < 50:
#         print("F")

# main()

# ----------------------------------------------------------------------------------------------------#

# """Way to travel"""

# def main():
#     """Way to travel"""
#     climate = str(input())
#     matter = str(input())
#     distance = float(input())

#     if climate == 'rainy' and matter == 'important' or climate == 'sunny':
#         if distance < 1:
#             if distance < 0:
#                 print("Error")
#             else:
#                 print("Walk")
#         elif distance < 20:
#             print("Motorcycle")
#         elif distance < 300:
#             print("Car")
#         elif distance > 300:
#             print("Private jet")
#         else:
#             print("Private jet")
#     else:
#         print("Not go")

# main()

# ---------------------------------------------------------------------------------------------------- #

"""What is it then?"""

# def main():
#     """What is it then?"""
#     massage = str(input())
#     resultfewfew = massage.isalpha() == True and 'an alphabet.' or massage.isnumeric() \
# == True and 'numeric.' or 'not both an alphabet and numeric.'
#     print("'" + massage + "' is " + resultfewfew)

# main()

# ---------------------------------------------------------------------------------------------------- #

"""Do you know leap year?"""

# def main():
#     """Do you know leap year?"""
#     input1 = int(input())
#     if input1 % 4 == 0:
#         if input1 % 100 != 0:
#             print("%d is a leap year." %(input1))
#         elif input1 % 100 == 0 and input1 % 400 == 0:
#             print("%d is a leap year." %(input1))
#         else:
#             print("%d is not a leap year." %(input1))
#     else:
#         print("%d is not a leap year." %(input1))

# main()

# ---------------------------------------------------------------------------------------------------- #

