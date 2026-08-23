import customtkinter as ctk
from customtkinter import filedialog
from FS_logic import FileSorter

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class FileSorterGUI:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Сортировщик файлов по годам")
        self.root.geometry("460x320")
        self.root.resizable(False, False)

        self._create_widgets()

    def _create_widgets(self):
        # Заголовок
        self.title_label = ctk.CTkLabel(
            self.root,
            text="📁 Сортировка Файлов по Годам",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
        )
        self.title_label.pack(pady=(20, 15))

        # Выбор папки
        self.path_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.path_frame.pack(pady=10, fill="x", padx=20)

        self.entry_path = ctk.CTkEntry(
            self.path_frame,
            placeholder_text="Выберите папку...",
            width=300,
            height=35,
        )
        self.entry_path.pack(side="left", padx=(0, 10))

        self.btn_browse = ctk.CTkButton(
            self.path_frame,
            text="Обзор",
            width=100,
            height=35,
            command=self._select_folder,
        )
        self.btn_browse.pack(side="left")

        # Кнопка сортировки
        self.btn_sort = ctk.CTkButton(
            self.root,
            text="Отсортировать файлы",
            height=40,
            width=220,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#27ae60",
            hover_color="#219150",
            command=self._run_sorting,
        )
        self.btn_sort.pack(pady=20)

        # Статус
        self.status_label = ctk.CTkLabel(
            self.root,
            text="Выберите папку для начала работы",
            font=ctk.CTkFont(size=13),
            text_color="#a0a0a0",
        )
        self.status_label.pack(pady=10)

    def _select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, folder_selected)
            self.status_label.configure(
                text="Папка выбрана. Нажмите «Отсортировать»", text_color="#a0a0a0"
            )

    def _run_sorting(self):
        folder_path = self.entry_path.get().strip()

        if not folder_path:
            self.status_label.configure(text="Ошибка: Путь не выбран!", text_color="#e74c3c")
            return

        try:
            sorter = FileSorter(folder_path)
            moved_count, errors = sorter.sort_files()

            if moved_count == 0 and not errors:
                self.status_label.configure(
                    text="В папке нет файлов для сортировки", text_color="#f39c12"
                )
            else:
                msg = f"Готово! Перемещено файлов: {moved_count}"
                if errors:
                    msg += f" (Ошибок: {len(errors)})"
                self.status_label.configure(text=msg, text_color="#2aa198")

        except Exception as e:
            self.status_label.configure(text=f"Ошибка: {e}", text_color="#e74c3c")