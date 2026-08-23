class ClickerLogic:
    def __init__(self, initial_count: int = 50):
        self.initial_count = initial_count
        self.counter = initial_count

    def set_difficulty(self, count: int):
        """Устанавливает новое стартовое значение и сбрасывает счетчик."""
        self.initial_count = count
        self.reset()

    def decrement(self) -> int:
        """Уменьшает счетчик на 1."""
        if not self.is_victory():
            self.counter -= 1
        return self.counter

    def is_victory(self) -> bool:
        """Проверяет, достигнута ли победа."""
        return self.counter <= 0

    def reset(self):
        """Сброс состояния игры."""
        self.counter = self.initial_count