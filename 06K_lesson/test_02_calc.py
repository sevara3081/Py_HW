import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    # Настройка WebDriver
    driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    try:
        # Установить задержку 45 секунд
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажать кнопки 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ожидать результата "15"
        wait = WebDriverWait(driver, 50)  # Увеличиваем тайм-аут для 45 секунд задержки
        result = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        # Проверка результата
        assert result, "Результат на калькуляторе не равен 15."
        print("Тест успешно пройден!")

    finally:
        # Закрыть браузер
        driver.quit()