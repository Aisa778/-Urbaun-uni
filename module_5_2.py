new_floor= int(input('Введите номер нужного Вам этажа '))

class House:
    def __init__(self,name, number_of_floors):
        pass
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):

        if new_floor < 1 or new_floor > self.number_of_floors:
            return print('Такого этажа не существует')
        else:
            for i in range(1,new_floor+1):
                print(i)

    def __len__(self):
        print('Всего этаже -', self.number_of_floors)
    def __str__(self):
        print('С уважением, коллектив', self.name)


h1 = House('ЖК Горский', 18)
h1.go_to(new_floor)
h1.__len__()
h1.__str__()