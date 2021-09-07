def next_permutation(iterable):
    if n <= 1:
        return False
    for it in reversed(range(len(iterable) - 1)):
        if iterable[it] < iterable[it + 1]:
            for j in reversed(range(it + 1, n)):
                if iterable[it] < iterable[j]:
                    iterable[it], iterable[j] = iterable[j], iterable[it]
                    iterable[it + 1:] = reversed(iterable[it + 1:])
                    return True
    else:
        return False


def all_permutations(number):
    massive = [el for el in range(1, number + 1)]
    while True:
        yield tuple(massive)
        if not next_permutation(massive):
            break


if __name__ == '__main__':
    n = int(input())
    for i in all_permutations(n):
        print(i)
