import random
import tkinter as tk
from tkinter import messagebox

WORDS = ["яблоко", "футбол", "пенал", "ручка", "хлеб", "краб"]

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра — 'Виселица'")
        self.root.geometry("450x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")

        self.word = ""
        self.guessed_letters = set()
        self.attempts = 10

        self.create_widgets()
        self.start_new_game()

    def create_widgets(self):
        # Заголовок
        self.title_label = tk.Label(
            self.root, 
            text="Виселица", 
            font=("Arial", 22, "bold"), 
            bg="#2b2b2b", 
            fg="#ffffff"
        )
        self.title_label.pack(pady=10)

        # Попытки
        self.attempts_label = tk.Label(
            self.root, 
            text="", 
            font=("Arial", 12), 
            bg="#2b2b2b", 
            fg="#ff6b6b"
        )
        self.attempts_label.pack(pady=5)

        # Слово (с прочерками)
        self.display_label = tk.Label(
            self.root, 
            text="", 
            font=("Courier New", 28, "bold"), 
            bg="#2b2b2b", 
            fg="#4ed964"
        )
        self.display_label.pack(pady=20)

        # Поле ввода буквы
        input_frame = tk.Frame(self.root, bg="#2b2b2b")
        input_frame.pack(pady=10)

        tk.Label(
            input_frame, 
            text="Буква:", 
            font=("Arial", 14), 
            bg="#2b2b2b", 
            fg="#ffffff"
        ).pack(side=tk.LEFT, padx=5)

        self.letter_entry = tk.Entry(
            input_frame, 
            font=("Arial", 16), 
            width=5, 
            justify="center"
        )
        self.letter_entry.pack(side=tk.LEFT, padx=5)
        self.letter_entry.bind("<Return>", lambda event: self.make_guess())

        self.btn_guess = tk.Button(
            input_frame, 
            text="Проверить", 
            command=self.make_guess, 
            font=("Arial", 11, "bold"), 
            bg="#3b82f6", 
            fg="white", 
            activebackground="#2563eb",
            activeforeground="white",
            padx=10
        )
        self.btn_guess.pack(side=tk.LEFT, padx=5)

        # Использованные буквы
        self.used_letters_label = tk.Label(
            self.root, 
            text="Введённые буквы: ", 
            font=("Arial", 10), 
            bg="#2b2b2b", 
            fg="#aaaaaa"
        )
        self.used_letters_label.pack(pady=15)

        # Кнопка перезапуска
        self.btn_restart = tk.Button(
            self.root, 
            text="Новая игра", 
            command=self.start_new_game, 
            font=("Arial", 10), 
            bg="#4b5563", 
            fg="white", 
            activebackground="#374151",
            activeforeground="white"
        )
        self.btn_restart.pack(pady=5)

    def start_new_game(self):
        self.word = random.choice(WORDS)
        self.guessed_letters = set()
        self.attempts = 10
        self.btn_guess.config(state=tk.NORMAL)
        self.letter_entry.config(state=tk.NORMAL)
        self.update_ui()

    def update_ui(self):
        # Формируем отображение слова
        display = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.display_label.config(text=display)
        self.attempts_label.config(text=f"❤️ Осталось попыток: {self.attempts}")
        
        used = ", ".join(sorted(list(self.guessed_letters))) if self.guessed_letters else "нет"
        self.used_letters_label.config(text=f"Введённые буквы: {used}")

    def make_guess(self):
        guess = self.letter_entry.get().lower().strip()
        self.letter_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Ошибка ввода", "Введите ровно ОДНУ букву!")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Внимание", "Вы уже вводили эту букву!")
            return

        self.guessed_letters.add(guess)

        if guess not in self.word:
            self.attempts -= 1

        self.update_ui()

        # Проверка победы
        if all(letter in self.guessed_letters for letter in self.word):
            messagebox.showinfo("Победа! 🎉", f"Вы угадали слово '{self.word}'!")
            self.btn_guess.config(state=tk.DISABLED)
            self.letter_entry.config(state=tk.DISABLED)
            return

        # Проверка поражения
        if self.attempts <= 0:
            messagebox.showerror("Поражение 💀", f"Попытки закончились! Слово было: '{self.word}'")
            self.btn_guess.config(state=tk.DISABLED)
            self.letter_entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()