from lab5.interpolation import *
import sys


def func_to_pairs(func, borders, count):
    step = (borders[1] - borders[0]) / (count - 1)
    pairs = [[borders[0] + i * step, func(borders[0] + i * step)] for i in range(count)]
    return pairs


def my_func_1(x):
    return math.exp(x)


def my_func_2(x):
    return x ** 2


def main():
    strings = []
    for i in range(1, 25):
        try:
            strings.append(
                sys.argv[i].replace("x:", "").replace("pairs:", "").replace("{", "").replace("}", "").replace("[[", "").replace("]]",
                                                                                                              "").replace(
                    ",", "").replace("x=", "").replace("y=", ""))
        except IndexError:
            continue
    pairs = []
    last = ""
    strings[-1], x = strings[-1].split("[")
    x = x.replace("]", "")
    for str in strings:
        if last == "":
            last = str
        else:
            pairs.append([float(last), float(str)])
            last = ""

    number = 0
    borders = [0, 4]
    count = 5
    pairs = func_to_pairs(my_func_1 if number else my_func_2, borders, count)

    run_methods(pairs, float(x))


if __name__ == "__main__":
    main()
