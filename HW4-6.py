from itertools import count, cycle
import time


# def func(i, stop_num):
#     for num in count(i):
#         time.sleep(0.3)
#         if num > stop_num:
#             break
#         print(num)


def func_cycled(stop_num):
    for color in enumerate(cycle(['red', 'yellow', 'green'])):
        time.sleep(0.3)
        if color[0] == stop_num * 3:
            break
        print(color[1])


# func(int(input('Введите нач.число:')), int(input('Введите кон.число:')))

func_cycled(int(input('Введите число циклов:')))
