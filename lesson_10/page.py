class LoginPage:
    def open(self) -> None:
        """Открыть страницу логина"""
        print("Страница логина открыта")

    def login(self, username: str, password: str) -> None:
        """Ввести логин и пароль, затем выполнить вход
        :param username: Имя пользователя
        :param password: Пароль пользователя
        """
        print(f"Вводим логин: {username}")
        print(f"Вводим пароль: {password}")