from collections import deque


def remove_sequences(my_list=None):
    if my_list is None:
        my_list = deque()
    if not len(my_list):
        return
    if len(my_list) == 1:
        return my_list
    it1 = 0
    it2 = it1 + 1
    while it2 < len(my_list):
        if my_list[it1] == my_list[it2]:
            my_list.remove(my_list[it2])
        else:
            it1 += 1
            it2 += 1


if __name__ == '__main__':
    m = deque([4, 0, 0, 9, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 1])
    remove_sequences(m)
    print(list(m))
