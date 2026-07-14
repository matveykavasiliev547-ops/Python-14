import random
def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    symbols = "!@#$%^&*()"
    letters_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    all_chars = digits + letters + letters_big + symbols
    password = []

    password.append(random.choice(letters))
    password.append(random.choice(letters_big))
    password.append(random.choice(digits))
    password.append(random.choice(symbols))

    for i in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)



while True:
    print("-GENERATE-|-PASSWORD-")
    data = input("Введите длину пароля (должно быть не менее 5): ")

    try:
        length = int(data)
        

        if length >= 5:

            password = generate_password(lenght)
            print(f"Ваш новый пароль:{password}")

        else:
            print("Слишком мало. Введите длину не менее 5.")

    except ValueError:
        print("Пожалуйста, введите число!")

    again = input("Вы хотите переписать пароль? (да/нет): ")
    if again.lower() != "да":
        break

    
