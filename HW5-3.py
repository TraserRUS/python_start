with open('workers_list.txt', encoding='utf-8') as f:
    mid_salary = 0
    for line in enumerate(f):
        lines = line[0] + 1
        elems = line[1].split()
        salary = list(map(int, elems[-1:]))
        mid_salary += salary[0]
        if salary[0] < 20000:
            print(f'{" ".join(elems)}')
print(f'Средняя зп - {mid_salary / lines}')