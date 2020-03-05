#!/usr/bin/env python3

import task2
import unittest


class test_get_task2(unittest.TestCase):

    def setUp(self):
        """Init"""

    def test_compare_list(self):
        l1 = [1, 2, 3]
        l2 = [1, 2]
        self.assertEqual(task2.compare_list(l1, l2), {1: 1, 2: 2, 3: None})
        l1 = [21, 22, 23]
        l2 = [21, 22, 23]
        self.assertEqual(task2.compare_list(l1, l2), {21: 21, 22: 22, 23: 23})
        l1 = [31, 32, 33]
        l2 = [31, 32, 33, 34]
        self.assertEqual(task2.compare_list(l1, l2), {31: 31, 32: 32, 33: 33})

    def tearDown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()
