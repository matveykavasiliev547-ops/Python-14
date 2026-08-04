import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Pro")
        self.root.geometry("300x200")
        
        self.seconds_left = 0
        self.is_running = False

        # Заголовок
        self.label_title = tk.Label(root, text="_)=TIMER=(_", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=10)

        # Поле ввода секунд
        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.insert(0, "10") # Дефолтное значение
        self.entry.pack(pady=5)

        # Отображение времени
        self.label_time = tk.Label(root, text="00:00", font=("Arial", 24, "bold"), fg="blue")
        self.label_time.pack(pady=10)

        # Кнопка старта
        self.btn_start = tk.Button(root, text="Старт", font=("Arial", 12), command=self.start_timer)
        self.btn_start.pack(pady=5)

    def start_timer(self):
        if self.is_running:
            return # Если таймер уже идет — игнорируем повторные нажатия
            
        try:
            self.seconds_left = int(self.entry.get())
            if self.seconds_left <= 0:
                messagebox.showwarning("Ошибка", "Введите число больше 0!")
                return
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число!")
            return

        self.is_running = True
        self.btn_start.config(state="disabled") # Блокируем кнопку, чтобы не спамили
        self.update_timer()

    def update_timer(self):
        if self.seconds_left > 0:
            # Форматируем красивый вывод MM:SS
            mins, secs = divmod(self.seconds_left, 60)
            self.label_time.config(text=f"{mins:02d}:{secs:02d}")
            
            self.seconds_left -= 1
            # Главная магия Tkinter: вызвать метод update_timer снова через 1000 мс (1 сек)
            self.root.after(1000, self.update_timer)
        else:
            self.label_time.config(text="00:00")
            self.label_title.config(text="ВРЕМЯ ВЫШЛО!", fg="red")
            messagebox.showinfo("Таймер", "Время подошло к концу!")
            
            # Возвращаем всё в исходное состояние
            self.btn_start.config(state="normal")
            self.is_running = False


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
    

