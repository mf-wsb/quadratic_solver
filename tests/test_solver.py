# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:28:36 2025

@author: Michal
"""

import pytest
import math
from solver import solve_quadratic

@pytest.mark.parametrize("a, b, c, expected", [
    (1, -3, 2, (1.0, 2.0)),  # Dwa pierwiastki rzeczywiste (Δ > 0)
    (1, -2, 1, (1.0,)),      # Jeden pierwiastek rzeczywisty (Δ = 0)
    (1, 0, 1, ()),           # Brak pierwiastków rzeczywistych (Δ < 0)
    (2, 5, -3, (-3.0, 0.5)), # Dodatkowy przypadek z liczbami różnymi od 1
    (-1, -2, -1, (-1.0,)),   # Δ = 0 dla a < 0
    (1e-6, 1e-3, 1, ())      # Bardzo małe a, b, c
])
def test_solve_quadratic(a, b, c, expected):
    result = solve_quadratic(a, b, c)

    # Sprawdzenie liczby pierwiastków
    assert len(result) == len(expected), f"Oczekiwano {len(expected)} pierwiastków, otrzymano {len(result)}"

    # Sprawdzenie wartości pierwiastków (jeśli istnieją)
    for r, e in zip(result, expected):
        assert math.isclose(r, e, rel_tol=1e-6), f"Oczekiwano {e}, otrzymano {r}"

    # Sprawdzenie zwracanego typu (czy zawsze jest krotką)
    assert isinstance(result, tuple), "Funkcja powinna zwracać krotkę"


def test_solve_quadratic_raises_error():
    with pytest.raises(ValueError, match="Współczynnik 'a' nie może być zerowy."):
        solve_quadratic(0, 2, 3)
