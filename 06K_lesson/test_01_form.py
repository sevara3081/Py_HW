import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Функция для заполнения полей
def fill_field(driver, field_name, value):
    field = driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
    field.clear()
    field.send_keys(value)


# Тест
def test_01_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    fill_field(driver, "first-name", "Иван")
    fill_field(driver, "last-name", "Петров")
    fill_field(driver, "address", "Ленина, 55-3")
    fill_field(driver, "e-mail", "test@skypro.com")
    fill_field(driver, "phone", "+7985899998787")
    fill_field(driver, "zip-code", "")  # Пустое значение для zip code
    fill_field(driver, "city", "Москва")
    fill_field(driver, "country", "Россия")
    fill_field(driver, "job-position", "QA")
    fill_field(driver, "company", "SkyPro")

    # Нажатие на кнопку
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    ).click()

    # Ожидание, пока форма не обновится и поле zip-code не станет видимым
    print("Ожидаю видимость поля zip-code...")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='zip-code']"))
    )
    print("Поле zip-code стало видимым.")

    # Проверка красного поля для zip code
    alert_danger_color = "rgba(248, 215, 218, 1)"
    zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    color_zip = zip_code.value_of_css_property("background-color")
    assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    # Проверка зеленого поля для других полей
    alert_success_color = "rgba(209, 231, 221, 1)"
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field_name in fields:
        field = driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
        field_color = field.value_of_css_property("background-color")
        assert field_color == alert_success_color, f"Expected {alert_success_color} for {field_name}, but got {field_color}"