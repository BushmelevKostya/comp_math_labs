import math

from sympy import symbols, Eq, solve
from lab4.validate import try_to_int
from lab4.output import *


def find_best_method(pairs):
    answers = [linear_approx(pairs), polinom_2_approx(pairs), polinom_3_approx(pairs), power_approx(pairs),
               exp_approx(pairs), log_approx(pairs)]
    best_num = 0
    best_sqr_diff = 10 ** 10
    for i in range(6):
        try:
            if answers[i][3] < best_sqr_diff:
                best_num = i
                best_sqr_diff = answers[i][3]
        except TypeError:
            continue
    print_best_answer(answers, best_num)


def linear_approx(pairs):
    s_x = 0
    s_xx = 0
    s_y = 0
    s_xy = 0
    # calc sum
    for pair in pairs:
        s_x += pair[0]
        s_xx += pair[0] ** 2
        s_y += pair[1]
        s_xy += pair[0] * pair[1]
    # calc coefs
    delta = s_xx * len(pairs) - s_x ** 2
    delta1 = s_xy * len(pairs) - s_x * s_y
    delta2 = s_xx * s_y - s_x * s_xy
    a = delta1 / delta
    b = delta2 / delta
    # calc diff
    new_pairs = []
    diff = []
    sqr_diff = 0
    for pair in pairs:
        new_pairs.append([pair[0], a * pair[0] + b])
        diff.append(new_pairs[-1][1] - pair[1])
        sqr_diff += diff[-1] ** 2
    sqr_diff /= (len(pairs))
    sqr_diff = sqr_diff ** 0.5
    # pirson
    x_avg = s_x / len(pairs)
    y_avg = s_y / len(pairs)
    chisl = 0
    znam1 = 0
    znam2 = 0
    for pair in pairs:
        chisl += (pair[0] - x_avg) * (pair[1] - y_avg)
        znam1 += (pair[0] - x_avg) ** 2
        znam2 += (pair[1] - y_avg) ** 2
    r = chisl / (znam1 * znam2) ** 0.5
    # det_coef
    fi_avg = 0
    for pair in new_pairs:
        fi_avg += pair[1]
    fi_avg /= len(pairs)
    chisl = 0
    znam = 0
    for i in range(len(pairs)):
        chisl += (pairs[i][1] - new_pairs[i][1]) ** 2
        znam += (pairs[i][1] - fi_avg) ** 2
    R = 1 - chisl / znam
    return [pairs, new_pairs, diff, sqr_diff, r, R, [a, b]]


def polinom_2_approx(pairs):
    s_x = 0
    s_xx = 0
    s_xxx = 0
    s_xxxx = 0
    s_y = 0
    s_xy = 0
    s_xxy = 0
    # calc sum
    for pair in pairs:
        s_x += pair[0]
        s_xx += pair[0] ** 2
        s_xxx += pair[0] ** 3
        s_xxxx += pair[0] ** 4
        s_y += pair[1]
        s_xy += pair[0] * pair[1]
        s_xxy += pair[0] ** 2 * pair[1]
    # calc coefs
    x, y, z = symbols("x y z")

    eq1 = Eq(len(pairs) * x + s_x * y + s_xx * z, s_y)
    eq2 = Eq(s_x * x + s_xx * y + s_xxx * z, s_xy)
    eq3 = Eq(s_xx * x + s_xxx * y + s_xxxx * z, s_xxy)
    solution = solve((eq1, eq2, eq3), (x, y, z))

    a0 = try_to_int(solution[x])
    a1 = try_to_int(solution[y])
    a2 = try_to_int(solution[z])
    # calc diff
    new_pairs = []
    diff = []
    sqr_diff = 0
    for pair in pairs:
        new_pairs.append([pair[0], a0 + a1 * pair[0] + a2 * pair[0] ** 2])
        diff.append(new_pairs[-1][1] - pair[1])
        sqr_diff += diff[-1] ** 2
    sqr_diff /= (len(pairs))
    # det_coef
    fi_avg = 0
    for pair in new_pairs:
        fi_avg += pair[1]
    fi_avg /= len(pairs)
    chisl = 0
    znam = 0
    for i in range(len(pairs)):
        chisl += (pairs[i][1] - new_pairs[i][1]) ** 2
        znam += (pairs[i][1] - fi_avg) ** 2
    R = 1 - chisl / znam
    return [pairs, new_pairs, diff, sqr_diff, R, [a0, a1, a2]]


