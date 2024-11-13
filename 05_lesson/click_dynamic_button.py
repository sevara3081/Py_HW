from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Инициализация драйвера
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))

# Открытие страницы
driver.get("http://uitestingplayground.com/dynamicid")

# Клик по кнопке
button = driver.find_element(By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]")
button.click()

# Пауза для просмотра результата
time.sleep(3)

# Закрытие браузера
driver.quit()