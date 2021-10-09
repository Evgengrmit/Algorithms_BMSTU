from collections import deque


def remove_min_max(st = deque()):
    temp = deque()
    el = st.pop()
    min = el
    max = el
    temp.append(el)
    while len(st):
        e = st.pop()
        if e < min:
            min = e
        elif e > max:
            max = e
        temp.append(e)
    while len(temp):
        e = temp.pop()
        if not e == min and not e == max:
            st.append(e)
    return st


if __name__ == '__main__':
    stack = deque()

    stack.append(5)
    stack.append(4)
    stack.append(1)
    stack.append(2)
    stack.append(0)
    stack.append(3)

    print(stack)
    print(remove_min_max(stack))