def polinom_3_approx(pairs):
    s_x = 0
    s_y = 0
    s_xx = 0
    s_yy = 0
    s_xy = 0
    s_xxx = 0
    s_xxy = 0
    s_xyy = 0
    s_xxxx = 0
    s_xxyy = 0

    for pair in pairs:
        x = pair[0]
        y = pair[1]
        s_x += x
        s_y += y
        s_xx += x * x
        s_yy += y * y
        s_xy += x * y
        s_xxx += x * x * x
        s_xxy += x * x * y
        s_xyy += x * y * y
        s_xxxx += x * x * x * x
        s_xxyy += x * x * y * y
    x, y, z, w = symbols("x y z w")

    eq1 = Eq(len(pairs) * w + s_x * x + s_xx * y + s_xxx * z, s_y)
    eq2 = Eq(s_x * w + s_xx * x + s_xxx * y + s_xxxx * z, s_xy)
    eq3 = Eq(s_xx * w + s_xxx * x + s_xxxx * y + s_xxyy * z, s_xxy)
    eq4 = Eq(s_xxx * w + s_xxxx * x + s_xxyy * y + s_xyy * z, s_xxx)
    solution = solve((eq1, eq2, eq3, eq4), (w, x, y, z))

    a0 = try_to_int(solution[w])
    a1 = try_to_int(solution[x])
    a2 = try_to_int(solution[y])
    a3 = try_to_int(solution[z])
    # calc diff
    new_pairs = []
    diff = []
    sqr_diff = 0
    for pair in pairs:
        new_pairs.append([pair[0], a0 + a1 * pair[0] + a2 * pair[0] ** 2 + a3 * pair[0] ** 3])
        diff.append(new_pairs[-1][1] - pair[1])
        sqr_diff += diff[-1] ** 2
    sqr_diff /= (len(pairs))
    # det_coef
    fi_avg = 0
    for pair in new_pairs:
        fi_avg += pair[1]
    fi_avg /= len(pairs)
    chisl = 0
    znam = 0
    for i in range(len(pairs)):
        chisl += (pairs[i][1] - new_pairs[i][1]) ** 2
        znam += (pairs[i][1] - fi_avg) ** 2
    R = 1 - chisl / znam
    return [pairs, new_pairs, diff, sqr_diff, R, [a0, a1, a2, a3]]


def power_approx(pairs):
    s_x = 0
    s_xx = 0
    s_y = 0
    s_xy = 0
    # calc sum
    for pair in pairs:
        try:
            x = math.log(pair[0])
            y = math.log(pair[1])
        except ValueError:
            print("Power approx can't be check. Please set positive argument for logarithmic function!")
            return
        s_x += x
        s_xx += x ** 2
        s_y += y
        s_xy += x * y
    # calc coefs
    b = (len(pairs) * s_xy - s_x * s_y) / (len(pairs) * s_xx - s_x ** 2)
    a = math.exp((s_y - b * s_x) / len(pairs))
    # calc diff
    new_pairs = []
    diff = []
    sqr_diff = 0
    for pair in pairs:
        new_pairs.append([pair[0], a * pair[0] ** b])
        diff.append(new_pairs[-1][1] - pair[1])
        sqr_diff += diff[-1] ** 2
    sqr_diff /= (len(pairs))
    sqr_diff = sqr_diff ** 0.5
    # det_coef
    fi_avg = 0
    for pair in new_pairs:
        fi_avg += pair[1]
    fi_avg /= len(pairs)
    chisl = 0
    znam = 0
    for i in range(len(pairs)):
        chisl += (pairs[i][1] - new_pairs[i][1]) ** 2
        znam += (pairs[i][1] - fi_avg) ** 2
    R = 1 - chisl / znam
    return [pairs, new_pairs, diff, sqr_diff, R, [a, b]]


def exp_approx(pairs):
    s_x = 0
    s_xx = 0
    s_y = 0
    s_xy = 0
    # calc sum
    for pair in pairs:
        try:
            x = pair[0]
            y = math.log(pair[1])
        except ValueError:
            print("Exponential approx can't be check. Please set positive argument for logarithmic function!")
            return
        s_x += x
        s_xx += x ** 2
        s_y += y
        s_xy += x * y
    # calc coefs
    b = (len(pairs) * s_xy - s_x * s_y) / (len(pairs) * s_xx - s_x ** 2)
    a = math.exp((s_y - b * s_x) / len(pairs))
    # calc diff
    new_pairs = []
    diff = []
    sqr_diff = 0
    for pair in pairs:
        new_pairs.append([pair[0], a * math.exp(pair[0] * b)])
        diff.append(new_pairs[-1][1] - pair[1])
        sqr_diff += diff[-1] ** 2
    sqr_diff /= (len(pairs))
    sqr_diff = sqr_diff ** 0.5
    # det_coef
    fi_avg = 0
    for pair in new_pairs:
        fi_avg += pair[1]
    fi_avg /= len(pairs)
    chisl = 0
    znam = 0
    for i in range(len(pairs)):
        chisl += (pairs[i][1] - new_pairs[i][1]) ** 2
        znam += (pairs[i][1] - fi_avg) ** 2
    R = 1 - chisl / znam
    return [pairs, new_pairs, diff, sqr_diff, R, [a, b]]


def log_approx(pairs):
    s_x = 0
    s_xx = 0
    s_y = 0
    s_xy = 0
    # calc sum
    for pair in pairs:
        try:
            x = math.log(pair[0])
            y = pair[1]
        except ValueError:
            print("Logarithmic approx can't be check. Please set positive argument for logarithmic function!")
            return
        s_x += x
        s_xx += x ** 2
        s_y += y
        s_xy += x * y
    # calc coefs
    a = (len(pairs) * s_xy - s_x * s_y) / (len(pairs) * s_xx - s_x ** 2)
    b = (s_y - a * s_x) / len(pairs)
    # calc diff
    new_pairs = []
    diff = []
    sqr_diff = 0
    for pair in pairs:
        new_pairs.append([pair[0], a * math.log(pair[0]) + b])
        diff.append(new_pairs[-1][1] - pair[1])
        sqr_diff += diff[-1] ** 2
    sqr_diff /= (len(pairs))
    sqr_diff = sqr_diff ** 0.5
    # det_coef
    fi_avg = 0
    for pair in new_pairs:
        fi_avg += pair[1]
    fi_avg /= len(pairs)
    chisl = 0
    znam = 0
    for i in range(len(pairs)):
        chisl += (pairs[i][1] - new_pairs[i][1]) ** 2
        znam += (pairs[i][1] - fi_avg) ** 2
    R = 1 - chisl / znam
    return [pairs, new_pairs, diff, sqr_diff, R, [a, b]]
