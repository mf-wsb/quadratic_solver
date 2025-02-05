# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:28:36 2025

@author: Michal
"""

import pytest
from solver import solve_quadratic

@pytest.mark.parametrize("a, b, c, expected", [
    (1, -3, 2, (1.0, 2.0)),  # Dwa pierwiastki rzeczywiste
    (1, -2, 1, (1.0,)),      # Jeden pierwiastek rzeczywisty (delta = 0)
    (1, 0, 1, ()),           # Brak pierwiastków rzeczywistych (delta < 0)
])
def test_solve_quadratic(a, b, c, expected):
    assert solve_quadratic(a, b, c) == expected

def test_solve_quadratic_raises_error():
    with pytest.raises(ValueError):
        solve_quadratic(0, 2, 3)  # Współczynnik 'a' nie może być zerowy