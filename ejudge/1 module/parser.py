import sys


def parse_string_to_sum() -> int:
    line = sys.stdin.read()
    summary = 0
    next_number = ''
    for symbol in line:
        if symbol == '-':
            if next_number != '-' and next_number != '':
                summary += int(next_number)
            next_number = symbol
            continue
        elif symbol.isdigit():
            next_number += symbol
            continue
        elif next_number != '':
            if next_number != '-':
                summary += int(next_number)
            next_number = ''
    return summary


if __name__ == '__main__':
    print(parse_string_to_sum())
