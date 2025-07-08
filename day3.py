import tkinter as tk

def show_state():
    if checkbox_var.get():
        state_label.config(text="Checkbox is checked")
    else:
        state_label.config(text="Checkbox is unchecked")

window = tk.Tk()
window.title("Checkbox Example")

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="Check me!", variable=checkbox_var, command=show_state)
checkbox.pack(pady=10)

state_label = tk.Label(window, text="Checkbox is unchecked")
state_label.pack()

window.mainloop()