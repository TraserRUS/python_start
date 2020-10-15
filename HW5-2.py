with open('my_file.txt') as f:
    for line in enumerate(f):
        lines = line[0] + 1
        elems = len(line[1].split())
        print(f'Cтрокa {lines}, элемeнтов {elems}')
    print(f'Всего строк {lines}')
