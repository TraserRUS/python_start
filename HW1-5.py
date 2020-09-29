income = float(input('Выручка: '))
costs = float(input('Издержки: '))

total = income - costs

if total > 0:
    print(f'Прибыль: {total}')
    print(f'Рентабельность: {total / income}')
    staff = int(input('Количество сотрудников: '))
    print(f'Прибыль на одного сотрудника: {total / staff:.2f}')
elif total < 0:
    print(f'Убыток: {total}')
else:
    print('Комапния работает в 0')