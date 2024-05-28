import math
from lab5.output import *
from lab5.polinoms import *
from functools import reduce
from math import factorial

def run_methods(pairs, dot):
    n = len(pairs)
    diff_matrix = calc_diff_matrix(pairs, n)
    print_diff_matrix(diff_matrix, n)
    res, eq = lagrange(pairs, dot)
    lagrange_output(res, dot, eq)

    middle = (pairs[0][0] + pairs[n - 1][0]) // 2
    h = pairs[1][0] - pairs[0][0]
    if dot < middle:
        res, eq = first_newton_formula(dot, pairs[0][0], h, diff_matrix, n)
        newton_output(res, dot, eq)
        res, eq = second_gauss_formula(dot, pairs[(n - 1) // 2][0], h, diff_matrix, n)
        gauss_output(res, dot, eq)
    else:
        res, eq = second_newton_formula(dot, pairs[n - 1][0], h, diff_matrix, n)
        newton_output(res, dot, eq)
        res, eq = first_gauss_formula(dot, pairs[(n - 1) // 2][0], h, diff_matrix, n)
        gauss_output(res, dot, eq)
    res, eq = stirling_formula(dot, pairs[(n - 1) // 2][0], h, diff_matrix, n)
    stirling_output(res, dot, eq)
    res = bessel_formula(pairs, n)
    bessel_output(res(dot), dot, eq)


def calc_lagr_coef(pairs, num, dot, n, y):
    p = 1
    f = 0
    eq = "1"
    for i in range(n):
        if i != num:
            p *= (dot - pairs[i][0]) / (pairs[num][0] - pairs[i][0])
            if f == 0:
                coef1 = str(y / (pairs[num][0] - pairs[i][0]))
                coef2 = -pairs[i][0] * y / (pairs[num][0] - pairs[i][0])
                f = 1
            else:
                coef1 = str(1 / (pairs[num][0] - pairs[i][0]))
                coef2 = -pairs[i][0] / (pairs[num][0] - pairs[i][0])
            if coef2 > 0:
                eq = multiply_polynomial_strings(eq, coef1 + "x+" + str(coef2))
            else:
                eq = multiply_polynomial_strings(eq, coef1 + "x" + str(coef2))
    return p, eq


def first_newton_product_t(t, n, border, h):
    p = 1
    eq = "1"
    coef_x_1 = str(1 / h)
    coef_x_2 = str(-border / h)
    for i in range(n):
        p *= t
        t -= 1

        eq2 = coef_x_1 + "x" + ("" if float(coef_x_2) < 0 else "+") + coef_x_2
        eq = multiply_polynomial_strings(eq, eq2)
        coef_x_2 = str(float(coef_x_2) - 1)
    return p, eq


def second_newton_product_t(t, n, border, h):
    p = 1
    eq = "1"
    coef_x_1 = str(1 / h)
    coef_x_2 = str(-border / h)
    for i in range(n):
        p *= t
        t += 1

        eq2 = coef_x_1 + "x" + ("" if float(coef_x_2) < 0 else "+") + coef_x_2
        eq = multiply_polynomial_strings(eq, eq2)
        coef_x_2 = str(float(coef_x_2) + 1)
    return p, eq


def first_gauss_product_t(t, n, border, h):
    p = 1
    t1 = t2 = t

    eq = "1"
    coef_x_1 = str(1 / h)
    coef_x_2_1 = str(-border / h)
    coef_x_2_2 = str(-border / h)
    for i in range(n):
        if i % 2 != 0:
            p *= t1
            t2 -= 1

            eq2 = coef_x_1 + "x" + ("" if float(coef_x_2_1) < 0 else "+") + coef_x_2_1
            eq = multiply_polynomial_strings(eq, eq2)
            coef_x_2_2 = str(float(coef_x_2_2) - 1)
        else:
            p *= t2
            t1 += 1

            eq2 = coef_x_1 + "x" + ("" if float(coef_x_2_2) < 0 else "+") + coef_x_2_2
            eq = multiply_polynomial_strings(eq, eq2)
            coef_x_2_1 = str(float(coef_x_2_1) + 1)
    return p, eq


def second_gauss_product_t(t, n, border, h):
    p = 1
    t1 = t2 = t

    eq = "1"
    coef_x_1 = str(1 / h)
    coef_x_2_1 = str(-border / h)
    coef_x_2_2 = str(-border / h)
    for i in range(n):
        if i % 2 != 0:
            p *= t1
            t2 += 1

            eq2 = coef_x_1 + "x" + ("" if float(coef_x_2_1) < 0 else "+") + coef_x_2_1
            eq = multiply_polynomial_strings(eq, eq2)
            coef_x_2_2 = str(float(coef_x_2_2) + 1)
        else:
            p *= t2
            t1 -= 1

            eq2 = coef_x_1 + "x" + ("" if float(coef_x_2_2) < 0 else "+") + coef_x_2_2
            eq = multiply_polynomial_strings(eq, eq2)
            coef_x_2_1 = str(float(coef_x_2_1) - 1)
    return p, eq


def calc_diff_matrix(pairs, n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][0] = pairs[i][1]
    for i in range(1, n):
        for j in range(0, n - i):
            matrix[j][i] = matrix[j + 1][i - 1] - matrix[j][i - 1]
    return matrix


def first_newton_formula(dot, border, h, diff_matrix, n):
    s = 0
    t = (dot - border) / h
    equation = "0"
    for i in range(n):
        product, eq = first_newton_product_t(t, i, border, h)
        fact = math.factorial(i)
        s += diff_matrix[0][i] * product / fact

        # print(equation)
        eq = multiply_polynomial_strings(eq, str(diff_matrix[0][i] / fact))
        equation = plus_polynomial_strings(equation, eq)
    return s, equation


def second_newton_formula(dot, border, h, diff_matrix, n):
    s = 0
    t = (dot - border) / h
    equation = "0"
    for i in range(n):
        product, eq = second_newton_product_t(t, i, border, h)
        fact = math.factorial(i)
        s += diff_matrix[n - 1 - i][i] * product / fact

        eq = multiply_polynomial_strings(eq, str(diff_matrix[n - 1 - i][i] / fact))
        equation = plus_polynomial_strings(equation, eq)
        # print(equation)
    return s, equation


def first_gauss_get_coef(diff_matrix, n, i):
    return diff_matrix[(n - i) // 2][i]


def second_gauss_get_coef(diff_matrix, n, i):
    return diff_matrix[(n - i - 1) // 2][i]


def first_gauss_formula(dot, border, h, diff_matrix, n):
    s = 0
    t = (dot - border) / h
    equation = "0"
    for i in range(n):
        coef = first_gauss_get_coef(diff_matrix, n, i)
        product, eq = first_gauss_product_t(t, i, border, h)
        fact = math.factorial(i)
        s += coef * product / fact

        eq = multiply_polynomial_strings(eq, str(coef / fact))
        equation = plus_polynomial_strings(equation, eq)
    return s, equation


def second_gauss_formula(dot, border, h, diff_matrix, n):
    s = 0
    t = (dot - border) / h
    equation = "0"
    for i in range(n):
        coef = second_gauss_get_coef(diff_matrix, n, i)
        product, eq = second_gauss_product_t(t, i, border, h)
        fact = math.factorial(i)
        s += coef * product / fact

        eq = multiply_polynomial_strings(eq, str(coef / fact))
        equation = plus_polynomial_strings(equation, eq)
    return s, equation


def lagrange(pairs, dot):
    s = 0
    n = len(pairs)
    equation = "0"
    for i in range(n):
        p, eq = calc_lagr_coef(pairs, i, dot, n, pairs[i][1])
        # print(equation, " - ", eq)
        s += pairs[i][1] * p
        equation = plus_polynomial_strings(equation, eq)
        # print(equation)
    return s, equation


def stirling_formula(dot, pair, h, diff_matrix, n):
    s1, eq1 = first_gauss_formula(dot, pair, h, diff_matrix, n)
    s2, eq2 = second_gauss_formula(dot, pair, h, diff_matrix, n)

    result = (s1 + s2) / 2

    equation = plus_polynomial_strings(eq1, eq2)
    equation = multiply_polynomial_strings(equation, "0.5")

    return result, equation


def bessel_formula(pairs, n):
    xs = [pair[0] for pair in pairs]
    ys = [pair[1] for pair in pairs]
    n = len(xs) - 1
    alpha_ind = n // 2
    fin_difs = []
    fin_difs.append(ys[:])

    for k in range(1, n + 1):
        last = fin_difs[-1][:]
        fin_difs.append(
            [last[i + 1] - last[i] for i in range(n - k + 1)])

    h = xs[1] - xs[0]
    dts1 = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]

    return lambda x: (ys[alpha_ind] + ys[alpha_ind]) / 2 + sum([
        reduce(lambda a, b: a * b,
               [(x - xs[alpha_ind]) / h + dts1[j] for j in range(k)])
        * fin_difs[k][len(fin_difs[k]) // 2] / factorial(2 * k) +

        ((x - xs[alpha_ind]) / h - 1 / 2) *
        reduce(lambda a, b: a * b,
               [(x - xs[alpha_ind]) / h + dts1[j] for j in range(k)])
        * fin_difs[k][len(fin_difs[k]) // 2] / factorial(2 * k + 1)

        for k in range(1, n + 1)])
