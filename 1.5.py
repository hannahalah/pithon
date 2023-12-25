products = {
    "молоко": [100, 10],
    "хлеб": [200, 5],
    "яйца": [50, 20],
    "помидоры": [300, 3],
    "сметана": [150, 15]
}


def show_price(product_name):
    price = products.get(product_name, "Такого продукта нет")
    print(f"{product_name} - Цена: {price[0]} рублей")


def show_quantity(product_name):
    quantity = products.get(product_name, "Такого продукта нет")
    print(f"{product_name} - Количество: {quantity[1]} штук")


def show_all_info():
    for product_name, info in products.items():
        print(f"{product_name} - Цена: {info[0]} рублей, Количество: {info[1]} штук")


def buy_product(product_name, quantity):
    if product_name in products:
        if quantity <= products[product_name][1]:
            price = products[product_name][0] * quantity
            products[product_name][1] -= quantity
            print(f"Вы купили {quantity} {product_name} за {price} рублей.")
        else:
            print(f"Извините, недостаточно {product_name} в наличии.")
    else:
        print("Такого продукта нет")


while True:
    print("\nМеню:")
    print("1. Просмотр цены")
    print("2. Просмотр количества")
    print("3. Всю информацию")
    print("4. Покупка")
    print("5. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        product_name = input("Введите название продукта: ")
        show_price(product_name)
    elif choice == "2":
        product_name = input("Введите название продукта: ")
        show_quantity(product_name)
    elif choice == "3":
        show_all_info()
    elif choice == "4":
        while True:
            product_name = input("Введите название продукта (или 'n' для выхода): ")
            if product_name == "n":
                break
            quantity = int(input(f"Введите количество {product_name}: "))
            buy_product(product_name, quantity)
    elif choice == "5":
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 5.")
