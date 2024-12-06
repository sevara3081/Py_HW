import requests

# Базовый URL и заголовки
BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "GdomAK3wJPHE15ERK+32O2Nls+uZJjFGNDCrtkrVvGvEaHzNWjmzlW1YCjZHAVzV"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


def get_all_projects():
    """Функция для получения списка всех проектов"""
    url = f"{BASE_URL}/projects"  # URL для запроса
    response = requests.get(url, headers=HEADERS)  # Отправляем GET-запрос

    if response.status_code == 200:
        print("Список проектов успешно получен!")
        projects = response.json()  # Преобразуем ответ в JSON
        return projects
    else:
        print(f"Ошибка получения списка проектов. Код ответа: {response.status_code}")
        print(f"Текст ошибки: {response.text}")
        return None


# Вызов функции
projects = get_all_projects()

# Если проекты успешно получены, выводим их на экран
if projects:
    for project in projects.get("content", []):
        print(f"ID: {project['id']}, Название: {project['title']}")