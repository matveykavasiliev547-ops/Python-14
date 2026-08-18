import tkinter as tk
from gui import HangmanGUI  

def main():
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()