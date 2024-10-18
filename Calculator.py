from tkinter import * 
from tkmacosx import Button

root = Tk()
root.title("Calculator")

e = Entry(root, width=20, borderwidth=5)
e.grid(column=0, row=0, columnspan=4)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
plus = False
minus = False
times = False
divide = False
operator = False
first_number = 0
dot = False
first_input_dot = True
negative = False

def button_press(input):
    global plus
    global minus
    global divide
    global times
    global operator
    global first_number
    global dot
    global first_input_dot
    global negative
#Pressing the numbers after an operator has been pressed
    if (input in numbers or input == '.') and operator:
        first_number = float(e.get())
        e.delete(0, END)
        operator = False
        negative = False
#Pressing the numbers
    if input in numbers:
        e.insert("end", input)
        first_input_dot = False
#Pressing +, -, * or / sends signal to =
    if input == "+":
        first_input_dot = True
        dot = False
        operator = True
        plus = True
        times = False
        divide = False
        minus= False
    if input == "*":
        first_input_dot = True
        dot = False
        operator = True
        times = True
        plus = False
        divide = False
        minus= False
    if input == "/":
        first_input_dot = True
        dot = False
        operator = True
        divide = True
        times = False
        plus = False
        minus= False
        negative = False
    if input == "-":
        first_input_dot = True
        dot = False
        operator = True
        minus = True
        times = False
        divide = False
        plus= False
    #Pressing =
    if input == "=":
        second_number = e.get()
        if plus == True:
            e.delete(0, END)
            e.insert(0, first_number + float(second_number))
            plus = False
        if minus == True:
            e.delete(0, END)
            e.insert(0, first_number - float(second_number))
            minus = False
        if divide == True:
            e.delete(0, END)
            e.insert(0, first_number / float(second_number))
            divide = False
        if times == True:
            e.delete(0, END)
            e.insert(0, first_number * float(second_number))
            times = False
        if e.get():
            rounded_number = round(float(e.get()))        
        if rounded_number == float(e.get()):
            e.delete(0, END)
            e.insert(0, rounded_number)
    #Pressing clear button
    if input == "C":
        e.delete(0, END)
        first_number = 0
        second_number = 0
        plus = False
        times = False
        minus = False
        divide = False
        dot = False
        first_input_dot = True
        negative = False
    #dividing by 100 when clicking %
    if input == "%":
        percent_number = float(e.get())
        e.delete(0, END)
        e.insert(0, percent_number / 100)
    #putting dot between numbers
    if input == "." and dot == False and first_input_dot == False:
        e.insert("end", ".")
        dot = True
    elif input == "." and dot == False and first_input_dot:
        e.delete(0, END)
        e.insert(0, "0.")
        first_input_dot = False
        dot = True
    #clicking on the +/- button
    if input == "+/-":
        if e.get(): 
            if negative == False:
                e.insert(0, "-")
                negative = True
            elif negative:
                e.delete(0, 1)
                negative = False


#Creating the buttons
button_1 =  Button(root, text="1", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(1))
button_2 =  Button(root, text="2", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(2))
button_3 =  Button(root, text="3", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(3))
button_4 =  Button(root, text="4", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(4))
button_5 =  Button(root, text="5", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(5))
button_6 =  Button(root, text="6", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(6))
button_7 =  Button(root, text="7", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(7))
button_8 =  Button(root, text="8", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(8))
button_9 =  Button(root, text="9", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(9))
button_0 =  Button(root, text="0", width= 100, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press(0))
button_equal = Button(root, text="=", width=50, height=50, fg= "white", bg= "#FF9912",borderless= 1, command= lambda: button_press("="))
button_dot = Button(root, text=".", width=50, height=50, fg= "white", bg= "gray20", borderless= 1, command= lambda: button_press("."))
button_minus = Button(root, text="-", width=50, height=50, fg= "white", bg= "#FF9912", borderless= 1, command= lambda: button_press("-"))
button_plus = Button(root, text="+", width=50, height=50, fg= "white", bg= "#FF9912", borderless= 1, command= lambda: button_press("+"))
button_divide = Button(root, text="/", width=50, height=50, fg= "white", bg= "#FF9912", borderless= 1, command= lambda: button_press("/"))
button_x = Button(root, text="x", width=50, height=50, fg= "white", bg= "#FF9912", borderless= 1, command= lambda: button_press("*"))
button_clear = Button(root, text="C", width=50, height=50, fg= "black", bg= "gray73", command= lambda: button_press("C"))
button_percent= Button(root, text="%", width=50, height=50, fg= "black", bg= "gray73", command= lambda: button_press("%"))
button_plusminus = Button(root, text="+/-", width=50, height=50, fg= "black", bg= "gray73", command= lambda: button_press("+/-"))

#Buttons positioning
button_1.grid(column=0, row=4)
button_2.grid(column=1, row=4)
button_3.grid(column=2, row = 4)
button_4.grid(column=0, row=3)
button_5.grid(column=1, row=3)
button_6.grid(column=2, row=3)
button_7.grid(column=0, row=2)
button_8.grid(column=1, row=2)
button_9.grid(column=2, row=2)
button_0.grid(column=0, row=5, columnspan=2)
button_equal.grid(column=3, row=5)
button_dot.grid(column=2, row=5)
button_plus.grid(column=3, row=4)
button_clear.grid(column=0, row=1)
button_minus.grid(column=3, row=3)
button_x.grid(column=3, row=2)
button_divide.grid(column=3, row=1)
button_plusminus.grid(column=1, row=1)
button_percent.grid(column=2, row=1)

root.configure(background="black")
root.mainloop()