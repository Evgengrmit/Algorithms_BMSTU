from math import sqrt


def isPrimeSimple(a):
    if a == 1 or a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, int(sqrt(a)), 2):
        if a % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(isPrimeSimple(23))
