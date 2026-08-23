import customtkinter as ctk
from PG_logic import PasswordGenerator

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class PasswordGUI:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Генератор паролей")
        self.root.geometry("400x420")
        self.root.resizable(False, False)

        self._create_widgets()
        self._generate_password()

    def _create_widgets(self):
        # Заголовок
        self.title_label = ctk.CTkLabel(
            self.root,
            text="🔑 Генератор Паролей",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
        )
        self.title_label.pack(pady=(20, 15))

        # Поле вывода пароля
        self.entry_password = ctk.CTkEntry(
            self.root,
            width=280,
            height=40,
            font=ctk.CTkFont(size=16, weight="bold"),
            justify="center",
        )
        self.entry_password.pack(pady=10)

        # Слайдер длины пароля
        self.length_label = ctk.CTkLabel(
            self.root, text="Длина пароля: 12", font=ctk.CTkFont(size=14)
        )
        self.length_label.pack(pady=(10, 0))

        self.slider_length = ctk.CTkSlider(
            self.root,
            from_=4,
            to=32,
            number_of_steps=28,
            command=self._on_slider_change,
        )
        self.slider_length.set(12)
        self.slider_length.pack(pady=10)

        # Чекбоксы настроек
        self.var_digits = ctk.BooleanVar(value=True)
        self.var_symbols = ctk.BooleanVar(value=True)
        self.var_upper = ctk.BooleanVar(value=True)

        self.cb_digits = ctk.CTkCheckBox(
            self.root, text="Включать цифры (0-9)", variable=self.var_digits, command=self._generate_password
        )
        self.cb_digits.pack(anchor="w", padx=60, pady=5)

        self.cb_symbols = ctk.CTkCheckBox(
            self.root, text="Спецсимволы (!@#$%^&*)", variable=self.var_symbols, command=self._generate_password
        )
        self.cb_symbols.pack(anchor="w", padx=60, pady=5)

        self.cb_upper = ctk.CTkCheckBox(
            self.root, text="Заглавные буквы (A-Z)", variable=self.var_upper, command=self._generate_password
        )
        self.cb_upper.pack(anchor="w", padx=60, pady=5)

        # Кнопки
        self.btn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.btn_frame.pack(pady=20)

        self.btn_generate = ctk.CTkButton(
            self.btn_frame, text="Сгенерировать", width=130, command=self._generate_password
        )
        self.btn_generate.pack(side="left", padx=5)

        self.btn_copy = ctk.CTkButton(
            self.btn_frame,
            text="Скопировать",
            width=130,
            fg_color="#27ae60",
            hover_color="#219150",
            command=self._copy_to_clipboard,
        )
        self.btn_copy.pack(side="left", padx=5)

    def _on_slider_change(self, value):
        length = int(value)
        self.length_label.configure(text=f"Длина пароля: {length}")
        self._generate_password()

    def _generate_password(self):
        try:
            length = int(self.slider_length.get())
            pwd = PasswordGenerator.generate(
                length=length,
                use_digits=self.var_digits.get(),
                use_symbols=self.var_symbols.get(),
                use_uppercase=self.var_upper.get(),
            )
            self.entry_password.delete(0, "end")
            self.entry_password.insert(0, pwd)
            self.btn_copy.configure(text="Скопировать", fg_color="#27ae60")
        except ValueError:
            self.entry_password.delete(0, "end")
            self.entry_password.insert(0, "Выберите типы символов")

    def _copy_to_clipboard(self):
        pwd = self.entry_password.get()
        if pwd and pwd != "Выберите типы символов":
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            self.btn_copy.configure(text="Скопировано! ✓", fg_color="#2980b9")