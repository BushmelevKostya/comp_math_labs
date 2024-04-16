import sys
import sympy as sp
import numpy
import math


def calc_func(coefficients, dot, deg):
    s = 0
    for i in range(deg + 1):
        s += coefficients[i] * dot ** i
    return s


def left_rectangle_method(coefficients, borders, error, deg):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(0, n - 1):
            x = h * i
            y = calc_func(coefficients, x, deg)
            s += y
        s *= h
        if abs(s - last_value) / (2 ** 2 - 1) < error and n > 2:
            return [s, n]
        last_value = s


def right_rectangle_method(coefficients, borders, error, deg):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(1, n):
            x = h * i
            y = calc_func(coefficients, x, deg)
            s += y
        s *= h
        if abs(s - last_value) / (2 ** 2 - 1) < error and n > 2 and s != last_value:
            return [s, n]
        last_value = s


def middle_rectangle_method(coefficients, borders, error, deg):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(n - 1):
            x = h * i
            y = calc_func(coefficients, x + h / 2, deg)
            s += y
        s *= h
        if abs(s - last_value) / (2 ** 2 - 1) < error and n > 2:
            return [s, n]
        last_value = s


def trapezoid_method(coefficients, borders, error, deg):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(1, n - 1):
            x = h * i
            y = calc_func(coefficients, x, deg)
            s += y
        s += (calc_func(coefficients, borders[0], deg) + calc_func(coefficients, borders[1], deg)) / 2
        s *= h
        if abs(s - last_value) / (2 ** 2 - 1) < error and n > 2:
            return [s, n]
        last_value = s


def simpson_method(coefficients, borders, error, deg):
    n = 1
    last_value = 0
    while 1:
        n *= 2
        s = 0
        h = (borders[1] - borders[0]) / n
        for i in range(2, n - 2, 2):
            x = h * i
            y = calc_func(coefficients, x, deg)
            s += 2 * y

        for i in range(1, n - 1, 2):
            x = h * i
            y = calc_func(coefficients, x, deg)
            s += 4 * y
        s += calc_func(coefficients, borders[0], 3) + calc_func(coefficients, borders[1], deg)
        s *= h / 3
        if abs(s - last_value) / (2 ** 4 - 1) < error and n > 2:
            return [s, n]
        last_value = s


def limit_expression(expression, variable, limit_point):
    expr = sp.sympify(expression)
    var = sp.symbols(variable)
    limit = sp.limit(expr, var, limit_point)
    return limit


def indefinite_integral(func):
    x = sp.symbols('x')
    integral = sp.integrate(func(x), x)
    return integral


def evaluate_integral_at_point(integral, point):
    return integral.subs(integral.free_symbols.pop(), point)


def calc_unowned_integral(func, borders, i):
    integral = indefinite_integral(func)
    res1 = evaluate_integral_at_point(integral, borders[1 - i])
    res2 = limit_expression(integral, 'x', borders[i])
    if res2 == sp.oo:
        print("Integral undefined, sorry!")
        return
    if i == 0:
        return res1 - res2
    return res2 - res1


def func_1(x):
    return 1 / (1 - x)


def func_2(x):
    return 1 / sp.sqrt(x)


def func_3(x):
    return sp.ln(x)


def read_vars(filepath, dim):
    try:

        with open(filepath, "r") as file:
            if dim != 1:
                data = list(map(float, file.readlines()[0].replace(",", ".").strip().split(" ")))
            else:
                data = list(map(float, file.readlines()[1].replace(",", ".").strip().split(" ")))
            if len(data) < dim:
                raise IndexError
        return data
    except FileNotFoundError:
        print("This file doesn't exist! Try another name of file")
    except PermissionError:
        print("You haven't enough permissions for read this file! Try another name of file")
    except ValueError:
        print("Wrong type in variables!")
    except IndexError:
        print("Data in variables is not valid")


