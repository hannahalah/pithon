class Country:
    def __init__(self, name, capital, area, population):
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population


countries = [
    Country("Россия", "Москва", 17098242, 146171015),
    Country("Канада", "Оттава", 9984670, 37664517),
    Country("Китай", "Пекин", 9596961, 1403500365),
    Country("США", "Вашингтон", 9833520, 331002651)
]

def countries_by_area(countries, min_area):
    result = [country.name for country in countries if country.area >= min_area]
    return result


def countries_by_population(countries, min_population):
    result = [country.name for country in countries if country.population >= min_population]
    return result


print("Страны с площадью более 10 миллионов квадратных километров:", countries_by_area(countries, 10000000))
print("Страны с численностью населения более 1 миллиарда:", countries_by_population(countries, 1000000000))