from datetime import datetime
import customtkinter as ctk
from ToDo_logic import TodoList

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class TodoGUI:

    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("480x580")
        self.root.resizable(False, False)

        self.todo = TodoList()
        self._create_widgets()
        self._refresh_task_list()

    def _create_widgets(self):
        # Заголовок
        self.title_label = ctk.CTkLabel(
            self.root,
            text="📋 Список Дел",
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
        )
        self.title_label.pack(pady=(15, 10))

        # Форма добавления задачи
        input_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        input_frame.pack(pady=5, padx=20, fill="x")

        self.entry_name = ctk.CTkEntry(
            input_frame, placeholder_text="Что нужно сделать?", width=260
        )
        self.entry_name.grid(row=0, column=0, padx=(0, 5), pady=5)

        self.entry_date = ctk.CTkEntry(
            input_frame,
            placeholder_text="ГГГГ-ММ-ДД",
            width=110,
        )
        # Подставляем сегодняшнюю дату по умолчанию
        today_str = datetime.today().strftime("%Y-%m-%d")
        self.entry_date.insert(0, today_str)
        self.entry_date.grid(row=0, column=1, padx=5, pady=5)

        self.btn_add = ctk.CTkButton(
            self.root,
            text="➕ Добавить задачу",
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self._add_task,
        )
        self.btn_add.pack(pady=5, padx=20, fill="x")

        # Метка статуса / ошибок
        self.status_label = ctk.CTkLabel(
            self.root, text="", font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(pady=2)

        # Прокручиваемый список задач
        self.scroll_frame = ctk.CTkScrollableFrame(
            self.root, width=420, height=330
        )
        self.scroll_frame.pack(pady=10, padx=20)

        # Панель управления снизу
        bottom_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        bottom_frame.pack(pady=5, padx=20, fill="x")

        self.btn_clear_done = ctk.CTkButton(
            bottom_frame,
            text="🧹 Очистить выполненные",
            fg_color="#D9534F",
            hover_color="#C9302C",
            command=self._clear_done,
        )
        self.btn_clear_done.pack(side="right")

    def _refresh_task_list(self):
        # Очищаем виджеты в списке
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        sorted_tasks = self.todo.get_sorted_tasks()

        if not sorted_tasks:
            empty_lbl = ctk.CTkLabel(
                self.scroll_frame,
                text="Список дел пуст! Время отдохнуть ☕",
                font=ctk.CTkFont(size=14),
                text_color="#A0A0A0",
            )
            empty_lbl.pack(pady=50)
            return

        for idx, task in enumerate(sorted_tasks):
            card = ctk.CTkFrame(self.scroll_frame)
            card.pack(pady=4, padx=5, fill="x")

            # Чекбокс задачи
            date_str = task.date.strftime("%d.%m.%Y")
            chk_text = f"{task.name} ({date_str})"

            chk = ctk.CTkCheckBox(
                card,
                text=chk_text,
                font=ctk.CTkFont(
                    size=13, overstrike=task.done
                ),  # Зачёркиваем если выполнено
                command=lambda i=idx: self._toggle_task(i),
            )
            if task.done:
                chk.select()
            chk.pack(side="left", padx=10, pady=8)

            # Кнопка удаления
            btn_del = ctk.CTkButton(
                card,
                text="❌",
                width=30,
                height=25,
                fg_color="transparent",
                hover_color="#505050",
                command=lambda i=idx: self._delete_task(i),
            )
            btn_del.pack(side="right", padx=5)

    def _add_task(self):
        name = self.entry_name.get().strip()
        date_str = self.entry_date.get().strip()

        if not name:
            self.status_label.configure(
                text="Введите название задачи!", text_color="#FF4D4D"
            )
            return

        try:
            self.todo.add_task(name, date_str)
            self.entry_name.delete(0, "end")
            self.status_label.configure(
                text="Задача добавлена!", text_color="#2ECC71"
            )
            self._refresh_task_list()
        except ValueError:
            self.status_label.configure(
                text="Ошибка! Формат даты: ГГГГ-ММ-ДД", text_color="#FF4D4D"
            )

    def _toggle_task(self, index: int):
        self.todo.toggle_task(index)
        self._refresh_task_list()

    def _delete_task(self, index: int):
        self.todo.delete_task(index)
        self._refresh_task_list()

    def _clear_done(self):
        self.todo.clear_done()
        self.status_label.configure(
            text="Выполненные задачи удалены!", text_color="#2ECC71"
        )
        self._refresh_task_list()