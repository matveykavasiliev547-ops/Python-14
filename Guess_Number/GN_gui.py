import customtkinter as ctk
from GN_logic import GuessNumberLogic

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class GuessNumberGUI:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Guess the Number")
        self.root.geometry("420x420")
        self.root.resizable(False, False)

        self.game = GuessNumberLogic()
        self._create_widgets()
        self._start_new_game()

    def _create_widgets(self):
        # Заголовок
        self.title_label = ctk.CTkLabel(
            self.root,
            text="🎯 Угадай Число",
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
        )
        self.title_label.pack(pady=(20, 10))

        # Выбор сложности
        self.diff_label = ctk.CTkLabel(
            self.root, text="Сложность:", font=ctk.CTkFont(size=13)
        )
        self.diff_label.pack(pady=(5, 2))

        self.diff_selector = ctk.CTkSegmentedButton(
            self.root,
            values=["0-3 (Лёгкая)", "0-10 (Средняя)", "0-100 (Сложная)"],
            command=self._on_diff_change,
        )
        self.diff_selector.set("0-10 (Средняя)")
        self.diff_selector.pack(pady=(0, 15))

        # Поле ввода
        self.entry_guess = ctk.CTkEntry(
            self.root,
            placeholder_text="Введите число...",
            width=220,
            height=40,
            font=ctk.CTkFont(size=16),
            justify="center",
        )
        self.entry_guess.pack(pady=10)
        self.entry_guess.bind("<Return>", lambda e: self._process_guess())

        # Кнопка проверки
        self.btn_check = ctk.CTkButton(
            self.root,
            text="Проверить",
            width=220,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._process_guess,
        )
        self.btn_check.pack(pady=10)

        # Вывод результатов и подсказок
        self.info_label = ctk.CTkLabel(
            self.root,
            text="Угадайте число от 0 до 10",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#3B8ED0",
        )
        self.info_label.pack(pady=15)

        # Кнопка сброса/новой игры
        self.btn_reset = ctk.CTkButton(
            self.root,
            text="Новая игра",
            width=140,
            height=30,
            fg_color="#4A4A4A",
            hover_color="#333333",
            command=self._start_new_game,
        )
        self.btn_reset.pack(pady=(10, 0))

    def _get_max_num_from_selector(self) -> int:
        selected = self.diff_selector.get()
        if "0-3" in selected:
            return 3
        elif "0-100" in selected:
            return 100
        return 10

    def _on_diff_change(self, value):
        self._start_new_game()

    def _start_new_game(self):
        max_num = self._get_max_num_from_selector()
        self.game.start_new_game(max_num)
        self.entry_guess.configure(state="normal")
        self.entry_guess.delete(0, "end")
        self.btn_check.configure(state="normal")
        self.info_label.configure(
            text=f"Загадано число от 0 до {max_num}", text_color="#3B8ED0"
        )

    def _process_guess(self):
        raw_val = self.entry_guess.get().strip()
        if not raw_val.isdigit():
            self.info_label.configure(
                text="Ошибка: введите целое число!", text_color="#FF4D4D"
            )
            return

        user_val = int(raw_val)
        message, is_win = self.game.check_guess(user_val)

        if is_win:
            self.info_label.configure(text=message, text_color="#2ECC71")
            self.btn_check.configure(state="disabled")
            self.entry_guess.configure(state="disabled")
        else:
            self.info_label.configure(text=message, text_color="#E67E22")
            self.entry_guess.delete(0, "end")