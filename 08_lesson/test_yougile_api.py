import requests

BASE_URL = "https://yougile.com/api-v2"  # Замените на ваш URL
YOUR_ACCESS_TOKEN = "GdomAK3wJPHE15ERK+32O2Nls+uZJjFGNDCrtkrVvGvEaHzNWjmzlW1YCjZHAVzV"  # Замените на ваш токен

HEADERS = {
    "Authorization": f"Bearer {YOUR_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}


# Функция для создания проекта и получения его ID
def create_project(title):
    """Создает проект и возвращает его ID."""
    url = f"{BASE_URL}/projects"
    payload = {"title": title}  # Теперь создаем проект без description
    response = requests.post(url, json=payload, headers=HEADERS)

    # Проверка успешности запроса
    if response.status_code == 201:
        print(f"Проект создан: {response.json()}")
        return response.json().get('id')  # Получаем ID проекта из ответа
    else:
        raise Exception(f"Ошибка при создании проекта: {response.status_code}, {response.text}")


# Тест на создание проекта
def test_create_project():
    """Тест на создание проекта."""
    url = f"{BASE_URL}/projects"
    payload = {"title": "Тестовый проект"}
    response = requests.post(url, json=payload, headers=HEADERS)

    assert response.status_code == 201, f"Ошибка: {response.status_code}, {response.text}"
    print("Проект создан успешно")


# Тест на получение всех проектов
def test_get_all_projects():
    """Тест на получение всех проектов."""
    url = f"{BASE_URL}/projects"
    response = requests.get(url, headers=HEADERS)

    assert response.status_code == 200, f"Ошибка: {response.status_code}, {response.text}"
    print("Проекты получены успешно")


# Тест на обновление проекта
def test_update_project():
    """Тест на обновление проекта."""
    TEST_PROJECT_ID = create_project("Проект для обновления")  # Получаем ID проекта без description
    url = f"{BASE_URL}/projects/{TEST_PROJECT_ID}"
    payload = {"title": "Обновленный проект"}  # Обновление только поля title
    response = requests.put(url, json=payload, headers=HEADERS)

    assert response.status_code == 200, f"Ошибка: {response.status_code}, {response.text}"
    print("Проект обновлен успешно")


# Тест на создание проекта без поля title
def test_create_project_without_title():
    """Тест на обязательность поля title при создании проекта."""
    url = f"{BASE_URL}/projects"
    payload = {"description": "Описание без названия"}  # Без title
    response = requests.post(url, json=payload, headers=HEADERS)

    assert response.status_code == 400, f"Ошибка: {response.status_code}, {response.text}"
    print("Проект без title возвращает ошибку 400")


# Тест на создание проекта без поля description
def test_create_project_without_description():
    """Тест на создание проекта без поля description."""
    url = f"{BASE_URL}/projects"
    payload = {"title": "Проект без описания"}  # description можно опустить
    response = requests.post(url, json=payload, headers=HEADERS)

    assert response.status_code == 201, f"Ошибка: {response.status_code}, {response.text}"
    print("Проект без description создан успешно")


# Тест на обновление проекта без поля title
def test_update_project_without_title():
    """Тест на обязательность поля title при обновлении проекта."""
    TEST_PROJECT_ID = create_project("Проект для обновления")  # Получаем ID проекта без description
    url = f"{BASE_URL}/projects/{TEST_PROJECT_ID}"
    payload = {"description": "Описание без названия"}  # Без title
    response = requests.put(url, json=payload, headers=HEADERS)

    assert response.status_code == 400, f"Ошибка: {response.status_code}, {response.text}"
    print("Обновление проекта без title возвращает ошибку 400")


if __name__ == "__main__":
    # Вызов тестов
    test_create_project()
    test_get_all_projects()
    test_update_project()
    test_create_project_without_title()
    test_create_project_without_description()
    test_update_project_without_title()