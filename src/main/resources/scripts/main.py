from lab6.methods import *
from math import *
import sys

# '1. y + (1 + x)*y^2'
# '2. x + y'
# '3. sin(x) - y'

def main():
    strings = []

    for i in range(1, 6):
        try:
            strings.append(
                sys.argv[i].replace("{", "").replace("[", "").replace("]", "").replace("}", "").replace("floatList:", "").replace("n:", "").replace("func:", ""))
        except IndexError:
            continue
    a, b, c = strings[-1].split(',')
    strings[-1] = strings[-1][:3]
    strings.append(b)
    strings.append(c)
    print(strings)
    num = strings[5]
    if num == "x":
        f = lambda x, y: y + (1 + x) * y ** 2
        exact_y = lambda x, x0, y0: -exp(x) / (x * exp(x) - (x0 * exp(x0) * y0 + exp(x0)) / y0)
    elif num == "y":
        f = lambda x, y: x + y
        exact_y = lambda x, x0, y0: exp(x - x0) * (y0 + x0 + 1) - x - 1
    else:
        f = lambda x, y: sin(x) - y
        exact_y = lambda x, x0, y0: (2 * exp(x0) * y0 - exp(x0) * sin(x0) + exp(x0) * cos(x0)) / (2 * exp(x)) + (
            sin(x)) / 2 - (cos(x)) / 2
    y0 = strings[0].replace(",", "")
    x0, xn = strings[1].replace(",", ""), strings[2].replace(",", "")
    h = strings[3].replace(",", "")
    eps = strings[4].replace(",", "")
    n = strings[5].replace(",", "")
    run_methods(f, exact_y, float(x0), float(xn), float(y0), float(h), float(eps), int(n))


if __name__ == "__main__":
    main()
