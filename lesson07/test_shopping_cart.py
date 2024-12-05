from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop_purchase():
    driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH
    driver.get("https://www.saucedemo.com/")

    try:
        # Авторизация
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Страница товаров
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_product_to_cart("Sauce Labs Onesie")

        # Переход в корзину
        inventory_page.go_to_cart()

        # Страница корзины
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

        # Страница оформления заказа
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form("John", "Doe", "12345")

        # Проверка итоговой суммы
        total_value = checkout_page.get_total()
        assert total_value == "Total: $58.29", f"Ожидалось 'Total: $58.29', но было '{total_value}'"

        print("Тест успешно пройден!")

    finally:
        # Закрытие браузера
        driver.quit()