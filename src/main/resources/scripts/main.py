import sys
from lab4.approximation import find_best_method

def main():
    strings = []
    for i in range(1, 25):
        try:
            strings.append(sys.argv[i].replace("pairs:", "").replace("{", "").replace("}", "").replace("[[", "").replace("]]", "").replace(",", "").replace("x=", "").replace("y=", ""))
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
    find_best_method(pairs)


if __name__ == "__main__":
    main()
