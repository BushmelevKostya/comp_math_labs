def print_diff_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(round(matrix[i][j], 2), end=" ")
        print()


def lagrange_output(res, dot, eq):
    print("Lagrange method - result value f(", dot, "): ", round(res, 4))
    print(f"Lagrange equation: {eq}")


def newton_output(res, dot, eq):
    print("Newton method - result value f(", dot, "): ", round(res, 4))
    print(f"Newton equation: {eq}")


def gauss_output(res, dot, eq):
    print("Gauss method - result value f(", dot, "): ", round(res, 4))
    print(f"Gauss equation: {eq}")


def stirling_output(res, dot, eq):
    print("Stirling method - result value f(", dot, "): ", round(res, 4))
    print(f"Stirling equation: {eq}")


def bessel_output(res, dot, eq):
    print("Bessel method - result value f(", dot, "): ", res)
