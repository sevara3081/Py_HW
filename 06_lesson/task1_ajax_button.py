from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
button.click()

# Ожидаем, пока текст "Data loaded with AJAX get request." появится в зеленой плашке
wait = WebDriverWait(driver, 20)
message = wait.until(EC.text_to_be_present_in_element((By.ID, "content"), "Data loaded with AJAX get request."))

# Печатаем текст в консоль
print("Data loaded with AJAX get request.")

# Закрываем браузер
driver.quit()