import tkinter as tk

root = tk.Tk()
root.title('calculator')
root.geometry('300x200')

def on_button_clicked(var):
    global expression
    expression =  expression + var
    tx.delete(0, 'end')
    tx.insert(0, expression)

def evaluate():
    global expression
    try:
        expression = str(round(eval(expression),2))
        tx.delete(0, 'end')
        tx.insert(0, expression)
    except:
        tx.delete(0, 'end')
        tx.insert(0, 'Error')


def clear():
    global expression
    expression = ""
    tx.delete(0, 'end')

def back():
    global expression
    expression = expression[0:len(expression)-1]
    tx.delete(0, 'end')
    tx.insert(0, expression)

expression = ""

operatorframe = tk.Frame(root)

operatorframe.columnconfigure(0, weight= 1)
operatorframe.columnconfigure(1, weight= 1)
operatorframe.columnconfigure(2, weight= 1)
operatorframe.columnconfigure(3, weight= 1)

buttonframe = tk.Frame(root)

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

tx = tk.Entry(buttonframe, width=16, font=('Calibri', 24))
tx.grid(columnspan=5, sticky='news', padx=0, pady=1)

btn0 = tk.Button(buttonframe, text='0', command=lambda:on_button_clicked('0'))
btn0.grid( row=1, column=0, stick=tk.E+tk.W)

btn1 = tk.Button(buttonframe, text='1', command=lambda:on_button_clicked('1'))
btn1.grid( row=1, column=1, stick=tk.E+tk.W)

btn2 = tk.Button(buttonframe, text='2', command=lambda:on_button_clicked('2'))
btn2.grid( row=1, column=2, stick=tk.E+tk.W)

btn3 = tk.Button(buttonframe, text='3', command=lambda:on_button_clicked('3'))
btn3.grid( row=2, column=0, stick=tk.E+tk.W)

btn4 = tk.Button(buttonframe, text='4', command=lambda:on_button_clicked('4'))
btn4.grid( row=2, column=1, stick=tk.E+tk.W)

btn5 = tk.Button(buttonframe, text='5', command=lambda:on_button_clicked('5'))
btn5.grid( row=2, column=2, stick=tk.E+tk.W)

btn6 = tk.Button(buttonframe, text='6', command=lambda:on_button_clicked('6'))
btn6.grid( row=3, column=0, stick=tk.E+tk.W)

btn7 = tk.Button(buttonframe, text='7', command=lambda:on_button_clicked('7'))
btn7.grid( row=3, column=1, stick=tk.E+tk.W)

btn8 = tk.Button(buttonframe, text='8', command=lambda:on_button_clicked('8'))
btn8.grid( row=3, column=2, stick=tk.E+tk.W)

btn9 = tk.Button(buttonframe, text='9', command=lambda:on_button_clicked('9'))
btn9.grid( row=4, column=1, stick=tk.E+tk.W)

btn_right_parenthesis = tk.Button(buttonframe, text=')', command=lambda:on_button_clicked(')'))
btn_right_parenthesis.grid(row = 4, column= 2, sticky=tk.E+tk.W)

btn_left_parenthesis = tk.Button(buttonframe, text='(', command=lambda:on_button_clicked('('))
btn_left_parenthesis.grid(row = 4, column= 0, sticky=tk.E+tk.W)

btn_operator_add = tk.Button(operatorframe, text= '+', command=lambda:on_button_clicked('+'))
btn_operator_add.grid(row=5,column=0,sticky='news')

btn_operator_sub = tk.Button(operatorframe, text= '-', command=lambda:on_button_clicked('-'))
btn_operator_sub.grid(row=5,column=1,sticky='news')

btn_operator_multiply = tk.Button(operatorframe, text= 'x', command=lambda:on_button_clicked('*'))
btn_operator_multiply.grid(row=5,column=2,sticky='news')

btn_operator_divide = tk.Button(operatorframe, text= '%', command=lambda:on_button_clicked('/'))
btn_operator_divide.grid(row=5,column=3,sticky='news')

btn_equals = tk.Button(operatorframe, text='=', command = evaluate)
btn_equals.grid(row=6, column=3,sticky='news')

btn_clear = tk.Button(operatorframe, text= 'C', command=clear)
btn_clear.grid(row = 6, column= 2, sticky='news')

btn_point = tk.Button(operatorframe, text='.', command=lambda:on_button_clicked('.'))
btn_point.grid(row=6, column=0, sticky='news')

btn_back = tk.Button(operatorframe, text = 'back', command = back)
btn_back.grid(row=6, column=1, sticky='news')


buttonframe.pack(fill='x')
operatorframe.pack(fill='x')


root.mainloop()
