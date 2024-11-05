import pytest
from string_utils import StringUtils

# Создаем экземпляр класса для тестов
utils = StringUtils()

def test_capitalize():
    # Позитивные тесты
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("SkyPro") == "Skypro"

    # Негативные тесты
    assert utils.capitilize("") == ""  # Пустая строка
    assert utils.capitilize(" ") == " "  # Пробел

def test_trim():
    # Позитивные тесты
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro   ") == "skypro"

    # Негативные тесты
    assert utils.trim("") == ""  # Пустая строка
    assert utils.trim(" ") == ""  # Только пробел

def test_to_list():
    # Позитивные тесты
    assert utils.to_list("a,b,c") == ["a", "b", "c"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]

    # Негативные тесты
    assert utils.to_list("") == []  # Пустая строка
    assert utils.to_list(" ", ",") == [" "]  # Пробел в строке
    assert utils.to_list("a,,c", ",") == ["a", "", "c"]  # Пустое значение между разделителями

def test_contains():
    # Позитивные тесты
    assert utils.contains("SkyPro", "S") is True

    # Негативные тесты
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("", "S") is False  # Пустая строка

def test_delete_symbol():
    # Позитивные тесты
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    # Негативные тесты
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"  # Символ отсутствует
    assert utils.delete_symbol("", "Z") == ""  # Пустая строка

def test_starts_with():
    # Позитивные тесты
    assert utils.starts_with("SkyPro", "S") is True

    # Негативные тесты
    assert utils.starts_with("SkyPro", "P") is False
    assert utils.starts_with("", "S") is False  # Пустая строка

def test_end_with():
    # Позитивные тесты
    assert utils.end_with("SkyPro", "o") is True

    # Негативные тесты
    assert utils.end_with("SkyPro", "y") is False
    assert utils.end_with("", "o") is False  # Пустая строка

def test_is_empty():
    # Позитивные тесты
    assert utils.is_empty("") is True

    # Негативные тесты
    assert utils.is_empty(" ") is True  # Строка с пробелом
    assert utils.is_empty("SkyPro") is False  # Непустая строка

def test_list_to_string():
    # Позитивные тесты
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"

    # Негативные тесты
    assert utils.list_to_string([]) == ""  # Пустой список
    assert utils.list_to_string([""]) == ""  # Список с одной пустой строкой