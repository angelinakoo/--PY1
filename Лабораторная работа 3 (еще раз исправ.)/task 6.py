list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_max = 0
number_max = list_numbers[index_max]

for i, current_number in enumerate(list_numbers): # перебираем пары индекс-значение
    if current_number >= number_max: # условие для нахождения максисального значения
        index_max = i
        number_max = current_number
# Меняем местами значения
list_numbers[-1], list_numbers[index_max] = list_numbers[index_max], list_numbers[-1]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
