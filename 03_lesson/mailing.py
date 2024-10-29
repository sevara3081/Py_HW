"""Модуль с классом Mailing для представления почтового отправления."""

from address import Address

class Mailing:
    """Класс для представления почтового отправления."""

    def __init__(self, to_address, from_address, cost, track):
        """
        Инициализирует объект почтового отправления.

        Параметры:
            to_address (Address): адрес получателя.
            from_address (Address): адрес отправителя.
            cost (float): стоимость отправления.
            track (str): трек-номер.
        """
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track