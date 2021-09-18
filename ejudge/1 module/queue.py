import sys
import re


class QueueException(Exception):
    pass


class Queue:
    def __init__(self, n):
        self.capacity_ = n
        self.array_ = [0 for _ in range(n)]
        self.head_ = 0
        self.tail_ = -1
        self.n_of_elements_ = 0

    def push(self, x):
        if self.n_of_elements_ + 1 > self.capacity_:
            raise QueueException('overflow')
        self.tail_ = (self.tail_ + 1) % self.capacity_
        self.array_[self.tail_] = x
        self.n_of_elements_ += 1

    def pop(self):
        if self.n_of_elements_ == 0:
            raise QueueException('underflow')
        popped_element = self.array_[self.head_]
        self.head_ = (self.head_ + 1) % self.capacity_
        self.n_of_elements_ -= 1
        return popped_element

    def print_queue(self):
        if self.n_of_elements_ == 0:
            raise QueueException('empty')
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
        return line_.split()
    elif re.match(re.compile('pop|print'), line_):
        return [line_, None]
    raise QueueException('error')


if __name__ == '__main__':
    my_queue = None

    with open(sys.argv[1], 'r') as input_file:
        with open(sys.argv[2], 'w') as output_file:

            for line in input_file:
                if line == '\n':
                    continue
                try:
                    if line[-1] == '\n':
                        line = line[:-1]
                    command, mean = get_command(line)

                    if command == 'set_size':
                        if my_queue is None:
                            my_queue = Queue(int(mean))
                        else:
                            raise QueueException('error')
                    elif command == 'push':
                        my_queue.push(mean)
                    elif command == 'pop':
                        print(my_queue.pop(), file=output_file)
                    elif command == 'print':
                        print(my_queue.print_queue(), file=output_file)
                    else:
                        raise QueueException('error')
                except QueueException as qe:
                    print(qe, file=output_file)
                except Exception as e:
                    print('error', file=output_file)
