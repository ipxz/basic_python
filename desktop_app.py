# """desktop app"""
# inputคำไปเเล้วหัวข้อจะเปลี่ยนตามที่เรา inputไป

# import tkinter as tk

# def set_massage():
#     text = text_input.get()
#     title_label.configure(text=text)

# window = tk.Tk()
# window.title("desktop app")
# window.minsize(width=500, height=800)

# title_label = tk.Label(master=window, text="desktop app")
# title_label.pack()

# text_input = tk.Entry(master=window)
# text_input.pack()

# ok_button = tk.Button(master=window, text="ok"
#                       ,command=set_massage)
# ok_button.pack()

# window.mainloop()

# ----------------------------------------------------------------------------------------------------#

# สูตรคูณเเม่ 1 ถึง 12

# import tkinter as tk

# window = tk.Tk()
# window.title("desktop app")
# window.minsize(width=500, height=800)

# def multiplication_table():
#     number = int(number_input.get())

#     output = ""
#     for i in range(1, 13):
#         output += str(number) + "x" + str(i) \
#             + "=" + str(number*i) + '\n'

#     output_label.configure(text=output)

# title_label = tk.Label(master=window, text="desktop app")
# title_label.pack()

# number_input = tk.Entry(master=window)
# number_input.pack()

# ok_button = tk.Button(master=window, text="ok", 
#                       command=multiplication_table)
# ok_button.pack()

# output_label = tk.Label(master=window)
# output_label.pack()

# window.mainloop()

# ----------------------------------------------------------------------------------------------------#

