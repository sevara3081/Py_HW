import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage  # Импортируем класс FormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_01_form(driver):
    form_page = FormPage(driver)
    form_page.open()

    # Заполнение формы
    form_page.fill_field("first-name", "Иван")
    form_page.fill_field("last-name", "Петров")
    form_page.fill_field("address", "Ленина, 55-3")
    form_page.fill_field("e-mail", "test@skypro.com")
    form_page.fill_field("phone", "+7985899998787")
    form_page.fill_field("zip-code", "")  # Пустое значение для zip code
    form_page.fill_field("city", "Москва")
    form_page.fill_field("country", "Россия")
    form_page.fill_field("job-position", "QA")
    form_page.fill_field("company", "SkyPro")

    # Нажатие на кнопку отправки формы
    form_page.submit_form()

    # Ожидание, пока поле zip-code станет видимым
    form_page.wait_for_zip_code_field()

    # Проверка красного поля для zip code
    alert_danger_color = "rgba(248, 215, 218, 1)"
    color_zip = form_page.get_field_background_color("zip-code")
    assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    # Проверка зеленого поля для других полей
    alert_success_color = "rgba(209, 231, 221, 1)"
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field_name in fields:
        field_color = form_page.get_field_background_color(field_name)
        assert field_color == alert_success_color, f"Expected {alert_success_color} for {field_name}, but got {field_color}"


