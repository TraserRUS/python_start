with open('one_two.txt', 'r', encoding='utf-8') as f:
    dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
    }
    for line in f:
        elements = line.strip()
        elem = elements.split()
        if elem[0] in dict.keys():
            rus = dict[elem[0]]
            with open('three_four.txt', 'a', encoding='utf-8') as f_obj:
                f_obj.writelines(f'{rus} - {elem[2]}\n')