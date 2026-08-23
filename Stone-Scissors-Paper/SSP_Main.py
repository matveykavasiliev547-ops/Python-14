import customtkinter as ctk
from SSP_GUI import RockPaperScissorsGUI


def main():
    root = ctk.CTk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()