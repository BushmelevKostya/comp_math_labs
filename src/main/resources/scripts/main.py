import sys
import sympy
import numpy


def print_answers(dim, arr_var, keys):
    for i in range(dim):
        print(keys[i], " = ", round(arr_var[i], 5), sep="")
    print()


def calc_func(coefficients, dim, dot):
    res = 0
    for i in range(dim):
        res += coefficients[i] * dot ** i

    return res


def bisection_alg(borders, coefficients, dim, error):
    n = 0
    x = (borders[0] + borders[1]) / 2
    print("hello")
    while abs(borders[0] - borders[1]) > error and abs(calc_func(coefficients, dim, x)) >= error:
        x = (borders[0] + borders[1]) / 2
        if calc_func(coefficients, dim, borders[0]) * calc_func(coefficients, dim, x) > 0:
            borders[0] = x
        else:
            borders[1] = x
        n += 1
    x = (borders[0] + borders[1]) / 2
    keys = ["x", "f(x)", "count of operation"]
    print_answers(3, [x, calc_func(coefficients, dim, x), n], keys)


def newton_alg(approx, coefficients, dim, error):
    n = 0
    func_values = [calc_func(coefficients, dim, approx[0]), calc_func(coefficients, dim, approx[1])]
    while abs(approx[1] - approx[0]) > error and abs(calc_func(coefficients, dim, approx[1])):
        derivative = (func_values[1] - func_values[0]) / (approx[1] - approx[0])
        next_x = approx[1] - calc_func(coefficients, dim, approx[1]) / derivative
        approx[0], approx[1] = approx[1], next_x
        next_y = calc_func(coefficients, dim, approx[1])
        func_values[0], func_values[1] = func_values[1], next_y
        n += 1
    keys = ["x", "f(x)", "count of operation"]
    print_answers(3, [approx[1], calc_func(coefficients, dim, approx[1]), n], keys)


def simple_iteration_alg(approx, coefficients, dim, error):
    x = sympy.Symbol('x')
    f = sum(coefficients[i] * x ** i for i in range(len(coefficients)))
    df = sympy.diff(f, x)
    g = x - f / df
    g_func = sympy.lambdify(x, g, 'numpy')

    print("hello")
    xn = approx[1]
    n = 0
    while 1:
        n += 1
        xn_plus_1 = g_func(xn)
        if abs(xn_plus_1 - xn) < error:
            break
        xn = xn_plus_1
    keys = ["x", "f(x)", "count of operation"]
    print_answers(dim, [xn_plus_1, g_func(xn_plus_1), n], keys)


def create_polinom(num):
    coefficients = []
    if num == 1:
        x = sympy.Symbol('x')
        f = 2 ** x - sympy.cos(x - 1) - 3
        taylor_series = f.series(x, 0, 5).removeO()
        coefficients = [taylor_series.coeff(x, i).evalf() for i in range(6)]
    return coefficients


def system_simple_iteration_method(number, approx, error):
    x0 = approx[0]
    y0 = approx[1]
    max_iter = 1000
    iteration = 0

    if not check_convergence(number, x0, y0):
        print("The iteration matrix does not\nsatisfy the convergence condition.")
        exit()

    for i in range(max_iter):
        x = f1(x0, y0, number)
        y = f2(x0, y0, number)
        if (abs(x - x0) < error) and (abs(y - y0) < error):
            print(f"x = {x}\ny = {y}")
            print(f"Iterations = {iteration}")
            return x, y
        x0, y0 = x, y
        iteration += 1


def f1(x, y, number):
    if (number == 6):
        return x * x + y * y - 4
    elif (number == 7):
        return 6 * y + x * x - 18
    else:
        print("System out of choice")
        exit()


def f2(x, y, number):
    if (number == 6):
        return y - 3 * x * x
    elif (number == 7):
        return 2 * x * x + 0.5 * y * y - 8
    else:
        print("System out of choice")
        exit()


def check_convergence(number, x0, y0):
    jacobian_matrix = numpy.array([[f1_dx(number, x0, y0), f1_dy(number, x0, y0)],
                                   [f2_dx(number, x0, y0), f2_dy(number, x0, y0)]])
    eigenvalues = numpy.linalg.eigvals(jacobian_matrix)
    if numpy.all(numpy.abs(eigenvalues) < 1):
        return True
    else:
        return False


def f1_dx(number, x, y):
    if number == 6:
        return 2 * x
    elif number == 7:
        return 2 * x
    else:
        print("System out of choice")
        exit()


def f1_dy(number, x, y):
    if number == 6:
        return 2 * y
    elif number == 7:
        return 6
    else:
        print("System out of choice")
        exit()


def f2_dx(number, x, y):
    if number == 6:
        return -6 * x
    elif number == 7:
        return 4 * x
    else:
        print("System out of choice")
        exit()


def f2_dy(number, x, y):
    if number == 6:
        return 1
    elif number == 7:
        return y
    else:
        print("System out of choice")
        exit()


def main():
    type = str(sys.argv[1])
    gNum = int(sys.argv[2])
    mNum = int(sys.argv[3])
    a = float(sys.argv[4])
    b = float(sys.argv[5])
    error = float(sys.argv[6])
    print(type, gNum, mNum, a, b, error, "\n")

    coeffs = []
    dim = 0
    if gNum == 0:
        coeffs = [-14.766, -5.606, 2.84, 1]
        dim = 4
    elif gNum == 1:
        coeffs = [-4, 0, -8, 0, 0, 1]
        dim = 6
    elif gNum == 2:
        coeffs = create_polinom(1)
        dim = 6
    elif gNum == 6:
        system_simple_iteration_method(gNum, [a, b], error)
    elif gNum == 7:
        system_simple_iteration_method(gNum, [a, b], error)
    if mNum == 3:
        bisection_alg([a, b], coeffs, dim, error)
    elif mNum == 4:
        newton_alg([a, b], coeffs, dim, error)
    elif mNum == 5:
        simple_iteration_alg([a, b], coeffs, dim, error)


if __name__ == "__main__":
    main()
