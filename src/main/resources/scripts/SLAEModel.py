import math
import sympy as sp
import numpy as np

from FileReader import FileReader
from Model import *


class SLAEModel:
    def print_answers(self, dim, arr_var, keys):
        print("Please enter:\n"
              "1 for console output\n"
              "2 for file output\n"
              ">>>", end=" ")
        while 1:
            s = input().strip()
            if s == "1":
                for i in range(dim):
                    print(keys[i], " = ", round(arr_var[i], 5), sep="")
                print()
                break
            elif s == "2":
                while 1:
                    print("Please enter name of file\n>>>", end=" ")
                    s = input().strip()
                    if s == "":
                        continue
                    path = "output/" + s
                    fileReader = FileReader(path)
                    try:
                        fileReader.write_answer(keys, arr_var, dim)
                        break
                    except FileNotFoundError as e:
                        print(e.args[0])
                break
            else:
                print("Wrong value! Please enter:\n"
                      "1 for console output\n"
                      "2 for file output\n"
                      ">>>", end=" ")

    def calc_func(self, coefficients, dim, dot):
        res = 0
        for i in range(dim + 1):
            res += coefficients[i] * dot ** i

        return res

    def bisection_alg(self, borders, coefficients, dim, error):
        n = 0
        x = (borders[0] + borders[1]) / 2
        while abs(borders[0] - borders[1]) > error and abs(self.calc_func(coefficients, dim, x)) >= error:
            x = (borders[0] + borders[1]) / 2
            if self.calc_func(coefficients, dim, borders[0]) * self.calc_func(coefficients, dim, x) > 0:
                borders[0] = x
            else:
                borders[1] = x
            n += 1
        x = (borders[0] + borders[1]) / 2
        keys = ["x", "f(x)", "count of operation"]
        self.print_answers(3, [x, self.calc_func(coefficients, dim, x), n], keys)

    def secant_alg(self, approx, coefficients, dim, error):
        n = 0
        func_values = [self.calc_func(coefficients, dim, approx[0]), self.calc_func(coefficients, dim, approx[1])]
        while abs(approx[1] - approx[0]) > error and abs(self.calc_func(coefficients, dim, approx[1])):
            derivative = (func_values[1] - func_values[0]) / (approx[1] - approx[0])
            next_x = approx[1] - self.calc_func(coefficients, dim, approx[1]) / derivative
            approx[0], approx[1] = approx[1], next_x
            next_y = self.calc_func(coefficients, dim, approx[1])
            func_values[0], func_values[1] = func_values[1], next_y
            n += 1
        keys = ["x", "f(x)", "count of operation"]
        self.print_answers(3, [approx[1], self.calc_func(coefficients, dim, approx[1]), n], keys)

    def simple_iteration_alg(self, approx, coefficients, dim, error):
        f = sum(coefficients[i] * approx[0] ** i for i in range(len(coefficients)))
        df = sp.diff(f, approx[0])
        g = approx[0] - f / df

        g_func = sp.lambdify(approx[0], g, 'numpy')

        xn = approx[1]
        n = 0
        while 1:
            n += 1
            xn_plus_1 = g_func(xn)
            if abs(xn_plus_1 - xn) < error:
                break
            xn = xn_plus_1
        keys = ["x", "f(x)", "count of operation"]
        self.print_answers(dim, [xn_plus_1, g_func(xn_plus_1), n], keys)

    def simple_iteration_transcendental_alg(self, approx, error):
        n = 1
        while 1:
            approx[1] = math.log2(math.cos(approx[0]) + 3)
            if abs(approx[1] - approx[0]) < error:
                break
            approx[0] = approx[1]
            n += 1
        keys = ["x", "count of operation"]
        self.print_answers(2, [approx[1], n], keys)

    def Newton_alg(self, approx, error, dim):
        coefficients = [[0, 0], [0, 0]]
        arr_values = [0, 0]
        n = 1
        while 1:
            coefficients[0][0], coefficients[0][1] = 2 * approx[0], 2 * approx[1]
            coefficients[1][0], coefficients[1][1] = -6 * approx[0], 1
            arr_values[0], arr_values[1] = 4 - approx[0] ** 2 - approx[1] ** 2, 3 * approx[0] ** 2 - approx[1]
            model = Model(2, coefficients, arr_values)
            temp = approx.copy()
            roots = model.G_alg()
            approx[0], approx[1] = approx[0] + roots[0], approx[1] + roots[1]
            if abs(approx[0] - temp[0]) <= error and abs(approx[1] - temp[1]) <= error:
                break
            n += 1
        keys = ["x", "y", "count of operation"]
        self.print_answers(dim, [approx[0], approx[1], n], keys)

    import math

    def Newton_transcendental_alg(self, approx, error, dim):
        n = 1
        while True:
            A = math.sin(approx[0]) - 1
            B = -math.sin(approx[1])
            C = -0.5 + approx[1] + math.cos(approx[0] - 1)
            D = -3 + approx[0] - math.cos(approx[1])
            coefficients = [[A, 0], [0, B]]
            arr_values = [C, D]
            model = Model(2, coefficients, arr_values)
            temp = approx.copy()
            roots = model.G_alg()
            approx[0] += roots[0]
            approx[1] += roots[1]
            if abs(approx[0] - temp[0]) <= error and abs(approx[1] - temp[1]) <= error:
                break
            n += 1
        keys = ["x", "y", "count of operation"]
        self.print_answers(dim, [approx[0], approx[1], n], keys)

    def create_polinim(self, num):
        coefficients = []
        if num == 1:
            x = sp.Symbol('x')
            f = 2 ** x - sp.cos(x - 1) - 3
            taylor_series = f.series(x, 0, 5).removeO()
            coefficients = [taylor_series.coeff(x, i).evalf() for i in range(6)]
        return coefficients

    def do_task(self, approx, coefficients, dim, error, number):
        if number == 1:
            self.bisection_alg(approx, coefficients, dim, error)
        elif number == 2:
            self.secant_alg(approx, coefficients, dim, error)
        elif number == 3:
            approx[0] = sp.Symbol('x')
            self.simple_iteration_alg(approx, coefficients, dim, error)

    def check_roots(self, coefficients, borders):
        if borders[1] <= borders[0]:
            return False

        left_value = np.polyval(coefficients, borders[0])
        right_value = np.polyval(coefficients, borders[1])

        if np.sign(left_value) == np.sign(right_value):
            return False

        return True
