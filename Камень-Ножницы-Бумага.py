import random
choices = ["камень","ножницы","бумага"]

while True:
    print("-" * 30)
    print("(|=|)_КАМЕНЬ-ножницы-БУМАГА_(|=|)")
    print("Не стоит говорить о правилах, они и так многим предельно ясны!")

    choice = input("Сделайте выбор (камень/ножницы/бумага): ").lower()
    
    computer_choice = random.choice(choices)

    if choice not in choices:
        print("Такого варианта нет. Давай ещё раз.")
        continue

    print("-" * 30)
    computer_choice = random.choice(choices)
    print("Итак мой ход!")
    print(computer_choice)

    if choice == computer_choice:
        print("Это ничья!")

    elif(choice == "камень" and computer_choice == "ножницы") or(choice == "бумага" and computer_choice == "камень")or(choice == "ножницы" and computer_choice == "бумага"):
         print("Я проиграл! Ваша победа!")

    else:
        print("Похоже на то что вы... Проиграли! Не печальтесь, вы сможете попробовать заново")

    print("-" * 30)
    again = input("Вы хотите попробовать сыграть заново? (да/нет): ")
    if again != "да":
        print("Спасибо за игру! Заходите поиграть ещё!")
        break
    
    
        
