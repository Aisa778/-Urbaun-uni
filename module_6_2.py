class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, _model,  __engine_power, __color ):
        self.owner = owner
        self._model = _model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return ("Модель:", {self._model})
        pass
    def get_horsepower(self):
        return ("Мощность двигателя:", {self.__engine_power})
        pass
    def get_color(self):
        return ('Цвет транспорта', {self.__color})
        pass

    def print_info(self):
        print (Vehicle.get_model(self))
        print(f'{Vehicle.get_horsepower(self)}')
        print(f'{Vehicle.get_color(self)}')
        print (f'Владелец', self.owner)

        pass

    def set_color(self, new_color):
        self.new_color = new_color

        if new_color.lower() in self._COLOR_VARIANTS:
            self.__color = new_color

        else:
            print (f'Нельзя сменить цвет на', {new_color})



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


vehicle1 = Sedan('Fedos', 'Toyota Mark II', '500', 'blue')
# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
