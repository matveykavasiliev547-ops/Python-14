import tkinter as tk
from api_client import NotesAPIClient
from GUI import ModernNotesApp

def main():
    api = NotesAPIClient(base_url="http://127.0.0.1:8000")
    
    root = tk.Tk()
    app = ModernNotesApp(root, api_client=api)
    root.mainloop()

if __name__ == "__main__":
    main()