import sys
import re


class StackException(Exception):
    pass


class Stack:
    def __init__(self, n):
        self.capacity_ = n
        self.array_ = [0 for _ in range(n)]
        self.top_ = -1

    def push(self, x):
        if self.top_ + 1 >= self.capacity_:
            raise StackException('overflow')
        self.top_ += 1
        self.array_[self.top_] = x

    def pop(self):
        if self.top_ < 0:
            raise StackException('underflow')
        self.top_ -= 1
        return self.array_[self.top_ + 1]

    def print_stack(self):
        if self.top_ < 0:
            raise StackException('empty')
        return ' '.join(map(str, self.array_[:self.top_ + 1]))


def get_command(line_):
    if re.match(re.compile('(set_size\s\d+$)|(push\s\S+$)'), line_):
        return line_.split()
    elif re.match(re.compile('pop|print'), line_):
        return [line_, None]
    raise StackException('error')


if __name__ == '__main__':
    my_stack = None
    for line in sys.stdin:
        if line == '\n':
            continue
        try:
            line = line[:-1]
            command, mean = get_command(line)
            if command == 'set_size':
                if my_stack is None:
                    my_stack = Stack(int(mean))
                else:
                    raise StackException('error')
            elif command == 'push':
                my_stack.push(mean)
            elif command == 'pop':
                print(my_stack.pop())
            elif command == 'print':
                print(my_stack.print_stack())
            else:
                raise StackException('error')
        except StackException as se:
            print(se)
        except Exception as e:
            print('error')
