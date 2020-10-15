class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} помечает')


pen = Pen('Parker')
pencil = Pencil('Kohinoor')
handle = Handle('Flomaster')

pen.draw()
pencil.draw()
handle.draw()
