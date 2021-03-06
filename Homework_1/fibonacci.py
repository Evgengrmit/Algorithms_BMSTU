class MatrixFibonacci:

    def __init__(self):
        self.P = [[1, 1], [1, 0]]

    def __mul__(self, other):
        t = MatrixFibonacci()
        for i_ in range(2):
            for j_ in range(2):
                cell = 0
                for k in range(2):
                    cell += self.P[i_][k] * other.P[k][j_]
                t.P[i_][j_] = cell
        return t

    def __imul__(self, other):
        self.P = (self * other).P
        return self

    def __pow__(self, power, modulo=None):
        n_ = MatrixFibonacci()
        result = MatrixFibonacci()
        while power > 0:
            if power % 2 == 1:
                result *= n_
            n_ *= n_
            power >>= 1
        return result


def getFibonacci(number):
    p = MatrixFibonacci()
    return (p ** number).P[1][1]


if __name__ == '__main__':
    n = int(input())
    print(getFibonacci(n))
