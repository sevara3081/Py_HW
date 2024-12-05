from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


def test_01_form():
    # Настройка WebDriver
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Создаём объект класса FormPage
        form_page = FormPage(browser)

        # Вызываем метод для заполнения формы
        form_page.fill_form(
            first_name="Иван",
            last_name="Петров",
            address="Ленина, 55-3",
            e_mail="test@skypro.com",
            phone="+7985899998787",
            city="Москва",
            country="Россия",
            job_position="QA",
            company="SkyPro"
        )
    finally:
        # Закрываем браузер
        browser.quit()