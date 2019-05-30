import tkinter as tk
mainWindow=tk.Tk()
mainWindow.title("CALCULATOR")
heading_label=tk.Label(mainWindow,text="Calculator",padx=(10),pady=(20))
heading_label.pack()
heading_label=tk.Label(mainWindow,text="ENTER FIRST NUMBER")
heading_label.pack()
first_field=tk.Entry(mainWindow)
first_field.pack()
heading_label=tk.Label(mainWindow,text="ENTER SECOND NUMBER")
heading_label.pack()
second_field=tk.Entry(mainWindow)
second_field.pack()
operation=tk.Label(mainWindow,text="operator")
operation.pack()
def addition():
    first=int(first_field.get())
    second=int(second_field.get())
    result=first+second
    result_label.config(text="operation result is:" +str(result))
addition_button=tk.Button(mainWindow,text="+",command=lambda:addition())
addition_button.pack()
def minus():
    first=int(first_field.get())
    second=int(second_field.get())
    result=first-second
    result_label.config(text="operation result is:" +str(result))

minus_button=tk.Button(mainWindow,text="-", command=lambda:minus())
minus_button.pack()
def multiply():
    first=int(first_field.get())
    second=int(second_field.get())
    result=first*second
    result_label.config(text="operation result is:" +str(result))
mul_button=tk.Button(mainWindow,text="*", command=lambda:multiply())
mul_button.pack()
def divide():
    first=int(first_field.get())
    second=int(second_field.get())
    result=first/second
    result_label.config(text="operation result is:" +str(result))
divide_button=tk.Button(mainWindow,text="/", command=lambda:divide())
divide_button.pack()
result_label=tk.Label(mainWindow, text="operations result is:")
result_label.pack()
mainWindow.mainloop()
