from random import randint


def get_unique_list_numbers(start: int, end: int, length: int) -> list[int]:
    unique_numbers = []
    while len(unique_numbers) < length:  # пока список не достигнет заданной длины
        random_number = randint(start, end)
        # добавляем в список только те числа, которых еще не было в списке
        if random_number not in unique_numbers:
            unique_numbers.append(random_number)
    return unique_numbers


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
