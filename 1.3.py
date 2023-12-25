def count_equal_pairs(numbers):
    num_counts = {}
    pair_count = 0
    for num in numbers:
        if num in num_counts:
            pair_count += num_counts[num]
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    return pair_count
numbers = input("Введите список чисел через пробел: ").split()
numbers = [int(num) for num in numbers]
pairs = count_equal_pairs(numbers)
print(f"Количество пар элементов, равных друг другу: {pairs}")
