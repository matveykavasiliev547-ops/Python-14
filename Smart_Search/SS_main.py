import customtkinter as ctk
from SS_gui import SmartSearchGUI


def main():
    root = ctk.CTk()
    app = SmartSearchGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()