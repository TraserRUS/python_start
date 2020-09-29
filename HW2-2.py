my_list = []
n = abs(int(input("Введите количество элементов списка: ")))
for i in range (0, n):
    element = input(f'Введите элемент {i+1}: ')
    my_list.append(element)   
print(my_list)

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)