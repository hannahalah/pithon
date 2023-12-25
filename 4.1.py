class String:
    def __init__(self, value):
        self.value = value

    def length(self):
        return len(self.value)

    def uppercase(self):
        return self.value.upper()

    def lowercase(self):
        return self.value.lower()

    def reverse(self):
        return self.value[::-1]

    def count_words(self):
        return len(self.value.split())

# Пример использования класса String
my_string = String("Пример строки для теста")
print(my_string.length())
print(my_string.uppercase())
print(my_string.lowercase())
print(my_string.reverse())
print(my_string.count_words())