while True:
    days = 1
    start_km = int(input('Стартовый результат: '))
    last_km = int(input('Финальный результат: '))
    if start_km > last_km:
        print('Введены неверные данные')
    else:
        while start_km < last_km:
            start_km += start_km * 0.1  # start_km = start_km + (start_km * 0.1)
            days += 1
        print('Спортсмен добьется результата за {} дней'.format(days))
        break