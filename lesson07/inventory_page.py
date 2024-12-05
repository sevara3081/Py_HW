from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_buttons = (By.XPATH, "//div[@class='inventory_item']//button")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_name):
        # Находим кнопку добавления товара по имени
        button = self.driver.find_element(By.XPATH,
                                          f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        button.click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cart_link)).click()