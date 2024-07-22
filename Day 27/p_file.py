import tkinter

texttile = "I am a Label"
window = tkinter.Tk()
window.title("My first tkinter program")
window.minsize(width=500,height=300)
my_label = tkinter.Label(text=texttile,font=("times new roman",25,"italic"))
# my_label.pack()
my_label.grid(column=0,row=0)
def button_has_been_clicked():
    my_label.config(text=f"{input_c.get()}")
    button.grid(column=2,row=0)
button = tkinter.Button(text="Click here",command=button_has_been_clicked)
# button.pack()
button.grid(column=1, row=1)
input_c = tkinter.Entry(width=10)
# input_c.pack()
input_c.grid(column=3,row=2)
input_c.get()
window.mainloop()

# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
#
# def calculate(**kwargs):
#     sum = 0
#     sum += kwargs["add"]
#     sum *= kwargs["multiply"]
#     print(sum)
#
# calculate(add=1,multiply=5)