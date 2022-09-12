#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  import argparse
from td1.trinome_solver import solver
import unittest

#  parser = argparse.ArgumentParser()
#
#  parser.add_argument("-a", help="Value of a", required=True)
#  parser.add_argument("-b", help="Value of a", required=True)
#  parser.add_argument("-c", help="Value of a", required=True)
#
#  args = parser.parse_args()
#
config1 = [1, -3, 2]
config2 = [1, -2, 1]
config3 = [1, 0, 3]
config4 = [0, 0, 3]


class TestUtils(unittest.TestCase):
    def test_solver(self):
        self.assertEqual(solver(*config1), [float(1), float(2)])
        self.assertEqual(solver(*config2), [float(1), float(1)])
        self.assertEqual(solver(*config3), [])
        self.assertRaises(ValueError, solver, *config4)


if __name__ == "__main__":
    unittest.main()
