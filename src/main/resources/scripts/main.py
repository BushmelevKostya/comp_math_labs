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
                sys.argv[i].replace("pairs:", "").replace("{", "").replace("}", "").replace("[[", "").replace("]]",
                                                                                                              "").replace(
                    ",", "").replace("x=", "").replace("y=", ""))
        except IndexError:
            continue
    pairs = []
    last = ""
    for str in strings:
        if last == "":
            last = str
        else:
            pairs.append([float(last), float(str)])
            last = ""
    run_methods(pairs, 4.5)


if __name__ == "__main__":
    main()
