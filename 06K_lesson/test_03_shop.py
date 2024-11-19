from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_purchase():
    # Настройка WebDriver
    driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH
    driver.get("https://www.saucedemo.com/")

    try:
        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавление товаров в корзину
        driver.find_element(By.XPATH,
                            "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button").click()
        driver.find_element(By.XPATH,
                            "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button").click()
        driver.find_element(By.XPATH,
                            "//div[text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button").click()

        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Checkout
        driver.find_element(By.ID, "checkout").click()

        # Заполнение формы
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        # Получение итоговой суммы
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_value = total_element.text  # Пример: "Total: $58.29"

        # Проверка итоговой суммы
        assert total_value == "Total: $58.29", f"Ожидалось 'Total: $58.29', но было '{total_value}'"

        print("Тест успешно пройден!")

    finally:
        # Закрытие браузера
        driver.quit()