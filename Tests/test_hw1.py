import unittest
from Homework_1 import pow
from Homework_1 import fibonacci as fib
from Homework_1 import permutation as per
from Homework_1 import isPrime
from itertools import permutations


class TestHW1(unittest.TestCase):
    def testPow(self):
        self.assertEqual(pow.Pow(2, 10), 1024)
        self.assertEqual(pow.Pow(2, 100), 2 ** 100)

    def testFibonacci(self):
        self.assertEqual(fib.getFibonacci(0), 0)
        self.assertEqual(fib.getFibonacci(1), 1)
        self.assertEqual(fib.getFibonacci(2), 1)
        self.assertEqual(fib.getFibonacci(10), 55)

    def testPermutations(self):
        self.assertEqual([*per.all_permutations(4)], [*permutations([1, 2, 3, 4])])

    def testIsPrime(self):
        self.assertTrue(isPrime.isSimple(11))
        self.assertFalse(isPrime.isSimple(1024))


if __name__ == '__main__':
    unittest.main()
