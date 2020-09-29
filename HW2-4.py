phrase = input('Введите любую фразу: ')
num = 0
for word in phrase.split(' '):
    if len(str(word)) <= 10:
            print(f' {num + 1} {word}')
            num += 1
    else:
        print(f' {num + 1} {word[0:10]}')
        num += 1