class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.worker_name = name
        self.worker_surname = surname
        self.worker_position = position
        self._w_income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return (f'ФИО - {self.worker_name} {self.worker_surname}')

    def get_total_income(self,):
        return (f'{sum(self._w_income.values())}')

worker_1 = Position('Igor', 'Poll', 'worker', 10000, 2000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
