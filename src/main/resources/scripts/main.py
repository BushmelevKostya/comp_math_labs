import sys
import sympy
import numpy
import math


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
    temp = [borders[0], borders[1]]
    n = 0
    x = (borders[0] + borders[1]) / 2
    while abs(borders[0] - borders[1]) > error and abs(calc_func(coefficients, dim, x)) >= error:
        x = (borders[0] + borders[1]) / 2
        if calc_func(coefficients, dim, borders[0]) * calc_func(coefficients, dim, x) > 0:
            borders[0] = x
        else:
            borders[1] = x
        n += 1
    x = (borders[0] + borders[1]) / 2
    keys = ["x", "f(x)", "count of operation"]
    if check_roots(temp, x) == 0:
        print("Must be exactly one root")
        return
    print_answers(3, [x, calc_func(coefficients, dim, x), n], keys)


def newton_alg(approx, coefficients, dim, error):
    temp = [approx[0], approx[1]]
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
    if check_roots(temp, approx[1]) == 0:
        print("Must be exactly one root")
        return
    print_answers(3, [approx[1], calc_func(coefficients, dim, approx[1]), n], keys)


def simple_iteration_alg(approx, coefficients, dim, error):
    temp = [approx[0], approx[1]]
    x = sympy.Symbol('x')
    f = sum(coefficients[i] * x ** i for i in range(len(coefficients)))
    df = sympy.diff(f, x)
    g = x - f / df
    g_func = sympy.lambdify(x, g, 'numpy')

    xn = approx[1]
    n = 0
    while 1:
        n += 1
        xn_plus_1 = g_func(xn)
        if abs(xn_plus_1 - xn) < error:
            break
        xn = xn_plus_1
    keys = ["x", "f(x)", "count of operation"]
    if check_roots(temp, xn_plus_1) == 0:
        print("Must be exactly one root")
        return
    print_answers(dim, [xn_plus_1, calc_func(coefficients, dim, xn_plus_1), n], keys)


def create_polinom(num):
    coefficients = []
    if num == 1:
        x = sympy.Symbol('x')
        f = 2 ** x - sympy.cos(x - 1) - 3
        taylor_series = f.series(x, 0, 5).removeO()
        coefficients = [taylor_series.coeff(x, i).evalf() for i in range(6)]
    return coefficients


def derivative_function1(x, y):
    return numpy.array([[2 * x, 2 * y], [-6 * x, 1]], dtype=float)


def derivative_function2(x, y):
    return numpy.array([[2 * x, -numpy.sin(y)], [1, -numpy.sin(y)]], dtype=float)


def matrix_multiply(matrix1, matrix2):
    result = [[0, 0], [0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def equation_1(number, x, y):
    if number == 6:
        return x ** 2 + y ** 2 - 4
    elif number == 7:
        return x ** 2 + numpy.cos(y) - 4


def equation_2(number, x, y):
    if number == 6:
        return y - 3 * x ** 2
    elif number == 7:
        return numpy.cos(y) + x - 2


def inverse_matrix(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        raise ValueError("Singular matrix, cannot find inverse")
    inv_det = 1 / det
    inv_matrix = [
        [matrix[1][1] * inv_det, -matrix[0][1] * inv_det],
        [-matrix[1][0] * inv_det, matrix[0][0] * inv_det]
    ]
    return inv_matrix


def check_roots(approx, x):
    if x < min(approx[0], approx[1]) or x > max(approx[0], approx[1]) or abs(x - min(approx[0], approx[1])) < 0.1 or abs(x - max(approx[0], approx[1])) < 0.1:
        return 0
    return 1


def system_simple_iteration_method(number, approx, error):
    systems = [
        (
            "x^2 + y^2 = 4, y = 3x^2",
            lambda x, y: x ** 2 + y ** 2 - 4,
            lambda x, y: y - 3 * x ** 2,
            lambda x, y: numpy.matrix([[2 * x, 2 * y], [-6 * x, 1]]),
        ),
        (
            "x^2 + cos y = 4, cos(y) + x = 2",
            lambda x, y: x ** 2 + numpy.cos(y) - 4,
            lambda x, y: numpy.cos(y) + x - 2,
            lambda x, y: numpy.matrix([[2 * x, - numpy.sin(y)], [1, - numpy.sin(y)]])
        )
    ]

    system = []
    if number == 6:
        system = systems[0]
    elif number == 7:
        system = systems[1]

    x = approx[0]
    y = approx[1]
    eps = error

    iter_num = 0
    while True:
        iter_num += 1
        x_prev = x
        y_prev = y
        A = system[3](x, y)
        b = - numpy.array([system[1](x, y), system[2](x, y)])
        solution = numpy.linalg.solve(A, b)
        x = x + solution[0]
        y = y + solution[1]
        if abs(x - x_prev) < eps and abs(y - y_prev) < eps:
            print(f"Vector of errors: ({abs(x - x_prev)}, {abs(y - y_prev)})")
            break
        if iter_num > 1000:
            print("System has no answer on this interval")
            exit()

    print(f"x, y = ({x}, {y})")
    f_val = system[1](x, y)
    g_val = system[2](x, y)
    print(f": f = {f_val}, g = {g_val}")
    print(f"Count of iteration", iter_num)


def main():
    type = str(sys.argv[1])
    gNum = int(sys.argv[2])
    mNum = int(sys.argv[3])
    a = float(sys.argv[4])
    b = float(sys.argv[5])
    error = float(sys.argv[6])
    # print(type, gNum, mNum, a, b, error, "\n")

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