def read_dim(filepath):
    try:
        with open(filepath, "r") as file:
            data = float(file.readline())
        return data
    except FileNotFoundError:
        raise FileNotFoundError("This file doesn't exist! Try another name of file")
    except PermissionError:
        raise FileNotFoundError("You haven't enough permissions for read this file! Try another name of file")
    except ValueError:
        raise FileNotFoundError("Wrong type in dimension!")
    except IndexError:
        raise FileNotFoundError("Data in dimension is not valid")


def write_answer(filepath, answer):
    try:
        with open(filepath, "w") as file:
            file.write(answer)
    except FileNotFoundError:
        raise FileNotFoundError("This file doesn't exist! Try another name of file")
    except PermissionError:
        raise FileNotFoundError("You haven't enough permissions for read this file! Try another name of file")


def main():
    type = str(sys.argv[1])
    gNum = int(sys.argv[2])
    mNum = int(sys.argv[3])
    # filepath = "src\\main\\resources\\files\\input.txt" + str(sys.argv[8])
    # if sys.argv[4] == "" or sys.argv[5] == "" or sys.argv[6] == "":
    #     data = read_vars(filepath, 1)
    #     a = data[0]
    #     b = data[1]
    #     error = read_dim(filepath)
    # else:
    if sys.argv[4] == "" or sys.argv[5] == "":
        print("Interval boundaries are not specified!")
        return
    if sys.argv[6] == "":
        print("Error are not specified!")
        return
    a = float(sys.argv[4])
    b = float(sys.argv[5])
    if a > b:
        a, b = b, a
    error = float(sys.argv[6])
    answer = str(sys.argv[7])
    # print(type, gNum, mNum, a, b, error, "\n")
    if error < 0:
        print("Error must be positive!")
        return
    if answer == "None":
        coeffs = []
        dim = 0
        if gNum == 0:
            coeffs = [3, 1, -1, -1]
            dim = 3
        elif gNum == 1:
            coeffs = [1, 0, -5, 0, 4]
            dim = 4
        elif gNum == 2:
            coeffs = [-1, -1, -1, -1]
            dim = 3
        elif gNum == 8:
            if a < 1 and b > 1:
                print("Integral undefined, sorry!")
                return
            if b == 1:
                res = calc_unowned_integral(func_1, [a, b], 1)
            else:
                res = calc_unowned_integral(func_1, [a, b], 0)
            if res is not None:
                print("Integral value is: ", res)
        elif gNum == 9:
            if a < 0:
                print("Integral undefined, sorry!")
                return
            res = calc_unowned_integral(func_2, [a, b], 0)
            print("Integral value is: ", res)
        elif gNum == 10:
            if a < 0:
                print("Integral undefined, sorry!")
                return
            res = calc_unowned_integral(func_3, [a, b], 0)
            print("Integral value is: ", res)
        if mNum == 3:
            res = left_rectangle_method(coeffs, [a, b], error, dim)
            print("Integral value is: ", res[0], "\n")
            print("Count of segments is: ", res[1])
        elif mNum == 4:
            res = right_rectangle_method(coeffs, [a, b], error, dim)
            print("Integral value is: ", res[0], "\n")
            print("Count of segments is: ", res[1])
        elif mNum == 5:
            res = middle_rectangle_method(coeffs, [a, b], error, dim)
            print("Integral value is: ", res[0], "\n")
            print("Count of segments is: ", res[1])
        elif mNum == 6:
            res = trapezoid_method(coeffs, [a, b], error, dim)
            print("Integral value is: ", res[0], "\n")
            print("Count of segments is: ", res[1])
        elif mNum == 7:
            res = simpson_method(coeffs, [a, b], error, dim)
            print("Integral value is: ", res[0], "\n")
            print("Count of segments is: ", res[1])
    else:
        write_answer("src\\main\\resources\\files\\answer.txt", answer)


if __name__ == "__main__":
    main()
