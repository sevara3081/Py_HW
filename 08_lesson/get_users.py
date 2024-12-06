import requests

# Базовый URL API
BASE_URL = "https://yougile.com/api-v2"

# Заголовки с токеном авторизации
HEADERS = {
    "Authorization": "Bearer GdomAK3wJPHE15ERK+32O2Nls+uZJjFGNDCrtkrVvGvEaHzNWjmzlW1YCjZHAVzV",  # Замените "ваш_токен" на реальный токен
    "Content-Type": "application/json"
}

# URL для получения списка пользователей
url = f"{BASE_URL}/users"

# Выполнение GET-запроса
response = requests.get(url, headers=HEADERS)

# Обработка ответа
if response.status_code == 200:
    # Отладочная печать для анализа структуры данных
    users_data = response.json()
    print("Ответ от сервера:", users_data)

    # Извлечение списка пользователей из ключа 'content'
    users = users_data.get('content', [])

    print("Список пользователей:")
    for user in users:
        # Используем 'realName' вместо 'name'
        print(f"ID: {user['id']}, Имя: {user.get('realName', 'Не указано')}")
else:
    print(f"Ошибка: {response.status_code}, {response.text}")