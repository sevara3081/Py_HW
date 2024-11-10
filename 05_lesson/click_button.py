from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Импортируем By

# Настроим опции для Chrome
options = Options()
# options.add_argument('--headless')  # Если нужно запускать в headless-режиме

# Устанавливаем сервис для WebDriver
service = Service(ChromeDriverManager().install())

# Запускаем браузер с сервисом и опциями
driver = webdriver.Chrome(service=service, options=options)

# Переходим на страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Находим кнопку и кликаем по ней 5 раз
for _ in range(5):
    driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()

# Собираем все кнопки Delete на странице
delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')

# Выводим размер списка
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

# Закрываем браузер
driver.quit()