from sys import argv


def salary(*args):
    param = argv[1:]
    if 'help' in param or 'h' in param:
        print('Введите через пробел: выработка в часах, ставка в час, премия')
    else:
        print(f'ЗП равна {(int(param[0]) * int(param[1])) + int(param[2])}')


salary()
