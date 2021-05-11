from tkinter import *
expression=" "
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""
def clear():
    global expression
    expression=""
    equation.set("")
if  __name__  == "__main__" :
    top=Tk()
    top.title("My Calculator")
    top.geometry("256x130")
    top.configure(background="black")
    equation=StringVar()
    exp_field= Entry(top,textvariable=equation)
    exp_field.grid(columnspan=4,ipadx=70)
    equation.set("")
    button1 = Button(top, text="1",height=1,width=7,command=lambda:press(1)).grid(row=2,column=0)
    button2 = Button(top,text="2",height=1,width=7, command=lambda:press(2)).grid(row=2,column=1)
    button3 = Button(top, text="3", height=1, width=7, command=lambda:press(3)).grid(row=2, column=2)
    button4 = Button(top, text="4", height=1, width=7, command=lambda:press(4)).grid(row=3, column=0)
    button5 = Button(top, text="5", height=1, width=7, command=lambda:press(5)).grid(row=3, column=1)
    button6 = Button(top, text="6", height=1, width=7, command=lambda:press(6)).grid(row=3, column=2)
    button7 = Button(top, text="7", height=1, width=7, command=lambda:press(7)).grid(row=4, column=0)
    button8 = Button(top, text="8", height=1, width=7, command=lambda:press(8)).grid(row=4, column=1)
    button9 = Button(top, text="9", height=1, width=7, command=lambda:press(9)).grid(row=4, column=2)
    button0 = Button(top,text='0', height=1,width=7, command=lambda:press(0)).grid(row=5, column=0)
    plus = Button(top,text="+", height=1, width=10, command=lambda:press("+")).grid(row=2, column=3)
    minus =Button(top,text="-", height=1, width=10, command=lambda:press("-")).grid(row=3, column=3)
    multiply = Button(top, text="*", height=1, width=10, command=lambda:press("*")).grid(row=4, column=3)
    divide = Button(top, text="/", height=1, width=10, command=lambda:press("/")).grid(row=5, column=3)
    clear = Button(top,text="Clear",height=1,width=7,command=clear).grid(row=5, column=1)
    calculate= Button(top,text="=", height=1,width=7,command=equalpress).grid(row=5, column=2)
    top.mainloop()