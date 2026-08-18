import random

WORDS = ["яблоко", "футбол", "пенал", "ручка", "хлеб", "краб"]

class HangmanGame:
    def __init__(self, max_attempts: int = 10):
        self.max_attempts = max_attempts
        self.word = ""
        self.guessed_letters = set()
        self.attempts = max_attempts
        self.start_new_game()

    def start_new_game(self):
        self.word = random.choice(WORDS)
        self.guessed_letters = set()
        self.attempts = self.max_attempts

    def make_guess(self, letter: str) -> dict:
        letter = letter.lower().strip()

        # Валидация ввода
        if len(letter) != 1 or not letter.isalpha():
            return {"status": "error", "message": "Введите ровно ОДНУ букву!"}

        if letter in self.guessed_letters:
            return {"status": "warning", "message": "Вы уже вводили эту букву!"}

        self.guessed_letters.add(letter)

        if letter not in self.word:
            self.attempts -= 1

        # Проверка состояния игры
        is_won = all(l in self.guessed_letters for l in self.word)
        is_lost = self.attempts <= 0

        return {
            "status": "success",
            "is_won": is_won,
            "is_lost": is_lost
        }

    @property
    def display_word(self) -> str:
        """Возвращает слово с прочерками"""
        return " ".join([l if l in self.guessed_letters else "_" for l in self.word])

    @property
    def used_letters_str(self) -> str:
        """Возвращает строку с использованными буквами"""
        if not self.guessed_letters:
            return "нет"
        return ", ".join(sorted(list(self.guessed_letters)))