class ZooShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_most_expensive_breed(self):
        most_expensive = max(self.animals, key=lambda x: x.price)
        return most_expensive.breed

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(f'{animal.breed}, Цена: {animal.price} руб., Способ передвижения: {animal.move()}\n')


class Animal:
    def __init__(self, breed, price):
        self.breed = breed
        self.price = price

    def move(self):
        pass


class Fish(Animal):
    def move(self):
        return "плавает"


class Bird(Animal):
    def move(self):
        return "летает"


# Создаем объекты
zoo = ZooShop()
zoo.add_animal(Fish("Золотая рыбка", 100))
zoo.add_animal(Fish("Щука", 50))
zoo.add_animal(Bird("Попугай", 500))
zoo.add_animal(Bird("Аист", 200))

# Получаем данные о самой дорогой породе
most_expensive = zoo.get_most_expensive_breed()
print("Самая дорогая порода: ", most_expensive)

# Записываем информацию в файл
zoo.write_to_file("zoo_info.txt")