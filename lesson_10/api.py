class APIClient:
    def get_data(self, url: str) -> dict:
        """Отправить GET-запрос
        :param url: URL для запроса
        :return: Ответ API в формате словаря
        """
        print(f"Выполняем запрос к {url}")
        return {"status_code": 200, "data": {"key": "value"}}