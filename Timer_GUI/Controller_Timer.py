from tkinter import messagebox

class TimerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.btn_start.configure(command=self.start_timer)

    def start_timer(self):
        if self.model.is_running:
            return 
        try:
            val = int(self.view.entry.get())
            if val <= 0: return

            self.model.set_time(val)

            self.view.btn_start.configure(state="disabled")

            self.update_loop()
        except ValueError:
            messagebox.showwarning("Ошибка ввода", "Пожалуйста, введите целое число секунд! (не буквами)")

    def update_loop(self):
        if self.model.is_running:
            can_continue = self.model.tick()
            mins, secs = divmod(self.model.seconds_left, 60)
            self.view.label_time.configure(text=f"{mins:02d}:{secs:02d}")

            
            if can_continue:
                self.view.after(1000, self.update_loop)

            else:
                self.view.btn_start.configure(state="normal")