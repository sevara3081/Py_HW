"""
Этот модуль содержит классы и функции для работы с пользователями.

Класс User:
    Представляет пользователя с именем и фамилией.

    Атрибуты:
        first_name (str): Имя пользователя.
        last_name (str): Фамилия пользователя.

    Методы:
        print_first_name(): Выводит имя пользователя.
        print_last_name(): Выводит фамилию пользователя.
        print_full_name(): Выводит полное имя пользователя (имя и фамилия).
"""

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        """Выводит имя пользователя."""
        print(self.first_name)

    def print_last_name(self):
        """Выводит фамилию пользователя."""
        print(self.last_name)

    def print_full_name(self):
        """Выводит полное имя пользователя (имя и фамилия)."""
        print(f"{self.first_name} {self.last_name}")
