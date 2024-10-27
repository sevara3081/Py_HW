"""
Этот модуль содержит класс Smartphone, который представляет смартфон с его характеристиками.
"""

class Smartphone:
    """
    Класс Smartphone для представления смартфона.

    Атрибуты:
        brand (str): Марка телефона.
        model (str): Модель телефона.
        phone_number (str): Номер телефона.
    """

    def __init__(self, brand, model, phone_number):
        """
        Конструктор класса Smartphone.

        :param brand: Марка телефона.
        :param model: Модель телефона.
        :param phone_number: Номер телефона.
        """
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.brand} - {self.model}. {self.phone_number}"

    def make_call(self, number):
        """Симулирует исходящий вызов на указанный номер."""
        print(f"Идет вызов на {number}...")

    def send_message(self, number, message):
        """Симулирует отправку сообщения на указанный номер."""
        print(f"Отправка сообщения на {number}: {message}")