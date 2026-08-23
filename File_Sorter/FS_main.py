import customtkinter as ctk
from FS_gui import FileSorterGUI


def main():
    root = ctk.CTk()
    app = FileSorterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()