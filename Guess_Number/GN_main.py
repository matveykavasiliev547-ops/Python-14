import customtkinter as ctk
from GN_gui import GuessNumberGUI


def main():
    root = ctk.CTk()
    app = GuessNumberGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()