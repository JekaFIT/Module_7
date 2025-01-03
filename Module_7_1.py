import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if os.path.exists(self.__file_name):
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        return 'Файл не найден. Магазин пока пуст.'

    def add(self, *products):
        if os.path.exists(self.__file_name):
            with open(self.__file_name, 'r') as file:
                existing_products = [line.split(',')[0].strip() for line in file.readlines()]
        else:
            existing_products = []

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_products:
                    file.write(str(product) + '\n')
                else:
                    print(f'Продукт {product.name} уже есть в магазине.')

# Пример использования:
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__ будет вызван при печати

s1.add(p1, p2, p3)  # Добавляем продукты в магазин

print(s1.get_products())  # Выводим все продукты из файла
