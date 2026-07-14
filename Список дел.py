import json
from datetime import datetime

class Task:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = '[V]' if self.done else '[X]'
        return f"{status} {self.name} - {self.date.strftime('%d.%m.%Y')}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        self.tasks.append(Task(name, date_obj))

    def show_tasks(self):
        if not self.tasks:
            print("Список дел пуст.")

        else:
            for task in sorted(self.tasks, key=lambda t: t.date):
                print(task)

    def mark_done_by_name(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_done()
                print(f"Задача '{name}' выполнена!")
                return
        print(f"Задача '{name}' не найдена.")

    def clear_done(self):
        self.tasks = [task for task in self.tasks if not task.done]
        print("Выполненные задачи удалены.")

    def save_to_file(self, filename="Список дел.json"):
        data = [{"дело": t.name, "дата": t.date.isoformat(), "done": t.done} for t in self.tasks]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Сохранено!")

my_todo = TodoList()
        
    
while True:
    print("-||-TO-||-DO-||-LIST-||-")
    print("-" * 30)
    print("\nПриветствую вас! Это программа под названием 'список дел'!")
    print("Тут вы сможете добавить свои дела, удалить, отметить выполненные, сохранить или показать")
    print("Первым делом если вы хотите добавить в список дела напишите добавить")

    command = input("Введите команду: ")

    if command.startswith("добавить"):
        task_name = command[8:].strip()
        task_date_str = input("Введите дату (ГГГГ-ММ-ДД): ")
        print("-" * 30)

        try:
            my_todo.add_task(task_name, task_date_str)
        except ValueError:
            print("Неверный формат даты! Используй ГГГГ-ММ-ДД")
            continue

        print(f"Задача '{task_name}' добавлена!")

    elif command.startswith("выполнить"):
        task_name = command[9:].strip()
        my_todo.mark_done_by_name(task_name)
        print("-" * 30)
        

    elif command == "показать":
         print("---СПИСОК ВАШИХ ДЕЛ---")
         my_todo.show_tasks()
         print("-" * 30)
        

    elif command.startswith("очистить"):
        my_todo.clear_done()
        print("Список успешно очищен!")

    elif command == "сохранить":
        my_todo.save_to_file()
        print("Сохранение прошло успешно!")

    elif command == "выход":
        break


        
        
        
        
