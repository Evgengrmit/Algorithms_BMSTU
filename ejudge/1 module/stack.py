import sys
import re


class Stack:
    def __init__(self, n):
        self.capacity_ = n
        self.array_ = [0 for _ in range(n)]
        self.top_ = -1

    def push(self, x):
        if self.top_ + 1 >= self.capacity_:
            raise Exception('overflow')
        self.top_ += 1
        self.array_[self.top_] = x

    def pop(self):
        if self.top_ < 0:
            raise Exception('underflow')
        self.top_ -= 1
        return self.array_[self.top_ + 1]

    def print_stack(self):
        if self.top_ < 0:
            return 'empty'
        return ' '.join(map(str, self.array_[:self.top_ + 1]))


def get_command(line_):
    if re.match(re.compile('(set_size\s\d+$)|(push\s\S+$)'), line_):
        value_ = line_[line_.find(' ') + 1:]
        line_ = line_[:line_.find(' ')]
        return [line_, value_]
    elif re.match(re.compile('pop|print'), line_):
        return [line_, None]
    raise Exception('error')


if __name__ == '__main__':
    my_stack = None
    set_cap = False
    for line in sys.stdin:
        if line == '\n':
            continue
        try:
            line = line[:line.find('\n')]
            command, mean = get_command(line)
            if command is None:
                raise Exception('error')
            elif command == 'set_size':
                if not set_cap:
                    my_stack = Stack(int(mean))
                    set_cap = True
                else:
                    raise Exception('error')
            elif command == 'push':
                my_stack.push(mean)
            elif command == 'pop':
                print(my_stack.pop())
            elif command == 'print':
                print(my_stack.print_stack())
            else:
                raise Exception('error')
        except Exception as e:
            if str(e) not in ['underflow', 'overflow', 'error']:
                print('error')
            else:
                print(e)
