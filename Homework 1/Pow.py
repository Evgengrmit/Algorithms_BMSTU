def Pow(number, degree):
    result = 1
    while degree > 0:
        if degree % 2 == 1:
            result *= number
        number *= number
        degree >>= 1
    return result


if __name__ == '__main__':
    print(Pow(3, 11))
