# pylint: disable=invalid-name
"""
Этот модуль содержит функцию для определения сезона по номеру месяца.
"""
def month_to_season(month_num):
    """
        Определяет сезон на основе номера месяца.

        Параметры:
        month (int): Номер месяца (от 1 до 12).

        Возвращает:
        str: Название сезона (Зима, Весна, Лето, Осень).
        """
    if month_num in [12, 1, 2]:
        return "Зима"
    if month_num in [3, 4, 5]:
        return "Весна"
    if month_num in [6, 7, 8]:
        return "Лето"
    if month_num in [9, 10, 11]:
        return "Осень"
    return "Неверный номер месяца"

# Пример использования:
month = 2
season = month_to_season(month)
print(f"Месяц {month}: {season}")
