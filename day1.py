import tkinter as tk

def button_click():
    label.config(text="Button Clicked!")
 
window = tk.Tk()
window.title("Simple Tkinter App")
window.geometry("400x300")  # Width x Height in pixels

label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=100)  # 100px padding top and bottom

button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

window.mainloop()