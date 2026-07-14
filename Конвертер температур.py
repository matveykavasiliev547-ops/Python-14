def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def convert_temperature(value,direction):
    if direction == "C-F":
        return celsius_to_fahrenheit(value), "°F"

    elif direction == "F-C":
        return fahrenheit_to_celsius(value), "°C"

    else:
        return None, None


print("[|=CONVERT_TEMPERATURE=|]")

while True:

    while True:
        try:
            gradus = float(input("Введите вашу температуру: "))
            break

        except ValueError:
            print("Ошибка! Введите число (можно с точкой).")

    direction = input("В каком направлении будет перевод? (C-F или F-C): ").strip().upper()
    
    result, unit = convert_temperature(gradus, direction)

    if result is None:
        print("Неверное направление. Используйте C-F или F-C.")

    else:
        print(f"Результат: {result:.2f} {unit}")

    again = input("Вы хотите попробовать ещё раз? (да/нет): ")
    if again != "да":
        break

