list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_last = -1
number_last = list_numbers[index_last]
index_max = 0
number_max = list_numbers[index_max]

for i, current_number in enumerate(list_numbers): # перебираем пары индекс-значение
    number_max = list_numbers[index_max]
    if current_number >= number_max: # условие для нахождения максисального значения
        index_max = i
        number_max = list_numbers[index_max]
# Меняем местами значения
list_numbers[index_last], list_numbers[index_max] = list_numbers[index_max], list_numbers[index_last]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
