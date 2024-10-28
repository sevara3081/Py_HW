"""Создание и вывод данных о почтовом отправлении."""

from address import Address
from mailing import Mailing

# Создаем адрес отправителя и получателя
to_address = Address("115172", "Москва", "Большие Каменщики", "19", "26")
from_address = Address("143989", "Балашиха", "Некрасова", "10", "65")

# Создаем почтовое отправление
mailing = Mailing(to_address=to_address, from_address=from_address, cost=250.0, track="TR123456789RU")

# Вывод данных об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.postal_code}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.postal_code}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")