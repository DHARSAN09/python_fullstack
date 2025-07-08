import tkinter as tk

root = tk.Tk()
root.title("Place Example")
root.geometry("300x200")

# Widgets
label1 = tk.Label(root, text="At (50, 50)", bg="red", fg="white")
label2 = tk.Label(root, text="At (150, 100)", bg="green", fg="white")

# Place
label1.place(x=0.5, y=0.5)          # Absolute position
label2.place(relx=0.5, rely=0.5)  # 50% of window width/height

root.mainloop()