"""
Модуль для проверки високосного года.
"""

def is_year_leap(year):
    """
    Проверяет, является ли год високосным.

    :param year: Год для проверки
    :return: True, если год високосный, иначе False
    """
    # Проверяем, делится ли год на 4 без остатка
    return year % 4 == 0

# Пример использования функции
year_value = 2024
result_value = is_year_leap(year_value)
print(f"год {year_value}: {result_value}")

# Проверка другого года
year_value = 2023
result_value = is_year_leap(year_value)
print(f"год {year_value}: {result_value}")
