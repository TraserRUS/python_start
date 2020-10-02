def my_func (a, b, c):
    pre_sum = [a, b, c]
    pre_sum.remove(min(a,b,c))
    return sum(pre_sum)

print(my_func(10, 20, 30))