import customtkinter as ctk
from Clicker_Logic import ClickerLogic

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class ClickerGUI:
    def __init__(self, root: ctk.CTk, initial_count: int = 50):
        self.root = root
        self.root.title("Clicker Game")
        self.root.geometry("380x420")
        self.root.resizable(False, False)

        self.logic = ClickerLogic(initial_count=initial_count)
        self._create_widgets()

    def _create_widgets(self):
        # Заголовок / Счетчик
        self.label = ctk.CTkLabel(
            self.root,
            text=f"Осталось кликов: {self.logic.counter}",
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
        )
        self.label.pack(pady=25)

        # Выбор сложности
        self.diff_label = ctk.CTkLabel(
            self.root,
            text="Сложность:",
            font=ctk.CTkFont(family="Segoe UI", size=12),
        )
        self.diff_label.pack(pady=(0, 5))

        self.difficulty_selector = ctk.CTkSegmentedButton(
            self.root,
            values=["25 (Легко)", "50 (Норм)", "100 (Хард)"],
            command=self._on_difficulty_change,
        )
        self.difficulty_selector.set("50 (Норм)")
        self.difficulty_selector.pack(pady=(0, 20))

        # Главная кнопка кликера
        self.click_button = ctk.CTkButton(
            self.root,
            text="КЛИКАЙ!",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            width=220,
            height=50,
            corner_radius=12,
            command=self._on_click,
        )
        self.click_button.pack(pady=10)

        # Кнопка сброса (для перезапуска)
        self.reset_button = ctk.CTkButton(
            self.root,
            text="Сбросить",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            fg_color="#4a4d50",
            hover_color="#686b6f",
            width=120,
            height=32,
            corner_radius=8,
            command=self._on_reset,
        )
        self.reset_button.pack(pady=20)

    def _on_click(self):
        remaining = self.logic.decrement()

        if self.logic.is_victory():
            self.label.configure(text="🎉 ПОБЕДА!", text_color="#6a8759")
            self.click_button.configure(state="disabled")
        else:
            self.label.configure(text=f"Осталось кликов: {remaining}")

    def _on_difficulty_change(self, value: str):
        # Извлекаем число из выбранного варианта (например, "25 (Легко)" -> 25)
        count = int(value.split()[0])
        self.logic.set_difficulty(count)
        self._update_ui_state()

    def _on_reset(self):
        self.logic.reset()
        self._update_ui_state()

    def _update_ui_state(self):
        self.label.configure(
            text=f"Осталось кликов: {self.logic.counter}",
            text_color="#ffffff",
        )
        self.click_button.configure(state="normal")