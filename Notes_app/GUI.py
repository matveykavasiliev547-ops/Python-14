import tkinter as tk
from tkinter import messagebox, ttk
import requests
from api_client import NotesAPIClient


class ModernNotesApp:
    def __init__(self, root: tk.Tk, api_client: NotesAPIClient):
        self.root = root
        self.api = api_client

        self.root.title("Notes API Client")
        self.root.geometry("520x560")
        self.root.resizable(False, False)

        # Тёмная тема оформления
        self.root.configure(bg="#1e1e2e")
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame", background="#1e1e2e")
        style.configure("TLabel", background="#1e1e2e", foreground="#cdd6f4", font=("Segoe UI", 10))
        style.configure("TButton", background="#313244", foreground="#cdd6f4", font=("Segoe UI", 9, "bold"), borderwidth=0)
        style.map("TButton", background=[("active", "#45475a")])

        style.configure("Treeview", 
                        background="#181825", 
                        fieldbackground="#181825", 
                        foreground="#cdd6f4", 
                        rowheight=25,
                        font=("Segoe UI", 9))
        style.configure("Treeview.Heading", 
                        background="#313244", 
                        foreground="#cdd6f4", 
                        font=("Segoe UI", 10, "bold"))
        style.map("Treeview", background=[("selected", "#585b70")])

        # Главный контейнер
        main_frame = ttk.Frame(root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Поля ввода
        ttk.Label(main_frame, text="Текст заметки:").grid(row=0, column=0, sticky="w", pady=5)
        self.note_entry = ttk.Entry(main_frame, width=38, font=("Segoe UI", 10))
        self.note_entry.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        ttk.Label(main_frame, text="ID (удалить/обновить):").grid(row=1, column=0, sticky="w", pady=5)
        self.id_entry = ttk.Entry(main_frame, width=15, font=("Segoe UI", 10))
        self.id_entry.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        # Кнопки
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=15)

        ttk.Button(btn_frame, text="➕ Добавить", command=self.add_note).pack(side=tk.LEFT, padx=3)
        ttk.Button(btn_frame, text="✏️ Обновить", command=self.update_note).pack(side=tk.LEFT, padx=3)
        ttk.Button(btn_frame, text="❌ Удалить", command=self.delete_note).pack(side=tk.LEFT, padx=3)
        ttk.Button(btn_frame, text="🔄 Обновить список", command=self.show_notes).pack(side=tk.LEFT, padx=3)

        # Таблица
        self.tree = ttk.Treeview(main_frame, columns=("ID", "Content"), show="headings", height=13)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Content", text="Содержание заметки")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Content", width=420)
        self.tree.grid(row=3, column=0, columnspan=2, pady=5)

        self.tree.bind("<<TreeviewSelect>>", self.on_select_row)

        self.show_notes()

    def on_select_row(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item[0], "values")
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, values[0])
            self.note_entry.delete(0, tk.END)
            self.note_entry.insert(0, values[1])

    def show_notes(self):
        try:
            notes = self.api.get_notes()
            for item in self.tree.get_children():
                self.tree.delete(item)
            for note in notes:
                self.tree.insert("", tk.END, values=(note["id"], note["content"]))
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Ошибка", "Сервер FastAPI недоступен!")
        except requests.exceptions.HTTPError:
            messagebox.showerror("Ошибка", "Не удалось загрузить список заметок.")

    def add_note(self):
        content = self.note_entry.get().strip()
        if not content:
            messagebox.showwarning("Внимание", "Введите текст заметки!")
            return
        
        try:
            self.api.add_note(content)
            self.note_entry.delete(0, tk.END)
            self.show_notes()
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Ошибка", "Сервер FastAPI недоступен!")
        except requests.exceptions.HTTPError:
            messagebox.showerror("Ошибка", "Не удалось добавить заметку.")

    def update_note(self):
        note_id = self.id_entry.get().strip()
        new_content = self.note_entry.get().strip()

        if not note_id.isdigit() or not new_content:
            messagebox.showwarning("Внимание", "Введите ID и новый текст заметки!")
            return

        try:
            self.api.update_note(int(note_id), new_content)
            self.id_entry.delete(0, tk.END)
            self.note_entry.delete(0, tk.END)
            self.show_notes()
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Ошибка", "Сервер FastAPI недоступен!")
        except requests.exceptions.HTTPError:
            messagebox.showerror("Ошибка", f"Заметка с ID {note_id} не найдена.")

    def delete_note(self):
        note_id = self.id_entry.get().strip()
        if not note_id.isdigit():
            messagebox.showwarning("Внимание", "Укажите числовой ID заметки!")
            return

        try:
            self.api.delete_note(int(note_id))
            self.id_entry.delete(0, tk.END)
            self.note_entry.delete(0, tk.END)
            self.show_notes()
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Ошибка", "Сервер FastAPI недоступен!")
        except requests.exceptions.HTTPError:
            messagebox.showerror("Ошибка", f"Заметка с ID {note_id} не найдена.")