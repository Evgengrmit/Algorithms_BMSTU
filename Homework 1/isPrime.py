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


print(isPrimeSimple(23))
