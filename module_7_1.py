from itertools import product
from pprint import pprint

class Product:
    def __init__(self, name = str, weight = float, category = str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        one__ = open(self.__file_name, 'r', encoding = 'UTF-8')
        f_1 = one__.read()
        one__.close()
        return f_1
        pass

    def add(self, *products):
        f_3 = products
        f_2 = self.get_products()

        for i in f_3:
            name_1 = getattr(i,'name')
            weight_1 = str(getattr(i,'weight'))
            category_1 = getattr(i,'category')
            if name_1 not in f_2:
                f_4 = open(self.__file_name, 'a', encoding='UTF-8')
                f_4.write(name_1 +', '+ weight_1 +', ' + category_1+'\n')
                f_4.close()

            else:
                print(f'Продукт, {name_1}, уже есть в магазине')
        pass


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())





