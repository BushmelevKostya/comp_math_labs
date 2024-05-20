def print_diff_matrix(matrix, n):
    print("Matrix of differences is:")
    for i in range(n):
        for j in range(n):
            print("{:.2f}".format(matrix[i][j]), end="\t")
        print()

def lagrange_output(res, dot):
    print("Lagrange method - result value f(", dot, "): ", round(res, 4))


def newton_output(res, dot):
    print("Newton method - result value f(", dot, "): ", round(res, 4))


def gauss_output(res, dot):
    print("Gauss method - result value f(", dot, "): ", round(res, 4))
