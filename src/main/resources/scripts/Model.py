def calc_func(coefficients, dot, deg):
    s = 0
    for i in range(deg + 1):
        s += coefficients[i] * dot ** i
    return s


def left_rectangle_method(coefficients, borders, error):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(0, n - 1):
            x = h * i
            y = calc_func(coefficients, x, 3)
            s += y
        s *= h
        if abs(s - last_value) / (2 ** 2 - 1) < error and n > 2:
            return s
        last_value = s


def right_rectangle_method(coefficients, borders, error):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(1, n):
            x = h * i
            y = calc_func(coefficients, x, 3)
            s += y
        s *= h
        if abs(s - last_value) / (2 ** 2 - 1)  < error and n > 2 and s != last_value:
            return s
        last_value = s

def middle_rectangle_method(coefficients, borders, error):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(n - 1):
            x = h * i
            y = calc_func(coefficients, x + h / 2, 3)
            s += y
        s *= h
        if abs(s - last_value) / (2 ** 2 - 1) < error and n > 2:
            return s
        last_value = s


def trapezoid_method(coefficients, borders, error):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(1, n - 1):
            x = h * i
            y = calc_func(coefficients, x,   3)
            s += y
        s += (calc_func(coefficients, borders[0], 3) + calc_func(coefficients, borders[1], 3)) / 2
        s *= h
        if abs(s - last_value) / (2 ** 2 - 1) < error and n > 2:
            return s
        last_value = s


def simpson_method(coefficients, borders, error):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(2, n - 2, 2):
            x = h * i
            y = calc_func(coefficients, x,   3)
            s += 2 * y

        for i in range(1, n - 1, 2):
            x = h * i
            y = calc_func(coefficients, x,   3)
            s += 4 * y
        s += calc_func(coefficients, borders[0], 3) + calc_func(coefficients, borders[1], 3)
        s *= h / 3
        if abs(s - last_value) / (2 ** 4 - 1) < error and n > 2:
            return s
        last_value = s
