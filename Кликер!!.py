import tkinter as tk

def click():
    global counter
    counter -= 1
    label.config(text=f"счёт:{counter}")
    if counter == 0:
       label.config(text="ПОБЕДА!",fg="green")
       button.config(state="disabled")

root = tk.Tk()
root.title("ClickerGame")
root.geometry("350x350")

counter = 50

label = tk.Label(root, text=f"счёт: {counter}", font=("Arial", 20))
label.pack(pady=20)

button = tk.Button(root, text="Кликай!", command=click)
button.pack(pady=20)

root.mainloop()

