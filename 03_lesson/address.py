"""Модуль для представления адреса с почтовым индексом, городом, улицей, домом и квартирой."""


class Address:
    """Класс для представления адреса."""

    def __init__(self, postal_code: str, city: str, street: str, house: str, apartment: str):
        """Инициализация объекта адреса."""
        self.postal_code = postal_code  # Почтовый индекс
        self.city = city                # Город
        self.street = street            # Улица
        self.house = house              # Номер дома
        self.apartment = apartment      # Номер квартиры