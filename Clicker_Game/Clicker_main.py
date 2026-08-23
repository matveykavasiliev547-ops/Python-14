import customtkinter as ctk
from Clicker_gui import ClickerGUI


def main():
    root = ctk.CTk()
    app = ClickerGUI(root, initial_count=50)
    root.mainloop()


if __name__ == "__main__":
    main()