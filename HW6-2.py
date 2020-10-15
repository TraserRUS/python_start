class Road:
    def __init__(self, road_length, road_width):
        self.__length = road_length
        self.__width = road_width
        self.asphalt_calculation()


    def asphalt_calculation(self):
        mass_tonnes = self.__length * self.__width * 25 * 5 / 1000
        print(f'{mass_tonnes} тонн')


r1 = Road(road_length=20, road_width=5000)
r2 = Road(road_length=40, road_width=5000)
