from address import Address
from mailing import Mailing

to_address = Address(123456, "Sankt-Peterburg", "Prospect Toreza", 45, 50)
from_address = Address(165432, "Batumi", "Lermontova", 50, 65)
my_mailing = Mailing(to_address, from_address, 5000, "Отправление")

my_mailing.departure()
