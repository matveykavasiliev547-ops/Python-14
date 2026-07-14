import os

class Calculate:
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def sub(a,b):
        return a - b

    @staticmethod
    def mul(a,b):
        return a * b

    @staticmethod
    def div(a,b):
        if b == 0:
            raise ValueError("На ноль делить нельзя!")
        return a/b

    @staticmethod
    def pow(a,b):
        return a ** b

if not os.path.exists("history_data"):
    os.makedirs("history_data")
    

while True:
    print("(=888=)_КАЛЬКУЛЯТОР_(=888=)")
    try:
        a = float(input("Введи первое число: "))
        print("-" * 30)

        op = input("Введите операцию (+,-,*,/,**):")
        print("-" * 30)
        b = float(input("Введите второе число: "))

    except ValueError:
        print("Введите числа! Ошибка! (буквы и пустые строки также не принимаются")
        continue

    try:
        if op == "+":
            print("-" * 30)
            result = Calculate.add(a,b)

        elif op == "-":
            print("-" * 30)
            result = Calculate.sub(a,b)

        elif op == "*":
            print("-" * 30)
            result = Calculate.mul(a,b)

        elif op == "/":
            print("-" * 30)
            result = Calculate.div(a,b)

        elif op == "**":
            print("-" * 30)
            result = Calculate.pow(a,b)

        else:
            print("Такой операции не существует, используй + - * / **")
            continue
  
    except ValueError as e:
        print("Ошибка", e)
        continue

    print(f"Ответ: {result}")
    with open("history_data/history.txt","a",encoding="utf-8") as file:
        file.write(f"{a} {op} {b} = {result}\n")

    again = input("Попробовать ещё раз? (да/нет): ")
    if again.lower() != "да":
        break





