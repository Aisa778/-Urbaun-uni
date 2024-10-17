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
        print('Всего этажей -', self.number_of_floors)
    def __str__(self):
        print('С уважением, коллектив', self.name)

    def __eq__(self, other):
        if isinstance(other, int):
            if isinstance(other, House):
                return self.number_of_floors == other.number_of_floors
        else:
            print ('нельзя сравнить')


    def __lt__(self, other):
        if isinstance(other, int):
            if isinstance(other, House):
                return self.number_of_floors < other.number_of_floors
        else:
            print('нельзя сравнить')


    def __le__(self, other):
        if isinstance(other, int):
            if isinstance(other, House):
                return self.number_of_floors <= other.number_of_floors
        else:
            print('нельзя сравнить')


    def __gt__(self, other):
        if isinstance(other, int):
           if isinstance(other, House):
                return self.number_of_floors > other.number_of_floors
        else:
            print('нельзя сравнить')


    def __ge__(self, other):
        if isinstance(other, int):
           if isinstance(other, House):
                return self.number_of_floors >= other.number_of_floors
        else:
            print('нельзя сравнить')


    def __ne__( self, other):
        if isinstance(other, int):
            if isinstance(other, House):
                return self.number_of_floors != other.number_of_floors
        else:
            print('нельзя сравнить')

    def __add__(self, value):
        if isinstance(value, int):
            if isinstance(self.number_of_floors,int):
                return self.number_of_floors + value
        else:
            print ('введите число')

    def __radd__(self, value):
        if isinstance(value, int):
            if isinstance(self.number_of_floors, int):
                return self.number_of_floors + value
        else:
            print('введите число')

    def __iadd__(self, value):
        if isinstance(value, int):
            if isinstance(self.number_of_floors, int):
                return self.number_of_floors + value
        else:
            print('введите число')


h1 = House('ЖК Горский', 18)
h2 = House('ЖК Венеция', 'lll')
# h1.go_to(new_floor)
# h2.go_to(new_floor)

h1.__len__()
h1.__str__()
h2.__len__()
h2.__str__()

print(h1==h2)
print(h1<h2)
print(h1<=h2)
print(h1>h2)
print(h1>=h2)
print(h1!=h2)
print('Сейчас в ЖК Горский', h1.__add__(2), 'этажей, а было', h1.number_of_floors, 'этажей' )
print('Сейчас в ЖК Венеция', h2.__add__(2), 'этажей, а было', h2.number_of_floors, 'этажей' )
print(h1.__radd__(1))
print(h2.__radd__(3))
print(h1.__iadd__('единица'))
print(h2.__iadd__(3))
