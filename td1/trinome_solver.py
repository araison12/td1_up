#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from typing import List

# Let a,b,c in R with a=/=0, what is the root of P(x)=ax^2+bx+c=0 ? Propose an algorithm that provide list of roots in case in P(x) is splitable on R only!


def solver(a: float, b: float, c: float) -> List:
    if a == 0:
        raise ValueError
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        return [(-2 * b + val * np.sqrt(delta)) / (2 * a) for val in [-1, 1]]
    elif delta == 0:
        return [-b / (2 * a) for _ in range(2)]
    else:
        return []
