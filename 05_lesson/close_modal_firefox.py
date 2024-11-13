from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

# Настроим веб-драйвер для Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Даем время на загрузку страницы
time.sleep(2)

# Находим кнопку "Close"
close_button = driver.find_element(By.XPATH, '//div[@class="modal-footer"]/p')

# Прокручиваем страницу до кнопки, чтобы она стала доступна
driver.execute_script("arguments[0].scrollIntoView(true);", close_button)

# Теперь кликаем по кнопке
close_button.click()

# Ожидаем несколько секунд, чтобы убедиться, что модальное окно закрыто
time.sleep(2)

# Закрываем браузер
driver.quit()