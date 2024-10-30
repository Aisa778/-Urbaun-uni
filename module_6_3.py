class Horse:
    def __init__(self, x_distance, sound):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()

    def run(self, dx):

        self.x_distance += dx
        pass


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly (self, dy):
        self.y_distance += dy
        pass

class Pegasus(Horse, Eagle):

    def move(self, dx, dy):

       return self.run(dx), self.fly(dy)

       pass

    def get_pos(self):
        return self.x_distance, self.y_distance
        pass

    def voice(self):
        print(self.sound)
        pass


p1 = Pegasus(0, "FRRR")

# p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

