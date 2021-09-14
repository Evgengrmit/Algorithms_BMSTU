import sys
import re


def func():
    summary = 0
    for number in re.findall(r'-?\d+', sys.stdin.read()):
        summary += int(number)
    return summary


if __name__ == '__main__':
    print(func())
