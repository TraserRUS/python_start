def divide(*arguments):
    try:
        arg1 = int(input("Укажите делимое: "))
        arg2 = int(input("Укажите делитель: "))
        result = arg1 / arg2
    except ValueError:
        return 'Укажите целое число'
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    return result

print(divide())
