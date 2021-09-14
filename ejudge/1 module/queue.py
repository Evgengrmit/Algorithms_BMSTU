import sys
import re


class Queue:
    def __init__(self, n):
        self.capacity_ = n
        self.array_ = [0 for _ in range(n)]
        self.head_ = 0
        self.tail_ = -1
        self.n_of_elements_ = 0

    def push(self, x):
        if self.n_of_elements_ + 1 > self.capacity_:
            raise Exception('overflow')
        self.tail_ = (self.tail_ + 1) % self.capacity_
        self.array_[self.tail_] = x
        self.n_of_elements_ += 1

    def pop(self):
        if self.n_of_elements_ == 0:
            raise Exception('underflow')
        popped_element = self.array_[self.head_]
        self.head_ = (self.head_ + 1) % self.capacity_
        self.n_of_elements_ -= 1
        return popped_element

    def print_queue(self):
        if self.n_of_elements_ == 0:
            return 'empty'
        else:
            if self.head_ <= self.tail_:
                return ' '.join(map(str, self.array_[self.head_:self.tail_ + 1]))
            else:
                from_head_to_end = self.array_[self.head_:]
                from_begin_to_tail = self.array_[:self.tail_ + 1]
                result = from_head_to_end + from_begin_to_tail
                return ' '.join(map(str, result))


def get_command(line_):
    if re.match(re.compile('(set_size\s\d+$)|(push\s\S+$)'), line_):
        value_ = line_[line_.find(' ') + 1:]
        line_ = line_[:line_.find(' ')]
        return [line_, value_]
    elif re.match(re.compile('pop|print'), line_):
        return [line_, None]

    raise Exception('error')


if __name__ == '__main__':
    my_queue = None
    set_cap = False

    name_of_input, name_of_output = sys.argv[1], sys.argv[2]

    with open(name_of_input, 'r') as input_file:
        with open(name_of_output, 'w') as output_file:

            for line in input_file:
                if line == '\n':
                    continue
                try:
                    if line[-1] == '\n':
                        line = line[:line.find('\n')]
                    command, mean = get_command(line)
                    if command is None:
                        raise Exception('error')
                    elif command == 'set_size':
                        if not set_cap:
                            my_queue = Queue(int(mean))
                            set_cap = True
                        else:
                            raise Exception('error')
                    elif command == 'push':
                        my_queue.push(mean)
                    elif command == 'pop':
                        print(my_queue.pop(), file=output_file)
                    elif command == 'print':
                        print(my_queue.print_queue(), file=output_file)
                    else:
                        raise Exception('error')
                except Exception as e:
                    if str(e) not in ['underflow', 'overflow', 'error']:
                        print('error', file=output_file)
                    else:
                        print(e, file=output_file)
