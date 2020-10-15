new_list = []

while True:
    elems = input('Введите новую текстовую строку или пробел для выхода:')
    if elems == ' ':
        print(new_list)
        break
    else:
        line = elems + '\n'
        new_list.append(line)
    with open('my_file.txt', 'w') as f:
        f.writelines(new_list)
with open('my_file.txt') as f:
    content = f.read()
    print(content)
