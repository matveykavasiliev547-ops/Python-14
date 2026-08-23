import customtkinter as ctk
from SSP_Logic import GameRules, BotPlayer

# Настройка темы интерфейса
ctk.set_appearance_mode("Dark")  # Варианты: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Варианты: "blue", "green", "dark-blue"


class RockPaperScissorsGUI:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Камень • Ножницы • Бумага")
        self.root.geometry("450x450")
        self.root.resizable(False, False)

        self.bot = BotPlayer()
        self._create_widgets()

    def _create_widgets(self):
        # Заголовок
        title_label = ctk.CTkLabel(
            self.root,
            text="Камень • Ножницы • Бумага",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
        )
        title_label.pack(pady=20)

        # Табло с выбором бота
        self.bot_choice_label = ctk.CTkLabel(
            self.root,
            text="Бот ждёт твоего хода...",
            font=ctk.CTkFont(family="Segoe UI", size=14),
            fg_color="#3c3f41",
            corner_radius=8,
            width=300,
            height=40,
        )
        self.bot_choice_label.pack(pady=10)

        # Результат раунда
        self.result_label = ctk.CTkLabel(
            self.root,
            text="Сделай выбор ниже!",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color="#e8e8e8",
        )
        self.result_label.pack(pady=25)

        # Контейнер для кнопок
        buttons_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        buttons_frame.pack(pady=10)

        moves = [("💎 Камень", "камень"), ("✂ Ножницы", "ножницы"), ("📄 Бумага", "бумага")]

        for text, move in moves:
            btn = ctk.CTkButton(
                buttons_frame,
                text=text,
                font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
                width=110,
                height=40,
                corner_radius=10,
                command=lambda m=move: self._play_round(m),
            )
            btn.pack(side="left", padx=5)

        # Кнопка выхода
        exit_btn = ctk.CTkButton(
            self.root,
            text="Выйти из игры",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            fg_color="#8b0000",
            hover_color="#a52a2a",
            width=150,
            height=35,
            corner_radius=8,
            command=self.root.quit,
        )
        exit_btn.pack(pady=30)

    def _play_round(self, user_move: str):
        bot_move = self.bot.make_move()
        self.bot_choice_label.configure(text=f"Бот выбрал: {bot_move.capitalize()}")

        winner = GameRules.get_winner(user_move, bot_move)

        if winner is None:
            self.result_label.configure(text="🤝 НИЧЬЯ!", text_color="#ffc66d")
        elif winner == "user":
            self.result_label.configure(text="🎉 ВЫ ПОБЕДИЛИ!", text_color="#6a8759")
        else:
            self.result_label.configure(text="💀 ВЫ ПРОИГРАЛИ!", text_color="#ff5252")