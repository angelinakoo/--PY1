from random import randint

unique_numbers = []


def get_unique_list_numbers() -> list[int]:
    while len(unique_numbers) < 15:  # пока длина списка не станет равна 15 числам
        random_number = randint(-10, 10)
        # добавляем в список только те числа, которых еще не было в списке
        if random_number not in unique_numbers:
            unique_numbers.append(random_number)
    return unique_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
