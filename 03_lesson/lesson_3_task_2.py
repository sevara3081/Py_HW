"""Модуль для создания списка объектов смартфонов с использованием класса Smartphone."""

from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23", "+79234567890"),
    Smartphone("Xiaomi", "Mi 13", "+79345678901"),
    Smartphone("Huawei", "P60", "+79456789012"),
    Smartphone("Google", "Pixel 7", "+79567890123")
]

for phone in catalog:
    print(phone)
