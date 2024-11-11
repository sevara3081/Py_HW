from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# 1. Настроим драйвер Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# 2. Откроем страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# 3. Найдем поле ввода
input_field = driver.find_element(By.XPATH, '//input[@type="number"]')

# 4. Вводим в поле текст "1000"
input_field.send_keys("1000")
time.sleep(1)  # Пауза, чтобы увидеть результат

# 5. Очищаем поле
input_field.clear()
time.sleep(1)  # Пауза, чтобы увидеть результат

# 6. Вводим текст "999"
input_field.send_keys("999")
time.sleep(1)  # Пауза, чтобы увидеть результат

# 7. Закрываем браузер
driver.quit()