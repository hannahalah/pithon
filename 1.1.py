def is_ordered_increasing(number):
    num_str = str(number)
    for i in range(len(num_str) - 2, -1, -1):
        if num_str[i] < num_str[i + 1]:
            return False
    return True
number = int(input("Введите натуральное число: "))
if is_ordered_increasing(number):
    print("Последовательность цифр упорядочена по возрастанию при просмотре справа налево.")
else:
    print("Последовательность цифр не упорядочена по возрастанию при просмотре справа налево.")
