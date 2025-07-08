from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title('Form Example')
window.geometry("400x300+10+10")

# Radio Buttons (Gender Selection)
gender_var = IntVar()
gender_var.set(1)  # Default selection

Label(window, text="Gender:").place(x=50, y=50)

Radiobutton(window, text="Male", variable=gender_var, value=1).place(x=100, y=50)
Radiobutton(window, text="Female", variable=gender_var, value=2).place(x=180, y=50)

# Checkboxes (Hobbies Selection)
Label(window, text="Hobbies:").place(x=50, y=100)

cricket_var = IntVar()
tennis_var = IntVar()

Checkbutton(window, text="Cricket", variable=cricket_var).place(x=100, y=100)
Checkbutton(window, text="Tennis", variable=tennis_var).place(x=180, y=100)

# Combobox (Dropdown Selection)
Label(window, text="Single Selection:").place(x=60, y=130)

options = ("one", "two", "three", "four")
combo = Combobox(window, values=options)
combo.current(0)  # Set default selection
combo.place(x=60, y=150)

# Listbox (Multiple Selection)
Label(window, text="Multiple Selection:").place(x=250, y=130)

listbox = Listbox(window, height=5, selectmode='multiple')
for item in options:
    listbox.insert(END, item)
listbox.place(x=250, y=150)

# Submit Button
def submit():
    # Get all selected values
    gender = "Male" if gender_var.get() == 1 else "Female"
    hobbies = []
    if cricket_var.get(): hobbies.append("Cricket")
    if tennis_var.get(): hobbies.append("Tennis")
    single_selection = combo.get()
    
    # Get multiple selections from listbox
    multiple_selections = [listbox.get(i) for i in listbox.curselection()]
    
    # Display results (in real app, you'd save to database/file)
    print(f"Gender: {gender}")
    print(f"Hobbies: {', '.join(hobbies) if hobbies else 'None'}")
    print(f"Single Selection: {single_selection}")
    print(f"Multiple Selections: {', '.join(multiple_selections) if multiple_selections else 'None'}")

Button(window, text="Submit", command=submit).place(x=150, y=200)

window.mainloop()