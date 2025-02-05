# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:22:18 2025

@author: Michal
"""

import math

def solve_quadratic(a: float, b: float, c: float):
    """Oblicza pierwiastki równania kwadratowego ax^2 + bx + c = 0"""
    if a == 0:
        raise ValueError("Współczynnik 'a' nie może być zerowy.")

    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        x = -b / (2 * a)
        return x,
    else:
        return ()