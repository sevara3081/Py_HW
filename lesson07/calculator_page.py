from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_screen = (By.CLASS_NAME, "screen")
        self.buttons = {
            "7": (By.XPATH, "//span[text()='7']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "=": (By.XPATH, "//span[text()='=']")
        }

    def open(self, url):
        """Открыть указанную страницу."""
        self.driver.get(url)

    def set_delay(self, delay):
        """Установить задержку."""
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(delay)

    def click_button(self, label):
        """Нажать на кнопку с указанной надписью."""
        self.driver.find_element(*self.buttons[label]).click()

    def get_result(self, expected_result, timeout=50):
        """Получить результат с ожиданием."""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.result_screen, expected_result))
        return self.driver.find_element(*self.result_screen).text