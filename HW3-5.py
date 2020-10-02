def adding_sum(*args):
    sum = 0
    while True:
        nums = input('Введите числа через пробел или Q для выхода: ').split()
        for n in nums:
            try:
                if n == 'q' or n == 'Q' or n == 'Й' or n == 'й':
                    print(f'Сумма = {sum}')
                    return
                else:
                    sum += float(n)
            except ValueError:
                print('Ошибка. Введите числа через пробел или Q для выхода: ')
        print(f'Сумма = {sum}')
adding_sum()