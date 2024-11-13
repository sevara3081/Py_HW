from selenium import webdriver  # Импортируем Selenium
from selenium.webdriver.common.by import By  # Импортируем метод для поиска элементов
from webdriver_manager.chrome import ChromeDriverManager  # Менеджер для скачивания драйвера Chrome
import time  # Импортируем библиотеку для паузы

# Запуск Chrome с использованием WebDriver Manager
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))

# Открытие страницы
driver.get("http://uitestingplayground.com/classattr")

# Поиск кнопки на странице по CSS-классу '.btn-primary' и клик по ней
button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()  # Нажатие на кнопку

# Ожидание 3 секунды, чтобы убедиться, что кнопка нажалась
time.sleep(3)

# Закрытие браузера
driver.quit()