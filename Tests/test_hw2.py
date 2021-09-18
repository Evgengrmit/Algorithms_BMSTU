import unittest
from collections import deque
from Homework_2 import deque as d
from Homework_2 import remove_sequences as rs

class TestHW2(unittest.TestCase):
    def testDeque(self):
        my_deque = d.Deque()
        my_deque.push_back(1)
        self.assertEqual(my_deque.pop_front(), 1)
        my_deque.push_front(1)
        my_deque.push_back(3)
        my_deque.push_front(2)
        my_deque.push_front(4)
        self.assertEqual(my_deque.pop_front(), 4)
        self.assertEqual(my_deque.pop_back(), 3)
        self.assertEqual(my_deque.pop_front(), 2)
        self.assertEqual(my_deque.pop_front(),1)
        with self.assertRaises(IndexError):
            my_deque.pop_back()

    def testRemove(self):
        m = deque([4, 0, 0, 9, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 1])
        rs.remove_sequences(m)
        self.assertEqual(m, deque([4, 0, 9, 1, 2, 3, 1]))


if __name__ == '__main__':
    unittest.main()
