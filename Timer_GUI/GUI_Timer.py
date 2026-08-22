import customtkinter as ctk
from Logic_Timer import TimerModel

class TimerView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Timer Pro")
        self.geometry("300x350")

        self.resizable(False, False)
        
        
        self.label_time = ctk.CTkLabel(self, text="00:00", font=("Arial", 40, "bold"))
        self.label_time.pack(pady=20)
        
        self.entry = ctk.CTkEntry(self, placeholder_text="Секунды")
        self.entry.pack(pady=10)
        
        self.btn_start = ctk.CTkButton(self, text="Старт")
        self.btn_start.pack(pady=10)