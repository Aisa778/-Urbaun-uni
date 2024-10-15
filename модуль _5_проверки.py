class House:
    def __init__(self,name, number_of_floors):
        pass
        self.name = name
        self.number_of_floors = number_of_floors

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('нельзя проверить')

h1 = House('ЖК Горский', 18)
h2 = House('ЖК Венеция', 'nhb')

print(h1>=h2)