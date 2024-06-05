import os
import signal
from math import inf

MAX_ITERS = 20

def my_input(str):
    s = input(str)
    if (s == 'q'):
        print("! Выход из программы.")
        os.kill(os.getpid(), signal.SIGINT)
    else:
        return s


def run_methods(f, exact_y, x0, xn, y0, h, eps, n):
    print()
    methods = [("Метод Эйлера", euler_method),
               ("Метод Рунге-Кутта 4-го порядка", fourth_order_runge_kutta_method),
               ("Метод Милна", milne_method)]

    for name, method in methods:
        ni = n
        print(name + ":\n")

        try:
            iters = 0

            xs = [x0 + i * ((xn - x0) / ni) for i in range(ni)]
            ys = method(f, xs, y0, eps)
            inaccuracy = inf

            while inaccuracy > eps:
                if (iters >= MAX_ITERS):
                    print(f"! Не удалось увеличить точность. Произведено {iters} итераций.")
                    break

                iters += 1
                ni *= 2
                xs = [x0 + i * (xn - x0) / ni for i in range(ni)]
                new_ys = method(f, xs, y0, eps)

                if method is milne_method:
                    inaccuracy = max([abs(exact_y(x, x0, y0) - y) for x, y in zip(xs, new_ys)])
                else:
                    p = 4 if method is fourth_order_runge_kutta_method else 2
                    coef = 2 ** p - 1
                    inaccuracy = abs(new_ys[-1] - ys[-1]) / coef

                ys = new_ys.copy()
            if iters != 1:
                print(
                    f"Для точности eps={eps} интервал был разбит на n={ni} частей с шагом h={round((xn - x0) / ni, 6)} за {iters} итераций.\n")
            else:
                print(
                    f"Для точности eps={eps} интервал был разбит на n={ni} частей с шагом h={round((xn - x0) / ni, 6)}.\n")
            if len(xs) < 100:
                print("y:\t[", *map(lambda x: round(x, 5), ys), "]")
                print("y_точн:\t[", *map(lambda x: round(exact_y(x, x0, y0), 5), xs), "]")
            elif my_input("Показать все значения y (количество > 100)? [y/n]: ") == 'y':
                print("y:\t[", *map(lambda x: round(x, 5), ys), "]")
                print("y_точн:\t[", *map(lambda x: round(exact_y(x, x0, y0), 5), xs), "]")
            print()
            if method is milne_method:
                print(f"Погрешность (max|y_iточн - y_i|): {inaccuracy}")
            else:
                print(f"Погрешность (по правилу Рунге): {inaccuracy}")
        except OverflowError:
            print('-' * 30 + '\n')
            print("! Невозможно вычислить. Число/точность слишком большое.")
        print('-' * 30)


def euler_method(f, xs, y0, eps):
    x0 = xs[0]
    xn = xs[-1]
    h = xs[1] - xs[0]
    ys = []
    while x0 <= xn:
        y = y0 + h * f(x0, y0)
        x0 += h
        xs.append(round(x0, 3))
        ys.append(round(y0, 5))
        y0 = y
    return ys


def fourth_order_runge_kutta_method(f, xs, y0, eps):
    # ni = int((xn - x0) / h)
    # xs = [x0 + i * ((xn - x0) / ni) for i in range(ni + 1)]
    ys = [y0]
    h = xs[1] - xs[0]
    for i in range(len(xs)):
        k1 = h * f(xs[i], ys[i])
        k2 = h * f(xs[i] + h / 2, ys[i] + k1 / 2)
        k3 = h * f(xs[i] + h / 2, ys[i] + k2 / 2)
        k4 = h * f(xs[i] + h, ys[i] + k3)
        ys.append(ys[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
    # xs = [round(x, 3) for x in xs]
    ys = [round(y, 6) for y in ys][:-1]
    return ys


def milne_method(f, xs, y0, eps):
    # ni = int((xn - x0) / h)
    # xs = [x0 + i * ((xn - x0) / ni) for i in range(ni + 1)]
    n = len(xs)
    h = xs[1] - xs[0]
    y = [y0]
    for i in range(1, 4):
        k1 = h * f(xs[i - 1], y[i - 1])
        k2 = h * f(xs[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(xs[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(xs[i - 1] + h, y[i - 1] + k3)
        y.append(y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    for i in range(4, n):
        # Предиктор
        yp = y[i - 4] + 4 * h * (2 * f(xs[i - 3], y[i - 3]) - f(xs[i - 2], y[i - 2]) + 2 * f(xs[i - 1], y[i - 1])) / 3

        # Корректор
        y_next = yp
        while True:
            yc = y[i - 2] + h * (f(xs[i - 2], y[i - 2]) + 4 * f(xs[i - 1], y[i - 1]) + f(xs[i], y_next)) / 3
            if abs(yc - y_next) < eps:
                y_next = yc
                break
            y_next = yc

        y.append(y_next)
    # xs = [round(x, 3) for x in xs]
    y = [round(yi, 6) for yi in y]
    return y
