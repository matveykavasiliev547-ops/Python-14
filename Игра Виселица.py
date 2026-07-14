import random
words = ["яблоко","футбол","пенал","ручка","хлеб","краб"]

while True:
    print("-" * 30)
    print("Игра - '+_Виселица_+'")

    word = random.choice(words)
    guessed_letters = []
    attempts = 10

    while attempts > 0:
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter

            else:
                display += "_"
        print(display)

        if "_" not in display:
            print("Вы победили!")
            print("-" * 30)
            break

        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Ошибка: введи ОДНУ букву, не цифру и не слово")
            continue

        if guess in guessed_letters:
            print("Такая буква уже есть!")
            continue

        elif guess in word:
            guessed_letters.append(guess)

        else:
            attempts -= 1
            print(f"Такая буква в слове отсутствует. ❤Осталось попыток: {attempts}")

        if attempts == 0:
            print(f"Вы проиграли! Слово было:{word}")
            break

    again = input("Попробовать снова? (да/нет): ")
    if again != "да":
        break
            
