import tkinter as tk



calculation = " "

def add_to_cal(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_cal():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
       

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    pass

root = tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root, height = 2, width = 16, font=("Arial", 24))
text_result.grid(columnspan=5)
btn_1 = tk.Button(root, text="1", command = lambda: add_to_cal(1), width =5, font = ("Arial", 14))
btn_1.grid(row=2,column=1)
btn_2 = tk.Button(root, text="2", command = lambda: add_to_cal(2), width =5, font = ("Arial", 14))
btn_2.grid(row=2,column=2)
btn_3 = tk.Button(root, text="3", command = lambda: add_to_cal(3), width =5, font = ("Arial", 14))
btn_3.grid(row=2,column=3)
btn_plus = tk.Button(root, text="+", command = lambda: add_to_cal("+"), width =5, font = ("Arial", 14))
btn_plus.grid(row=2,column=4)
btn_4 = tk.Button(root, text="4", command = lambda: add_to_cal(4), width =5, font = ("Arial", 14))
btn_4.grid(row=3,column=1)
btn_5 = tk.Button(root, text="5", command = lambda: add_to_cal(5), width =5, font = ("Arial", 14))
btn_5.grid(row=3,column=2)
btn_6 = tk.Button(root, text="6", command = lambda: add_to_cal(6), width =5, font = ("Arial", 14))
btn_6.grid(row=3,column=3)
btn_min = tk.Button(root, text="-", command = lambda: add_to_cal("-"), width =5, font = ("Arial", 14))
btn_min.grid(row=3,column=4)
btn_7 = tk.Button(root, text="7", command = lambda: add_to_cal(7), width =5, font = ("Arial", 14))
btn_7.grid(row=4,column=1)
btn_8 = tk.Button(root, text="8", command = lambda: add_to_cal(8), width =5, font = ("Arial", 14))
btn_8.grid(row=4,column=2)
btn_9 = tk.Button(root, text="9", command = lambda: add_to_cal(9), width =5, font = ("Arial", 14))
btn_9.grid(row=4,column=3)
btn_multi = tk.Button(root, text="*", command = lambda: add_to_cal("*"), width =5, font = ("Arial", 14))
btn_multi.grid(row=4,column=4)
btn_0 = tk.Button(root, text="0", command = lambda: add_to_cal(0), width =5, font = ("Arial", 14))
btn_0.grid(row=5,column=2)
btn_prepar = tk.Button(root, text="(", command = lambda: add_to_cal("("), width =5, font = ("Arial", 14))
btn_prepar.grid(row=5,column=1)
btn_postpar = tk.Button(root, text=")", command = lambda: add_to_cal(")"), width =5, font = ("Arial", 14))
btn_postpar.grid(row=5,column=3)
btn_div = tk.Button(root, text="/", command = lambda: add_to_cal("/"), width =5, font = ("Arial", 14))
btn_div.grid(row=5,column=4)
btn_equals = tk.Button(root, text="=", command =  evaluate_cal, width =11, font = ("Arial", 14))
btn_equals.grid(row=6,column=1, columnspan=2)
btn_clear = tk.Button(root, text="C", command = clear_field, width =11, font = ("Arial", 14))
btn_clear.grid(row=6,column=3, columnspan=2)



root.mainloop()