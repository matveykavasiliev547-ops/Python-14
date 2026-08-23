import random
import string


class PasswordGenerator:
    @staticmethod
    def generate(
        length: int,
        use_digits: bool = True,
        use_symbols: bool = True,
        use_uppercase: bool = True,
    ) -> str:
        """Генерирует надежный пароль с гарантированным наличием выбранных типов символов."""
        if length < 4:
            raise ValueError("Длина пароля должна быть не менее 4 символов")

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase if use_uppercase else ""
        digits = string.digits if use_digits else ""
        symbols = "!@#$%^&*()" if use_symbols else ""

        all_chars = lowercase + uppercase + digits + symbols
        if not all_chars:
            raise ValueError("Не выбран ни один тип символов")

        password = [random.choice(lowercase)]

        if use_uppercase:
            password.append(random.choice(uppercase))
        if use_digits:
            password.append(random.choice(digits))
        if use_symbols:
            password.append(random.choice(symbols))

        # Заполняем оставшуюся длину случайными символами из доступных
        while len(password) < length:
            password.append(random.choice(all_chars))

        random.shuffle(password)
        return "".join(password)