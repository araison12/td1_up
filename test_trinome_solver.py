#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from td1.trinome_solver import solver

#  import unittest

parser = argparse.ArgumentParser()

parser.add_argument("-a", help="Value of a", required=True, type=float)
parser.add_argument("-b", help="Value of b", required=True, type=float)
parser.add_argument("-c", help="Value of c", required=True, type=float)

args = parser.parse_args()

config = [args.a, args.b, args.c]
res = solver(*config)
print(res)

#  class TestUtils(unittest.TestCase):
#  def test_solver(self):
#  self.assertEqual(solver(*config1), [float(1), float(2)])
#  self.assertEqual(solver(*config2), [float(1), float(1)])
#  self.assertEqual(solver(*config3), [])
#  self.assertRaises(ValueError, solver, *config4)
#
#
#  if __name__ == "__main__":
#  unittest.main()
