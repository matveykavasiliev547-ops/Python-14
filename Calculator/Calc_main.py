import customtkinter as ctk
from Calc_gui import CalculatorGUI

def main():
    root = ctk.CTk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()