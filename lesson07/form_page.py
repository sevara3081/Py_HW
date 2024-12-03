from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_field(self, field_name, value):
        field = self.driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
        field.clear()
        field.send_keys(value)

    def submit_form(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        ).click()

    def wait_for_zip_code_field(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='zip-code']"))
        )

    def get_field_background_color(self, field_name):
        field = self.driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
        return field.value_of_css_property("background-color")