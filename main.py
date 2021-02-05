from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib as plt
from Class import Class

root = Tk()
text = Text(root)
root.title('Calculating Grades')
root.maxsize(1100, 800)
root.config(bg = 'white')


#UI_frame = tk.Frame(root, width=1000, height=600, bg='white')
#UI_frame.grid(row=0, column=0, padx=5, pady=5)

#UI_class = tk.Frame(root, width=100, height=100, bg='black')
#UI_class.grid(row=1, column=1, padx=1, pady=1)

#tk.Button(UI_frame, text = "Add Class", command="", bg = 'light green').grid(row=1, column=10, padx=10, pady=10)


Complejidad = Class()

Complejidad.CalculateGrades(20, 20)
Complejidad.CalculateGrades(15, 15)
Complejidad.CalculateGrades(10, 10)


print(Complejidad.grades)
print(Complejidad.CalculateAverage(Complejidad.grades))

# root.mainloop()