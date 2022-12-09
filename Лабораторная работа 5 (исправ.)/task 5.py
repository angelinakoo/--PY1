from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(n: int) -> str:
    all_symbols = ascii_lowercase + ascii_uppercase + digits  # набор из всех символов
    # создаем строку из случайных букв и цифор
    random_password_str = "".join(sample(all_symbols, n))
    return random_password_str


print(get_random_password(8))
