from math import gcd
from re import fullmatch
from sys import stdin, exit


class Solver:
    @staticmethod
    def build_table(m_weight, items):
        table = [[0] * (m_weight + 1) for _ in range(len(items) + 1)]
        for i in range(1, len(items) + 1):
            for j in range(1, m_weight + 1):
                old_val = table[i - 1][j]
                if items[i - 1][0] <= j:
                    new_val = items[i - 1][1] + table[i - 1][j - items[i - 1][0]]
                    if new_val > old_val:
                        table[i][j] = new_val
                        continue

                table[i][j] = old_val

        return table

    @staticmethod
    def create_item_list(table, items):
        max_weight = len(table[0]) - 1
        price = table[len(table) - 1][max_weight]
        j = max_weight
        indexes = []

        for e in items:
            if e[0] == 0:
                indexes.append(e[2])

        for i in range(len(table), 0, -1):
            if table[i - 1][j] < price:
                indexes.append(i)
                price -= items[i - 1][1]
                if price <= 0:
                    return set(indexes)
                j -= items[i - 1][0]

        return set(indexes)

    @classmethod
    def solve(self, max_weight, items):
        common_w_gcd = items[0][0]
        for i in range(1, len(items)):
            common_w_gcd = gcd(common_w_gcd, items[i][0])

        if common_w_gcd != 1:
            max_weight //= common_w_gcd
            for i, e in enumerate(items):
                items[i][0] = e[0] // common_w_gcd

        table = self.build_table(max_weight, items)
        opt_indexes = self.create_item_list(table, items)

        total_weight = 0
        total_cost = 0
        for ind in opt_indexes:
            total_weight += items[ind - 1][0]
            total_cost += items[ind - 1][1]

        total_weight *= common_w_gcd

        return total_weight, total_cost, opt_indexes


if __name__ == "__main__":
    max_weight = None
    while max_weight is None:
        for line in stdin:
            line = line.rstrip("\n")
            if fullmatch(r"\d+", line):
                max_weight = int(line)
                break
            elif line == "":
                pass
            else:
                print("error")
        else:
            exit()

    items = []

    index_counter = 0
    for line in stdin:
        line = line.rstrip("\n")
        if fullmatch(r"\d+ \d+", line):
            index_counter += 1
            w, c = line.split()
            items.append([int(w), int(c), index_counter])
        elif line != "":
            print("error")

    # pprint(Solver.build_table(max_weight, items))
    res_w, res_c, res_ind = Solver.solve(max_weight, items)
    print(res_w, res_c)
    for e in res_ind:
        print(e)