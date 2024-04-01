import sys


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
    while abs(borders[0] - borders[1]) > error and abs(calc_func(coefficients, dim, x)) >= error:
        x = (borders[0] + borders[1]) / 2
        if calc_func(coefficients, dim, borders[0]) * calc_func(coefficients, dim, x) > 0:
            borders[0] = x
        else:
            borders[1] = x
        n += 1
    x = (borders[0] + borders[1]) / 2
    keys = ["x", "f(x)", "count of operation"]
    # print("hello")
    print_answers(3, [x, calc_func(coefficients, dim, x), n], keys)


def main():
    type = (sys.argv[1])

    if str(type) == "true":
        input_variant = int(1)
    else:
        input_variant = int(2)

    print(input_variant)
    if input_variant == 1:
        bisection_alg([1, 2], [5, 1, 2], 3, 0.01)


if __name__ == "__main__":
    print(12)
    main()
