import random


with open('nums_5_5.txt', 'w', encoding='utf-8') as f:
    my_list = []
    for num in range(10):
        my_list.append(random.randint(0,100))
    f.write(" ".join(map(str,my_list)))

print(f'{my_list} - сумма: {sum(my_list)}')