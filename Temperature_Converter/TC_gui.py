import customtkinter as ctk
from TC_logic import TemperatureConverter

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class TemperatureGUI:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Конвертер температур")
        self.root.geometry("380x320")
        self.root.resizable(False, False)

        self._create_widgets()

    def _create_widgets(self):
        # Заголовок
        self.title_label = ctk.CTkLabel(
            self.root,
            text="🌡 Конвертер Температур",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
        )
        self.title_label.pack(pady=(20, 10))

        # Фрейм для выбора "ИЗ" -> "В"
        self.select_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.select_frame.pack(pady=10)

        self.from_unit = ctk.CTkOptionMenu(
            self.select_frame,
            values=["°C", "°F", "K"],
            width=80,
            command=lambda _: self._on_convert(),
        )
        self.from_unit.set("°C")
        self.from_unit.pack(side="left", padx=10)

        self.arrow_label = ctk.CTkLabel(
            self.select_frame,
            text="➔",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.arrow_label.pack(side="left")

        self.to_unit = ctk.CTkOptionMenu(
            self.select_frame,
            values=["°C", "°F", "K"],
            width=80,
            command=lambda _: self._on_convert(),
        )
        self.to_unit.set("°F")
        self.to_unit.pack(side="left", padx=10)

        # Поле ввода температуры
        self.entry_temp = ctk.CTkEntry(
            self.root,
            placeholder_text="Введите значение (напр. 36.6)",
            width=260,
            height=35,
        )
        self.entry_temp.pack(pady=15)
        self.entry_temp.bind("<KeyRelease>", lambda event: self._on_convert())

        # Результат
        self.result_label = ctk.CTkLabel(
            self.root,
            text="Результат: —",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#2aa198",
        )
        self.result_label.pack(pady=15)

    def _on_convert(self, *args):
        raw_value = self.entry_temp.get().strip().replace(",", ".")

        if not raw_value:
            self.result_label.configure(text="Результат: —", text_color="#ffffff")
            return

        try:
            val = float(raw_value)
            from_u = self.from_unit.get()
            to_u = self.to_unit.get()

            res, unit = TemperatureConverter.convert(val, from_u, to_u)
            self.result_label.configure(
                text=f"Результат: {res:.2f} {unit}",
                text_color="#2aa198",
            )
        except ValueError:
            self.result_label.configure(
                text="Ошибка! Введите число",
                text_color="#e74c3c",
            )