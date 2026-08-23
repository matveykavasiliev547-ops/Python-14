import customtkinter as ctk
from Calc_logic import CalculatorLogic

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class CalculatorGUI:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("360x480")
        self.root.resizable(False, False)

        self.logic = CalculatorLogic()
        self.current_expression = ""

        self._create_widgets()

    def _create_widgets(self):
        # Дисплей для ввода и вывода
        self.display = ctk.CTkEntry(
            self.root,
            width=320,
            height=60,
            font=ctk.CTkFont(size=24, weight="bold"),
            justify="right",
        )
        self.display.pack(pady=(20, 10), padx=20)

        # Метка статуса / ошибок
        self.status_label = ctk.CTkLabel(
            self.root,
            text="Готов к вычислениям",
            font=ctk.CTkFont(size=12),
            text_color="#A0A0A0",
        )
        self.status_label.pack(pady=(0, 10))

        # Фрейм для сетки кнопок
        grid_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        grid_frame.pack(pady=10)

        # Раскладка кнопок
        buttons = [
            ("C", 0, 0, "#D9534F"),
            ("**", 0, 1, "#2E4053"),
            ("/", 0, 2, "#2E4053"),
            ("*", 0, 3, "#2E4053"),
            ("7", 1, 0, None),
            ("8", 1, 1, None),
            ("9", 1, 2, None),
            ("-", 1, 3, "#2E4053"),
            ("4", 2, 0, None),
            ("5", 2, 1, None),
            ("6", 2, 2, None),
            ("+", 2, 3, "#2E4053"),
            ("1", 3, 0, None),
            ("2", 3, 1, None),
            ("3", 3, 2, None),
            ("=", 3, 3, "#1F538D"),
            ("0", 4, 0, None),
            (".", 4, 1, None),
        ]

        for text, row, col, color in buttons:
            cmd = lambda t=text: self._on_button_click(t)

            btn = ctk.CTkButton(
                grid_frame,
                text=text,
                width=70,
                height=50,
                font=ctk.CTkFont(size=18, weight="bold"),
                fg_color=color if color else "#3B3B3B",
                hover_color="#505050" if not color else None,
                command=cmd,
            )
            btn.grid(row=row, column=col, padx=4, pady=4)

    def _on_button_click(self, char: str):
        if char == "C":
            self.current_expression = ""
            self.display.delete(0, "end")
            self.status_label.configure(text="Очищено", text_color="#A0A0A0")
        elif char == "=":
            self._calculate_result()
        else:
            self.current_expression += str(char)
            self.display.delete(0, "end")
            self.display.insert(0, self.current_expression)

    def _calculate_result(self):
        try:
            expr = self.display.get().strip()
            if not expr:
                return

            # Ищем оператор в выражении
            op_found = None
            for op in ["**", "+", "-", "*", "/"]:
                if op in expr:
                    op_found = op
                    break

            if not op_found:
                self.status_label.configure(
                    text="Введите операцию (+, -, *, /, **)", text_color="#FF4D4D"
                )
                return

            parts = expr.split(op_found)
            if len(parts) != 2 or not parts[0] or not parts[1]:
                self.status_label.configure(
                    text="Некорректное выражение", text_color="#FF4D4D"
                )
                return

            a = float(parts[0])
            b = float(parts[1])

            res = self.logic.execute_operation(a, op_found, b)

            # Форматируем результат (убираем .0 у целых чисел)
            res_str = f"{res:g}"

            self.display.delete(0, "end")
            self.display.insert(0, res_str)
            self.current_expression = res_str
            self.status_label.configure(
                text="Сохранено в историю!", text_color="#2ECC71"
            )

        except ValueError as e:
            self.status_label.configure(text=f"Ошибка: {e}", text_color="#FF4D4D")
        except Exception:
            self.status_label.configure(text="Ошибка вычисления!", text_color="#FF4D4D")