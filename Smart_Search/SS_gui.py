import threading
import customtkinter as ctk
from SS_logic import SmartSearch

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class SmartSearchGUI:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Smart Search - Авто-Поисковик")
        self.root.geometry("480x320") # Чуть увеличили высоту
        self.root.resizable(False, False)

        self.search_engine = SmartSearch()
        self._create_widgets()

    def _create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self.root,
            text="🔍 Smarty Search",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
        )
        self.title_label.pack(pady=(20, 15))

        self.entry_query = ctk.CTkEntry(
            self.root,
            placeholder_text="Введите поисковый запрос...",
            width=380,
            height=40,
            font=ctk.CTkFont(size=14),
        )
        self.entry_query.pack(pady=10)

        # Выбор поисковика
        self.engine_var = ctk.StringVar(value="DuckDuckGo")
        self.engine_menu = ctk.CTkOptionMenu(
            self.root,
            values=["DuckDuckGo", "Google", "Yandex", "Bing"],
            variable=self.engine_var,
            width=200,
            height=35
        )
        self.engine_menu.pack(pady=10)

        self.btn_search = ctk.CTkButton(
            self.root,
            text="Найти",
            height=40,
            width=200,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#1f538d",
            hover_color="#14375e",
            command=self._start_search_thread,
        )
        self.btn_search.pack(pady=15)

        self.status_label = ctk.CTkLabel(
            self.root,
            text="Готов к работе",
            font=ctk.CTkFont(size=12),
            text_color="#a0a0a0",
        )
        self.status_label.pack(pady=5)

    def _update_status(self, message: str):
        self.status_label.configure(text=message)

    def _start_search_thread(self):
        query = self.entry_query.get().strip()
        engine = self.engine_var.get()
        
        if not query:
            self._update_status("Ошибка: Введите текст запроса!")
            return

        self.btn_search.configure(state="disabled")
        thread = threading.Thread(
            target=self._run_search, args=(query, engine), daemon=True
        )
        thread.start()

    def _run_search(self, query: str, engine: str):
        try:
            self.search_engine.run_search(
                query, engine_name=engine, status_callback=self._update_status
            )
        except Exception as e:
            self._update_status(f"Ошибка: {e}")
        finally:
            self.btn_search.configure(state="normal")