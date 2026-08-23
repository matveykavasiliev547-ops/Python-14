class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f: float) -> float:
        return (f - 32) * 5 / 9

    @staticmethod
    def celsius_to_kelvin(c: float) -> float:
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k: float) -> float:
        return k - 273.15

    @classmethod
    def convert(cls, value: float, from_unit: str, to_unit: str) -> tuple[float | None, str]:
        """Универсальная конвертация между C, F и K."""
        if from_unit == to_unit:
            return value, to_unit

        # Сначала переводим всё в Цельсии как в базовую единицу
        if from_unit == "°C":
            celsius = value
        elif from_unit == "°F":
            celsius = cls.fahrenheit_to_celsius(value)
        elif from_unit == "K":
            celsius = cls.kelvin_to_celsius(value)
        else:
            return None, ""

        # Из Цельсия переводим в целевую единицу
        if to_unit == "°C":
            return celsius, "°C"
        elif to_unit == "°F":
            return cls.celsius_to_fahrenheit(celsius), "°F"
        elif to_unit == "K":
            return cls.celsius_to_kelvin(celsius), "K"

        return None, ""