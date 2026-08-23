from datetime import datetime
import json
import os


class Task:

    def __init__(self, name: str, date: datetime, done: bool = False):
        self.name = name
        self.date = date
        self.done = done

    def mark_done(self):
        self.done = True

    def toggle_done(self):
        self.done = not self.done


class TodoList:

    def __init__(self, filename="Список дел.json"):
        self.tasks: list[Task] = []
        self.filename = filename
        self.load_from_file()

    def add_task(self, name: str, date_str: str):
        """Добавляет задачу с парсингом даты."""
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        self.tasks.append(Task(name, date_obj))
        self.save_to_file()

    def delete_task(self, index: int):
        """Удаляет задачу по индексу."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_to_file()

    def toggle_task(self, index: int):
        """Переключает статус выполнения задачи."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle_done()
            self.save_to_file()

    def clear_done(self):
        """Удаляет все выполненные задачи."""
        self.tasks = [t for t in self.tasks if not t.done]
        self.save_to_file()

    def get_sorted_tasks(self) -> list[Task]:
        """Возвращает отсортированный по дате список задач."""
        return sorted(self.tasks, key=lambda t: t.date)

    def save_to_file(self):
        """Сохраняет список задач в JSON."""
        data = [
            {"дело": t.name, "дата": t.date.strftime("%Y-%m-%d"), "done": t.done}
            for t in self.tasks
        ]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_from_file(self):
        """Загружает задачи из JSON, если файл существует."""
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = []
                for item in data:
                    date_obj = datetime.strptime(item["дата"], "%Y-%m-%d")
                    task = Task(
                        item["дело"], date_obj, done=item.get("done", False)
                    )
                    self.tasks.append(task)
        except Exception:
            self.tasks = []