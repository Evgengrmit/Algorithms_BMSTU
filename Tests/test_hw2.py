import unittest
from Homework_2 import deque


class TestHW2(unittest.TestCase):
    def testDeque(self):
        my_deque = deque.Deque()
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


if __name__ == '__main__':
    unittest.main()
