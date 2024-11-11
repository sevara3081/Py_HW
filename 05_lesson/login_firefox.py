from selenium import webdriver  # Импортируем Selenium
from selenium.webdriver.common.by import By  # Импортируем методы для поиска элементов
from selenium.webdriver.firefox.service import Service  # Импортируем Service для указания пути к драйверу
from webdriver_manager.firefox import GeckoDriverManager  # Используем WebDriverManager для GeckoDriver
import time  # Для добавления задержки

# Указываем путь к GeckoDriver через Service
service = Service(GeckoDriverManager().install())

# Запуск Firefox с использованием WebDriver Manager
driver = webdriver.Firefox(service=service)

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/login")

# Ожидание загрузки страницы (по желанию, можно улучшить с WebDriverWait)
time.sleep(2)

# Заполнение поля "Username"
username_field = driver.find_element(By.ID, "username")  # Поиск элемента по ID
username_field.send_keys("tomsmith")  # Вводим текст в поле

# Заполнение поля "Password"
password_field = driver.find_element(By.ID, "password")  # Поиск элемента по ID
password_field.send_keys("SuperSecretPassword!")  # Вводим текст в поле

# Нажатие на кнопку "Login"
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Поиск кнопки по CSS-селектору
login_button.click()  # Клик по кнопке

# Ожидание, чтобы увидеть результат
time.sleep(3)

# Закрытие браузера
driver.quit()