import urllib.parse
import webbrowser
from datetime import datetime

class SmartSearch:
    def __init__(self, history_file: str = "history_search.txt"):
        self.history_file = history_file
        # Словарь с поисковиками
        self.engines = {
    "DuckDuckGo": "https://duckduckgo.com/?q={}",
    "Google": "https://www.google.ru/search?q={}&hl=ru&gl=ru",
    "Yandex": "https://yandex.ru/search/?text={}",
    "Bing": "https://www.bing.com/search?q={}&setlang=ru"
}

    def _save_history(self, request: str, engine: str):
        current_date = datetime.now().strftime("%d.%m.%Y %H:%M")
        with open(self.history_file, "a", encoding="utf-8") as f:
            f.write(f"[{engine}] '{request}': запрос был сделан - {current_date}\n")

    def run_search(self, request: str, engine_name: str, status_callback=None):
        if not request.strip():
            raise ValueError("Запрос не может быть пустым")

        if engine_name not in self.engines:
            raise ValueError("Выбран неизвестный поисковик")

        if status_callback:
            status_callback(f"Формирование ссылки для {engine_name}...")

        encoded_query = urllib.parse.quote(request)
        # Подставляем закодированный запрос в шаблон выбранного поисковика
        url = self.engines[engine_name].format(encoded_query)

        if status_callback:
            status_callback("Открытие браузера...")

        webbrowser.open(url)
        self._save_history(request, engine_name)

        if status_callback:
            status_callback("Запрос успешно отправлен!")