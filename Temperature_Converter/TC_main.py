import customtkinter as ctk
from TC_gui import TemperatureGUI


def main():
    root = ctk.CTk()
    app = TemperatureGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()