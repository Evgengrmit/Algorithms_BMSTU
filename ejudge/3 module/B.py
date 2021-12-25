from collections import deque


class Solver:
    @staticmethod
    def __first_zeros_len(value):
        res = 0
        temp_val = value
        while temp_val / 2 == temp_val // 2 and temp_val / 2 != 0:
            temp_val /= 2
            res += 1

        return res

    @classmethod
    def solve(cls, value):
        ans = deque()

        while value:
            if value & 1 == 1:

                if value >= 5:
                    if cls.__first_zeros_len(value + 1) >= cls.__first_zeros_len(value - 1):
                        ans.append("dec")
                        value += 1
                    else:
                        ans.append("inc")
                        value -= 1
                else:
                    ans.append("inc")
                    value -= 1
            else:
                ans.append("dbl")
                value >>= 1
        ans.reverse()
        return ans


if __name__ == "__main__":
    num = input()
    if not num.isdigit():
        print("error")
        raise Exception("NaN input")

    sequence = Solver.solve(int(num))
    for e in sequence:
        print(e)
