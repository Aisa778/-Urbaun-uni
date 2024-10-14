

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


h1 = House('ЖК Горский', 18)
new_floor= int(input('Введите номер нужного Вам этажа '))
h1.go_to(new_floor)

