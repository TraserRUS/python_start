class Car:
    def __init__(self, speed, color, name, is_police):
        self.car_speed = speed
        self.car_color = color
        self.car_name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.car_name} едет вперед...')

    def stop(self):
        print(f'{self.car_name} останавливается...')

    def turn_left(self):
        print(f'{self.car_name} поворачивает налево...')

    def turn_right(self):
        print(f'{self.car_name} поворачивает направо...')

    def show_speed(self):
        print (f'{self.car_speed}км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.car_speed > 60:
            print(f'{self.car_name} превышает скорость!')
        else:
            print(f'{self.car_name} едет с разрешенной скоростью.')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.car_speed > 40:
            print(f'{self.car_name} превышает скорость!')
        else:
            print(f'{self.car_name} едет с разрешенной скоростью.')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
            print(f'{self.car_name} едет со скоростью {self.car_speed}км/ч.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.car_name} едет со скоростью {self.car_speed}км/ч.')


uaz = WorkCar(60, 'white', 'UAZ Patriot', False)
ferrari = SportCar(120, 'red', 'Ferrari', False)
daewoo = TownCar(50, 'green', 'Daewoo Matiz', False)
skoda = PoliceCar(130, 'blue', 'POLISE DPS', True)
print(f'{ferrari.car_name}, цвет - {ferrari.car_color}')
ferrari.show_speed()
print(f'{uaz.car_name}, цвет - {uaz.car_color}')
uaz.show_speed()
print(f'{daewoo.car_name}, цвет - {daewoo.car_color}')
daewoo.show_speed()
print(f'{skoda.car_name}, цвет - {skoda.car_color}')
skoda.show_speed()
skoda.go()
skoda.stop()
skoda.turn_right()
skoda.turn_left()