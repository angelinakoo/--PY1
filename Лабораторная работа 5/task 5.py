from random import sample
import string


letter_lower = string.ascii_lowercase  # буквы нижнего регистра
letter_upper = string.ascii_uppercase  # буквы верхнего регистра
number = string.digits  # цифры
all_symbols = letter_lower + letter_upper + number


def get_random_password() -> str:
    # создаем строку из случайных букв и цифор длиной в 8 символов
    random_password_str = "".join(sample(all_symbols, 8))
    return random_password_str


print(get_random_password())
