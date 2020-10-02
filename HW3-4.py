def x_x_y(x,y):
#    return 1 / x ** abs(y)
    for i in range(abs(y-1)):
        x *= x
        return 1 / x
print(x_x_y(4,-2))