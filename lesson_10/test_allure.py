import allure

@allure.title("Тест авторизации на сайте")
@allure.description("Проверяем успешную авторизацию с валидными данными")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_login():
    with allure.step("Открыть страницу логина"):
        # Здесь будет код для открытия страницы
        print("Страница логина открыта")

    with allure.step("Ввести данные пользователя"):
        # Здесь вводим логин и пароль
        print("Введены данные логина и пароля")

    with allure.step("Нажать на кнопку Войти"):
        # Здесь код для клика по кнопке
        print("Кнопка 'Войти' нажата")

    with allure.step("Проверить успешный вход"):
        # Проверяем успешный вход
        assert True

@allure.title("Тест API получения данных")
@allure.description("Проверяем, что API возвращает корректный статус и данные")
@allure.feature("API")
@allure.severity(allure.severity_level.NORMAL)
def test_api():
    with allure.step("Выполнить запрос к API"):
        response = {"status_code": 200, "data": {"key": "value"}}  # Заглушка для примера
        assert response["status_code"] == 200

    with allure.step("Проверить данные ответа"):
        assert "key" in response["data"]