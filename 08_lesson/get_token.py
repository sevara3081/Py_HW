import requests

# URL для получения токена
url = "https://yougile.com/api-v2/auth/keys"

# Данные для авторизации
payload = {
    "login": "Sevara3081@mail.ru",        # Укажите ваш логин
    "password": "laguna1981",    # Укажите ваш пароль
    "companyId": "fa668f38-3605-4293-87a5-b915dbeeae53" # Укажите ID вашей компании
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
        # Получение токена
        token = response.json().get("key")
        if token:
            print(f"Ваш токен: {token}")
        else:
            print("Токен не найден в ответе:", response.json())
    except ValueError as e:
        print(f"Ошибка обработки JSON: {e}")
else:
    print(f"Ошибка: {response.status_code}, {response.text}")