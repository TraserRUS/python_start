time_in_seconds = abs(int(input('Введите количество секунд: ')))
hours = time_in_seconds // 3600
minutes = (time_in_seconds // 60) % 60
sec = time_in_seconds % 60
print(f'H:M:S = {hours} : {minutes} : {sec}')