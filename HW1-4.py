num = abs(int(input('Введите положительное число: ')))
max_num = 0
while num > 0:
    last_num = num % 10
    if last_num > max_num:
        max_num = last_num
        if max_num == 9:
            break
    num = num //10
print(f'Максимальная цифра = {max_num}')