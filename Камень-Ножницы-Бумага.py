import random
import tkinter as tk
from tkinter import messagebox
from typing import Optional


# 1. Логика правил (осталась абсолютно той же!)
class GameRules:
    CHOICES = ["камень", "ножницы", "бумага"]

    _WINNING_COMBINATIONS = {
        "камень": "ножницы",
        "бумага": "камень",
        "ножницы": "бумага",
    }

    @classmethod
    def get_winner(cls, user_move: str, bot_move: str) -> Optional[str]:
        if user_move == bot_move:
            return None
        elif cls._WINNING_COMBINATIONS[user_move] == bot_move:
            return "user"
        return "bot"


# 2. Логика бота (тоже без изменений)
class BotPlayer:
    @staticmethod
    def make_move() -> str:
        return random.choice(GameRules.CHOICES)


# 3. Графический интерфейс на Tkinter
class RockPaperScissorsGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Камень-Ножницы-Бумага")
        self.root.geometry("450x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")  # Тёмная тема!

        self.bot = BotPlayer()

        # Инициализация элементов интерфейса
        self._create_widgets()

    def _create_widgets(self):
        # Заголовок
        title_label = tk.Label(
            self.root,
            text="Камень • Ножницы • Бумага",
            font=("Segoe AI", 16, "bold"),
            bg="#2b2b2b",
            fg="#ffffff",
        )
        title_label.pack(pady=15)

        # Табло с выбором бота
        self.bot_choice_label = tk.Label(
            self.root,
            text="Бот ждёт твоего хода...",
            font=("Segoe UI", 12),
            bg="#3c3f41",
            fg="#a9b7c6",
            width=32,
            height=2,
            relief="groove",
        )
        self.bot_choice_label.pack(pady=10)

        # Результат раунда
        self.result_label = tk.Label(
            self.root,
            text="Сделай выбор ниже!",
            font=("Helvetica", 14, "bold"),
            bg="#2b2b2b",
            fg="#e8e8e8",
        )
        self.result_label.pack(pady=20)

        # Фрейм (контейнер) для кнопок
        buttons_frame = tk.Frame(self.root, bg="#2b2b2b")
        buttons_frame.pack(pady=10)

        # Создаём 3 кнопки для пользователя
        moves = [("💎 Камень", "камень"), ("✂ Ножницы", "ножницы"), ("📄 Бумага", "бумага")]

        for text, move in moves:
            btn = tk.Button(
                buttons_frame,
                text=text,
                font=("Helvetica", 11, "bold"),
                bg="#4a4d50",
                fg="#ffffff",
                activebackground="#686b6f",
                activeforeground="#ffffff",
                padx=12,
                pady=8,
                bd=0,
                command=lambda m=move: self._play_round(m),
            )
            btn.pack(side="left", padx=5)

        # Кнопка выхода
        exit_btn = tk.Button(
            self.root,
            text="Выйти из игры",
            font=("Helvetica", 10),
            bg="#8b0000",
            fg="#ffffff",
            activebackground="#a52a2a",
            padx=10,
            pady=5,
            bd=0,
            command=self.root.quit,
        )
        exit_btn.pack(pady=30)

    def _play_round(self, user_move: str):
        """Обработка клика по кнопке хода."""
        bot_move = self.bot.make_move()

        # Обновляем текст с ходом бота
        self.bot_choice_label.config(
            text=f"Бот выбрал: {bot_move.capitalize()}"
        )

        # Определяем победителя
        winner = GameRules.get_winner(user_move, bot_move)

        if winner is None:
            self.result_label.config(text="🤝 НИЧЬЯ!", fg="#ffc66d")
        elif winner == "user":
            self.result_label.config(text="🎉 ВЫ ПОБЕДИЛИ!", fg="#6a8759")
        else:
            self.result_label.config(text="💀 ВЫ ПРОИГРАЛИ!", fg="#ff5252")


if __name__ == "__main__":
    # Создаем главное окно Tkinter и запускаем приложение
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()