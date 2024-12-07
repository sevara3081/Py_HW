import requests

# URL для запроса
url = "https://yougile.com/api-v2/auth/companies"

# Данные для аутентификации
payload = {
    "login": "Sevara3081@mail.ru",        # Укажите ваш логин
    "password": "laguna1981"    # Укажите ваш пароль
}

# Заголовки
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Отправка POST-запроса
response = requests.post(url, json=payload, headers=headers)

# Обработка ответа
if response.status_code == 200:
    try:
        # Проверяем содержимое ответа
        companies = response.json()
        if isinstance(companies, list):
            print("Список компаний:")
            for company in companies:
                print(f"ID: {company['id']}, Название: {company['name']}")
        else:
            print("Ответ от сервера не является списком:", companies)
    except ValueError as e:
        print(f"Ошибка при обработке JSON: {e}")
else:
    print(f"Ошибка: {response.status_code}, {response.text}")