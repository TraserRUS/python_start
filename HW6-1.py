import time
from itertools import cycle


class TrafficLight:
    cycle_count = 0
    def __init__(self, tl_model, colors=None):
        self.model = tl_model
        self.__colors = {'Красный': 7,
                         'Желтый': 2,
                         'Зеленый': 2,}
        self._loading()
        self._running()

    def _loading(self):
        print(self.model, 'включается...')
        time.sleep(2)

    def _running(self):
        for color in cycle(self.__colors.keys()):
            print(color)
            time.sleep(self.__colors.get(color))
            TrafficLight.cycle_count += 1
            if TrafficLight.cycle_count == len(self.__colors) * 3:
                break


my_tl = TrafficLight('Светофор')
