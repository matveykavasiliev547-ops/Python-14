import random


class GuessNumberLogic:
    def __init__(self):
        self.secret_number = 0
        self.attempts = 0
        self.max_number = 10
        self.is_game_over = False

    def start_new_game(self, max_num: int):
        """Запускает новую игру с выбранной сложностью."""
        self.max_number = max_num
        self.secret_number = random.randint(0, max_num)
        self.attempts = 0
        self.is_game_over = False

    def check_guess(self, user_guess: int) -> tuple[str, bool]:
        """
        Проверяет число пользователя.
        Возвращает tuple: (Сообщение для игрока, Выиграл ли)
        """
        if self.is_game_over:
            return "Игра завершена! Начните новую.", True

        self.attempts += 1

        if user_guess < self.secret_number:
            return "Загаданное число БОЛЬШЕ ⬆️", False
        elif user_guess > self.secret_number:
            return "Загаданное число МЕНЬШЕ ⬇️", False
        else:
            self.is_game_over = True
            return f"🎉 Победа! Вы угадали число за {self.attempts} попыток!", True