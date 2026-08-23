import customtkinter as ctk
from ToDo_gui import TodoGUI


def main():
    root = ctk.CTk()
    app = TodoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()