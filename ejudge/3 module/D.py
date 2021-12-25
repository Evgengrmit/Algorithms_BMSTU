from math import ceil, log2, log
from re import fullmatch
from sys import stdin, exit
from copy import deepcopy

class BloomFilter:
    class BitArray:
        def __init__(self, size):
            self.data = bytearray(ceil(size / 8))
            self.size = size

        def __getitem__(self, item):
            bin_num, offset = item // 8, item % 8
            if self.data[bin_num] & 1 << offset:
                return 1

            return 0

        def set(self, key):
            if not self[key]:
                self.data[key // 8] += 1 << key % 8

        def __str__(self):
            res_arr = ["" for _ in range(self.size)]
            for i in range(self.size):
                res_arr[i] = str(self[i])

            return "".join(res_arr)

    M = 2 ** 31 - 1

    def prime_array(self, len):
        res = [0 for _ in range(len)]
        res[0] = 2
        initiated = 1
        counter = 2
        while initiated != len:
            for i in range(initiated):
                if counter % res[i] == 0:
                    counter += 1
                    break
            else:
                res[initiated] = counter
                initiated += 1

        return res

    def __init__(self, n, P):
        if round(-log2(P)) < 1:
            raise ValueError
        self.hashes = round(-log2(P))  # k
        self.size = round(-n * log2(P) / log(2))  # m
        self.array = self.BitArray(self.size)
        self.primes_list = self.prime_array(self.hashes)

    def stats(self):
        return {"m": self.size, "k": self.hashes}

    def __str__(self):
        return str(self.array)

    def _ith_hash(self, i, value):
        return (((i + 1) * value + self.primes_list[i]) % self.M) % self.size

    def add(self, value):
        for i in range(self.hashes):
            self.array.set(self._ith_hash(i, value))

    def __contains__(self, item):
        for i in range(self.hashes):
            if self.array[self._ith_hash(i, item)] == 0:
                return False
        else:
            return True


if __name__ == "__main__":
    reg_set = r"set \d+ 0.\d+"
    reg_add = r"add \d+"
    reg_search = r"search \d+"

    filter = None
    while filter is None:
        for line in stdin:
            line = line.rstrip("\n")
            if line == "":
                continue

            if not fullmatch(reg_set, line):
                print("error")
            else:
                _, n, P = line.split()
                n, P = int(n), float(P)

                if n == 0 or P >= 1 or P <= 0:
                    print("error")
                    continue
                try:
                    filter = BloomFilter(int(n), float(P))
                except ValueError:
                    print("error")
                    continue

                print(filter.stats()["m"], filter.stats()["k"])
                break
        else:
            exit()

    for line in stdin:
        line = line.rstrip("\n")
        if line == "":
            continue
        if fullmatch(reg_add, line):
            val = int(line.split()[-1])
            filter.add(val)

        elif fullmatch(reg_search, line):
            target = int(line.split()[-1])
            print(int(target in filter))

        elif line == "print":
            print(filter)

        else:
            print("error")