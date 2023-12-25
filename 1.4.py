def count_numbers(string):
    num_count = {}
    for char in string:
        if char.isdigit():
            num = int(char)
            num_count[num] = num_count.get(num, 0) + 1
    return num_count

string = input("Введите строку из чисел от 0 до 9: ")
result = count_numbers(string)
print("Результат:")
for key, value in result.items():
    print(f"Цифра {key}: {value} раз(а)")
