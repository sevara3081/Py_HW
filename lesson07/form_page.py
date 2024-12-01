from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):  # Исправлено название метода на __init__
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(15)  # Установка ожидания для всех элементов

    def fill_form(self, first_name, last_name, address, e_mail, phone, city, country, job_position, company):
        """Метод для заполнения формы"""
        self._driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self._driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self._driver.find_element(By.NAME, "address").send_keys(address)
        self._driver.find_element(By.NAME, "e-mail").send_keys(e_mail)
        self._driver.find_element(By.NAME, "phone").send_keys(phone)
        self._driver.find_element(By.NAME, "city").send_keys(city)
        self._driver.find_element(By.NAME, "country").send_keys(country)
        self._driver.find_element(By.NAME, "job-position").send_keys(job_position)
        self._driver.find_element(By.NAME, "company").send_keys(company)

        # Нажимаем на кнопку "Отправить"
        submit_button = WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

        # Проверяем наличие нового элемента, чтобы удостовериться в завершении операции
        WebDriverWait(self._driver, 30).until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )