class FileReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_matrix(self, dim):
        matrix = []
        try:
            with open(self.filepath, "r") as file:
                file.readline()
                for i in range(dim):
                    data = list(map(float, file.readline().replace(",", ".").split(" ")))
                    matrix.append(data)
            return matrix
        except FileNotFoundError:
            raise FileNotFoundError("This file doesn't exist! Try another name of file")
        except PermissionError:
            raise FileNotFoundError("You haven't enough permissions for read this file! Try another name of file")
        except ValueError:
            raise FileNotFoundError("Wrong type in matrix!")
        except IndexError:
            raise FileNotFoundError("Data in matrix is not valid")

    def read_vars(self, dim):
        try:
            with open(self.filepath, "r") as file:
                if dim != 1:
                    data = list(map(float, file.readlines()[0].replace(",", ".").strip().split(" ")))
                else:
                    data = list(map(float, file.readlines()[1].replace(",", ".").strip().split(" ")))
                if len(data) < dim:
                    raise IndexError
            return data
        except FileNotFoundError:
            raise FileNotFoundError("This file doesn't exist! Try another name of file")
        except PermissionError:
            raise FileNotFoundError("You haven't enough permissions for read this file! Try another name of file")
        except ValueError:
            raise FileNotFoundError("Wrong type in variables!")
        except IndexError:
            raise FileNotFoundError("Data in variables is not valid")

    def read_dim(self):
        try:
            with open(self.filepath, "r") as file:
                data = int(file.readline())
            return data
        except FileNotFoundError:
            raise FileNotFoundError("This file doesn't exist! Try another name of file")
        except PermissionError:
            raise FileNotFoundError("You haven't enough permissions for read this file! Try another name of file")
        except ValueError:
            raise FileNotFoundError("Wrong type in dimension!")
        except IndexError:
            raise FileNotFoundError("Data in dimension is not valid")

    def write_answer(self, keys, value, dim):
        try:
            with open(self.filepath, "w") as file:
                for i in range(dim):
                    file.write(str(keys[i]) + " = " + str(round(value[i], 5)) + "\n")
        except FileNotFoundError:
            raise FileNotFoundError("This file doesn't exist! Try another name of file")
        except PermissionError:
            raise FileNotFoundError("You haven't enough permissions for read this file! Try another name of file")