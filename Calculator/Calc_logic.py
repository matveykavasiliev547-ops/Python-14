import os

class Calculate:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def sub(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def mul(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def div(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("На ноль делить нельзя!")
        return a / b

    @staticmethod
    def pow(a: float, b: float) -> float:
        return a ** b

class CalculatorLogic:
    def __init__(self, history_dir: str = "history_data"):
        self.history_dir = history_dir
        self.history_file = os.path.join(self.history_dir, "history.txt")
        self._ensure_history_dir()

    def _ensure_history_dir(self):
        if not os.path.exists(self.history_dir):
            os.makedirs(self.history_dir)

    def save_history(self, a: float, op: str, b: float, result: float):
        """Записывает математическое выражение и результат в историю."""
        with open(self.history_file, "a", encoding="utf-8") as file:
            file.write(f"{a} {op} {b} = {result}\n")

    def execute_operation(self, a: float, op: str, b: float) -> float:
        """Выполняет вычисление в зависимости от оператора."""
        if op == "+":
            res = Calculate.add(a, b)
        elif op == "-":
            res = Calculate.sub(a, b)
        elif op == "*":
            res = Calculate.mul(a, b)
        elif op == "/":
            res = Calculate.div(a, b)
        elif op == "**":
            res = Calculate.pow(a, b)
        else:
            raise ValueError(f"Неизвестная операция '{op}'")

        self.save_history(a, op, b, res)
        return res