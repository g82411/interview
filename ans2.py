def anonymous(x):
    return x ** 2 + 1

def integrate(fun ,start, end):
    step = 0.00001
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        area += step * fun(intercept)
    return area


if __name__ == '__main__':
    print(integrate(anonymous, 0, 10))