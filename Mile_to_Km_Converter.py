from tkinter import *

# TODO: 1. Create a Window and write Title.
window = Tk()
window.minsize(width=250, height=250)
window.title("Mile to Km Converter")
window.config(padx=100, pady=100)

# TODO: 2. Create a Entry box and next to it write miles (take an integer).
input = Entry(width=10)
input.grid(row=0, column=0)
miles = input.get()
# creating label of "miles" nex to the entry box
label_miles = Label()
label_miles.config(text="Miles")
label_miles.grid(row=0, column=1)

# TODO: 3. Create Result Label.
result_label = Label()
result_label.config(text="")
result_label.grid(row=2, column=0)


# TODO: 4. Convert when a button clicked.
# Crate function
def button_clicked():
    result = int(input.get()) * 1.6214
    # Change the label of result
    result_label.config(text=round(result))

button = Button(text="Calculate", command=button_clicked)
button.grid(column=0, row=3)

# TODO: 5. Write two labels "is equal to"(left) and "Km"(right) next to the result.
Km_label = Label()
Km_label.config(text="Km")
Km_label.grid(row=2, column=1)

equal_label = Label()
equal_label.config(text="is equal to")
equal_label.place(x=-80, y = 20)

window.mainloop()

