import math
from lab5.output import *


def run_methods(pairs, dot):
    n = len(pairs)
    diff_matrix = calc_diff_matrix(pairs, n)
    print_diff_matrix(diff_matrix, n)
    res = lagrange(pairs, dot)
    lagrange_output(res, dot)

    middle = (pairs[0][0] + pairs[n - 1][0]) // 2
    h = pairs[1][0] - pairs[0][0]
    if dot < middle:
        res = first_newton_formula(dot, pairs[0][0], h, diff_matrix, n)
        newton_output(res, dot)
        res = second_gauss_formula(dot, pairs[(n - 1) // 2][0], h, diff_matrix, n)
        gauss_output(res, dot)
    else:
        res = second_newton_formula(dot, pairs[n - 1][0], h, diff_matrix, n)
        newton_output(res, dot)
        res = first_gauss_formula(dot, pairs[(n - 1) // 2][0], h, diff_matrix, n)
        gauss_output(res, dot)

def calc_lagr_coef(pairs, num, dot, n):
    p = 1
    for i in range(n):
        if i != num:
            p *= (dot - pairs[i][0]) / (pairs[num][0] - pairs[i][0])
    return p


def first_newton_product_t(t, n):
    p = 1
    for i in range(n):
        p *= t
        t -= 1
    return p


def second_newton_product_t(t, n):
    p = 1
    for i in range(n):
        p *= t
        t += 1
    return p


def first_gauss_product_t(t, n):
    p = 1
    t1 = t2 = t
    for i in range(n):
        if i % 2 != 0:
            p *= t1
            t2 -= 1
        else:
            p *= t2
            t1 += 1
    return p


def second_gauss_product_t(t, n):
    p = 1
    t1 = t2 = t
    for i in range(n):
        if i % 2 != 0:
            p *= t1
            t2 += 1
        else:
            p *= t2
            t1 -= 1
    return p


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
    for i in range(n):
        s += diff_matrix[0][i] * first_newton_product_t(t, i) / math.factorial(i)
    return s


def second_newton_formula(dot, border, h, diff_matrix, n):
    s = 0
    t = (dot - border) / h
    for i in range(n):
        s += diff_matrix[n - 1 - i][i] * second_newton_product_t(t, i) / math.factorial(i)
    return s


def first_gauss_get_coef(diff_matrix, n, i):
    return diff_matrix[(n - i) // 2][i]


def second_gauss_get_coef(diff_matrix, n, i):
    return diff_matrix[(n - i - 1) // 2][i]


def first_gauss_formula(dot, border, h, diff_matrix, n):
    s = 0
    t = (dot - border) / h
    for i in range(n):
        s += first_gauss_get_coef(diff_matrix, n, i) * first_newton_product_t(t, i) / math.factorial(i)
    return s


def second_gauss_formula(dot, border, h, diff_matrix, n):
    s = 0
    t = (dot - border) / h
    for i in range(n):
        s += second_gauss_get_coef(diff_matrix, n, i) * second_newton_product_t(t, i) / math.factorial(i)
    return s


def lagrange(pairs, dot):
    s = 0
    n = len(pairs)
    for i in range(n):
        s += pairs[i][1] * calc_lagr_coef(pairs, i, dot, n)
    return s
