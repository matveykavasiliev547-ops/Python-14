import customtkinter as ctk
from PG_gui import PasswordGUI


def main():
    root = ctk.CTk()
    app = PasswordGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()