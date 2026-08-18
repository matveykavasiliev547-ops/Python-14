import tkinter as tk
from tkinter import messagebox
from game import HangmanGame  # Подключаем нашу логику!

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра — 'Виселица'")
        self.root.geometry("450x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")

        # Создаем экземпляр бэкенда
        self.game = HangmanGame(max_attempts=10)

        self.create_widgets()
        self.restart_game()

    def create_widgets(self):
        self.title_label = tk.Label(
            self.root, text="Виселица", font=("Arial", 22, "bold"), 
            bg="#2b2b2b", fg="#ffffff"
        )
        self.title_label.pack(pady=10)

        self.attempts_label = tk.Label(
            self.root, text="", font=("Arial", 12), 
            bg="#2b2b2b", fg="#ff6b6b"
        )
        self.attempts_label.pack(pady=5)

        self.display_label = tk.Label(
            self.root, text="", font=("Courier New", 28, "bold"), 
            bg="#2b2b2b", fg="#4ed964"
        )
        self.display_label.pack(pady=20)

        input_frame = tk.Frame(self.root, bg="#2b2b2b")
        input_frame.pack(pady=10)

        tk.Label(
            input_frame, text="Буква:", font=("Arial", 14), 
            bg="#2b2b2b", fg="#ffffff"
        ).pack(side=tk.LEFT, padx=5)

        self.letter_entry = tk.Entry(
            input_frame, font=("Arial", 16), width=5, justify="center"
        )
        self.letter_entry.pack(side=tk.LEFT, padx=5)
        self.letter_entry.bind("<Return>", lambda event: self.make_guess())

        self.btn_guess = tk.Button(
            input_frame, text="Проверить", command=self.make_guess, 
            font=("Arial", 11, "bold"), bg="#3b82f6", fg="white", 
            activebackground="#2563eb", activeforeground="white", padx=10
        )
        self.btn_guess.pack(side=tk.LEFT, padx=5)

        self.used_letters_label = tk.Label(
            self.root, text="Введённые буквы: ", font=("Arial", 10), 
            bg="#2b2b2b", fg="#aaaaaa"
        )
        self.used_letters_label.pack(pady=15)

        self.btn_restart = tk.Button(
            self.root, text="Новая игра", command=self.restart_game, 
            font=("Arial", 10), bg="#4b5563", fg="white", 
            activebackground="#374151", activeforeground="white"
        )
        self.btn_restart.pack(pady=5)

    def restart_game(self):
        self.game.start_new_game()
        self.btn_guess.config(state=tk.NORMAL)
        self.letter_entry.config(state=tk.NORMAL)
        self.update_ui()

    def update_ui(self):
        # Дисплей берет данные напрямую из объекта бэкенда!
        self.display_label.config(text=self.game.display_word)
        self.attempts_label.config(text=f"❤️ Осталось попыток: {self.game.attempts}")
        self.used_letters_label.config(text=f"Введённые буквы: {self.game.used_letters_str}")

    def make_guess(self):
        guess = self.letter_entry.get()
        self.letter_entry.delete(0, tk.END)

        # Дергаем метод бэкенда
        result = self.game.make_guess(guess)

        if result["status"] == "error":
            messagebox.showwarning("Ошибка ввода", result["message"])
            return

        if result["status"] == "warning":
            messagebox.showinfo("Внимание", result["message"])
            return

        self.update_ui()

        # Проверка финала
        if result["is_won"]:
            messagebox.showinfo("Победа! 🎉", f"Вы угадали слово '{self.game.word}'!")
            self.disable_controls()

        elif result["is_lost"]:
            messagebox.showerror("Поражение 💀", f"Попытки закончились! Слово было: '{self.game.word}'")
            self.disable_controls()

    def disable_controls(self):
        self.btn_guess.config(state=tk.DISABLED)
        self.letter_entry.config(state=tk.DISABLED)

