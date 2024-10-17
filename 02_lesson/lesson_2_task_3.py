import math

# Функция для вычисления площади квадрата
def square(side):
    # Вычисляем площадь
    area = side * side
    # Округляем результат вверх, если сторона не целая
    return math.ceil(area)

# Пример использования функции
side = 4.5  # Введите любую сторону квадрата
result = square(side)
print(f"Площадь квадрата со стороной {side}: {result}")