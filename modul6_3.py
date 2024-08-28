class Horse:
    def __init__(self):
        self.x_distance = 0 # Пройденный путь
        self.sound = 'Frrr' # Звук, который издает лошадь
    def run(self, dx):
        self.x_distance += dx # изменение дистанции

class Eagle:
    def __init__(self):
        self.y_distance = 0 # высота полёта
        self.sound = 'I train, eat, sleep, and repeat' #звук,который издаёт орёл
    def fly(self, dy):
        self.y_distance += dy # изменение дистанции

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)  # Запускаем метод run из класса Horse
        self.fly(dy)  # Запускаем метод fly из класса Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance)  #  текущее положение

    def voice(self):
        print(self.sound)  #  звук, который издает орел

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()


