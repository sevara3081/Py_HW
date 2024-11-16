from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Устанавливаем и запускаем драйвер с использованием webdriver-manager
options = Options()
# Включите эту строку, если хотите запускать браузер в режиме без интерфейса (headless)
# options.add_argument("--headless")

# Автоматически скачиваем и запускаем драйвер с использованием webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Переход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

try:
    # Явное ожидание, чтобы дождаться загрузки изображений с конкретным локатором
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container img#landscape"))
    )

    # Получаем 3-е изображение с id="landscape"
    third_image = driver.find_element(By.CSS_SELECTOR, "#image-container img#landscape")

    # Получаем значение атрибута src у 3-й картинки (индексация с 0)
    src_value = third_image.get_attribute("src")
    print(f"Значение атрибута src 3-й картинки: {src_value}")

finally:
    # Закрываем браузер
    driver.quit()