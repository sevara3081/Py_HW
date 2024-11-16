from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Устанавливаем драйвер для Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Открываем сайт
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода и вводим текст
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Находим кнопку и нажимаем на неё
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Получаем текст кнопки после изменения
    button_text = button.text

    # Выводим текст кнопки в консоль
    print(button_text)

finally:
    # Закрываем браузер
    driver.quit()