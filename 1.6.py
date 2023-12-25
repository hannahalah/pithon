numbers = input("Введите список целых чисел через пробел: ").split()
unique_numbers = set(map(int, numbers))
unique_numbers_tuple = tuple(sorted(unique_numbers, reverse=True))
print("Кортеж уникальных элементов в обратном порядке:", unique_numbers_tuple)
