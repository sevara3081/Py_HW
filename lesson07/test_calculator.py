import pytest
from selenium import webdriver
from lesson07.calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)

    try:
        # Открытие страницы
        calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Установка задержки
        calculator_page.set_delay("45")

        # Выполнение операций 7 + 8 =
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

        # Проверка результата
        result = calculator_page.get_result("15")
        assert result == "15", "Результат на калькуляторе не равен 15."
        print("Тест успешно пройден!")

    finally:
        # Закрытие браузера
        driver.quit()