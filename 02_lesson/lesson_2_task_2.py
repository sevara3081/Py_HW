# Создаем функцию для проверки високосного года
def is_year_leap(year):
    # Проверяем, делится ли год на 4 без остатка
    if year % 4 == 0:
        return True
    else:
        return False

# Пример использования функции
year = 2024
result = is_year_leap(year)
print(f"год {year}: {result}")

# Проверка другого года
year = 2023
result = is_year_leap(year)
print(f"год {year}: {result}")