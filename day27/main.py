from tkinter import *


def button_clicked():
    x = float(input.get())
    xy = x * 1.609
    km_label.config(text=xy)


window = Tk()
window.title("Miles to km converter")
window.minsize(width=400, height=300)
window.config(padx=10, pady=20)

eq = Label(text="is equal to", font=("Arial", 12))
eq.grid(column=1, row=2)
eq.config(padx=10, pady=20)

input = Entry(width=10)
print(input.get())
input.grid(column=2, row=1)


km_label = Label(text="0", font=("Arial", 12))
km_label.grid(column=2, row=2)
km_label.config(padx=10, pady=20)

mi = Label(text="Miles", font=("Arial", 12))
mi.grid(column=3, row=1)
mi.config(padx=10, pady=20)

km = Label(text="Km", font=("Arial", 12))
km.grid(column=3, row=2)
km.config(padx=10, pady=20)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)












window.mainloop()