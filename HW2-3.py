'''
months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июль', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
m = int(input('Введите любимый номер месяца (1-12): ')) - 1
while m < 0 or m > 11:
    print('Неверно!')
    m = int(input('Введите число от 1 до 12: ')) - 1
if m == 0 or m == 1 or m == 11:
    print(f'Зима - {months[m]}')
elif m > 1 and m <= 4:
    print(f'Весна - {months[m]}')
elif m > 4 and m <= 7:
    print(f'Лето - {months[m]}')
elif m > 7 and m <= 10:
    print(f'Осень - {months[m]}')


'''
seasons = {'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11),
           'Зима': (12, 1, 2),
           }
month = int(input('Введите любимый номер месяца (1-12): '))
while month < 1 or month > 12:
    print('Неверно!')
    month = int(input('Введите число от 1 до 12: '))
for season in seasons.keys():
    if month in seasons[season]:
        print(f'Вам нравится - {season}')