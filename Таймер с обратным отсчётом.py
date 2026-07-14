import time

while True:
    print("_)=TIMER=(_")
    try:
        seconds = int(input("Введите секунды: "))

    except ValueError:
        print("Ошибка! Введите цифру!")
        continue
    
    while seconds > 0:
        print("-" * 20)
        print(f"Осталось: {seconds} секунд!")
        time.sleep(1)
        seconds -= 1
    
    print("Время подошло к концу!")

    again = input("Вы хотите попробовать снова? (да/нет): ")
    if again.lower() != "да":
        break
    
    

