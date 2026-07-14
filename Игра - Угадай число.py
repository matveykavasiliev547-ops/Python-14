import random
attempts = 0

def choice_difficulty():
    while True:
        print("ИГРА - '|8_УГАДАЙ-ЧИСЛО_8|' ")
        difficulty = input("Какую сложность вы бы хотели в игре? (1. - лёгкая, 2. - средняя, 3. - сложная): ")

        if difficulty == "1":
            return 3

        elif difficulty == "2":
            return 10

        elif difficulty == "3":
            return 100

        else:
            print("Такого уровня сложности нет в моей игре!")
            continue

def play_game(max_num):
    secret = random.randint(0, max_num)
    attempts = 0
    print(f"Диапазон: 0-{max_num}")

    while True:
        try:
            guess = int(input("Угадайте число: "))

        except ValueError:
            print("Введите число!")
            continue

        attempts += 1

        if guess < secret:
            print("Загаданное число больше")

        elif guess > secret:
            print("Загаданное число меньше!")
            

        elif guess == secret:
            print("Молодцы! Вы угадали число!")
            print(f"Попыток потрачено: {attempts}")
            break

while True:
    max_number = choice_difficulty()
    play_game(max_number)
    print("-" * 30)
    again = input("Вы хотите попробовать снова? (да/нет): ").lower()
    if again != "да":
        break
    print("-" * 30)
    
    
