import random
from typing import Optional


class GameRules:
    CHOICES = ["камень", "ножницы", "бумага"]

    _WINNING_COMBINATIONS = {
        "камень": "ножницы",
        "бумага": "камень",
        "ножницы": "бумага",
    }

    @classmethod
    def get_winner(cls, user_move: str, bot_move: str) -> Optional[str]:
        if user_move == bot_move:
            return None
        if cls._WINNING_COMBINATIONS.get(user_move) == bot_move:
            return "user"
        return "bot"


class BotPlayer:
    @staticmethod
    def make_move() -> str:
        return random.choice(GameRules.CHOICES)