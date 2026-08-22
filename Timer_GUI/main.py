# main.py
from Logic_Timer import TimerModel
from GUI_Timer import TimerView
from Controller_Timer import TimerController

def main():
    # 1. Инициализируем модель (данные)
    model = TimerModel()
    
    # 2. Инициализируем интерфейс (вью)
    view = TimerView()
    
    # 3. Инициализируем контроллер (логика управления), 
    # который берет на себя связку модели и интерфейса
    controller = TimerController(model, view)
    
    # 4. Запускаем приложение
    view.mainloop()

if __name__ == "__main__":
    main()