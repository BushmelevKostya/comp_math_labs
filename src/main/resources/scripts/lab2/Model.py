class Model:
    def __init__(self, dim, matrix, arr_var):
        self.dim = dim
        self.matrix = matrix
        self.arr_var = arr_var

    def det(self):
        arr = list(range(self.dim))
        arr_perm = self.generate_permutations(arr)
        return self.sum_permutations(arr_perm, self.matrix)

    def check_sign(self, perm):
        return self.count_inversions(perm) % 2 == 0

    def count_inversions(self, perm):
        res = 0
        dim = self.dim
        for i in range(dim):
            for j in range(i, dim):
                if perm[i] > perm[j]:
                    res += 1
        return res

    def mul_permutations(self, perm, matrix):
        mul = 1
        for i in range(self.dim):
            mul *= matrix[i][perm[i]]
        return mul

    def sum_permutations(self, arr_perm, matrix):
        res = 0
        for i in range(len(arr_perm)):
            sign = 1 if self.check_sign(arr_perm[i]) else -1
            res += self.mul_permutations(arr_perm[i], matrix) * sign
        return res

    def fact(self, n):
        if n < 0:
            return "error: please, enter positive number for factorial"
        return self.fact(n - 1) * n if n > 0 else 1

    def generate_permutations(self, arr, start=0):
        dim = self.dim
        permutations = []
        if start == dim:
            permutations.append(arr[:])
        else:
            for i in range(start, dim):
                arr[start], arr[i] = arr[i], arr[start]
                permutations += self.generate_permutations(arr, start + 1)
                arr[start], arr[i] = arr[i], arr[start]
        return permutations

    def print_matrix(self, matrix):
        for i in range(self.dim):
            print("|  ", end="")
            for j in range(self.dim):
                print("{: <3}".format(matrix[i][j]), end="  ")
            print("|\n")

    def print_answers(self, arr_var):
        for i in range(self.dim):
            print("x", i + 1, " = ", round(arr_var[i], 5), sep="")
        print()

    def G_alg(self):
        matrix = self.matrix
        arr_var = self.arr_var
        dim = self.dim
        results = [0] * dim
        count_perm = 0
        for i in range(0, dim - 1):
            if matrix[i][i] == 0:
                matrix = self.change_lines(matrix, i)
                count_perm += 1
            for k in range(i + 1, dim):
                c = matrix[k][i] / matrix[i][i]
                matrix[k][i] = 0
                for j in range(i + 1, dim):
                    matrix[k][j] = matrix[k][j] - c * matrix[i][j]
                arr_var[k] = arr_var[k] - c * arr_var[i]
        # self.print_triangle_matrix(matrix, arr_var)
        det = self.triangle_det(matrix, count_perm)
        if self.check_det(det) == 0:
            return -1
        for i in range(dim - 1, -1, -1):
            s = 0
            for j in range(i + 1, dim):
                s += matrix[i][j] * results[j]
            results[i] = (arr_var[i] - s) / matrix[i][i]
        return results

    def change_lines(self, matrix, n):
        for i in range(n + 1, self.dim):
            if matrix[i][n] != 0:
                matrix[n], matrix[i] = matrix[i], matrix[n]
                return matrix
        return -1

    def calc_errors(self, results):
        matrix = self.matrix
        dim = self.dim
        arr_vars = self.arr_var
        arr_errors = [0] * dim
        for i in range(dim):
            s = 0
            for j in range(dim):
                s += matrix[i][j] * results[j]
            arr_errors[i] = abs(arr_vars[i] - s)
        return arr_errors

    def print_task(self, matrix, arr_var):
        for i in range(self.dim):
            print("|  ", end="")
            for j in range(self.dim):
                print("{: <9}".format(round(matrix[i][j], 5)), end="  ")
            print("|  = ", round(arr_var[i], 5), "\n")

    def print_triangle_matrix(self, matrix, arr_var):
        print("Triangle matrix: ")
        self.print_task(matrix, arr_var)

    def check_det(self, det):
        if det != 0:
            # print("Determinant:", det, "\n")
            return 1
        else:
            # print("Determinant of matrix = 0, please try another matrix!")
            return 0

    def triangle_det(self, matrix, count_perm):
        dim = self.dim
        p = 1
        for i in range(dim):
            p *= matrix[i][i]
        return p * (-1) ** count_perm




