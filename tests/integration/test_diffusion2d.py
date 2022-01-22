"""
Tests for functionality checks in class SolveDiffusion2D
"""

from pytest import approx
from numpy.testing import assert_allclose

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    expected_dt = 0.0532539717274279

    solver = SolveDiffusion2D()
    solver.initialize_domain(w=13.0, h=7.0, dx=1.3, dy=1.2)
    solver.initialize_physical_parameters(d=7.3, T_cold=321.0, T_hot=720.0)

    assert solver.dt == approx(expected_dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    expected_u = [
        [321.0, 321.0, 321.0, 321.0, 321.0],
        [321.0, 321.0, 321.0, 321.0, 321.0],
        [321.0, 321.0, 321.0, 321.0, 321.0],
        [321.0, 321.0, 321.0, 720.0, 720.0],
        [321.0, 321.0, 321.0, 720.0, 720.0],
        [321.0, 321.0, 321.0, 321.0, 720.0],
        [321.0, 321.0, 321.0, 321.0, 321.0],
        [321.0, 321.0, 321.0, 321.0, 321.0],
        [321.0, 321.0, 321.0, 321.0, 321.0],
        [321.0, 321.0, 321.0, 321.0, 321.0],
    ]

    solver = SolveDiffusion2D()

    solver.initialize_domain(w=13.0, h=7.0, dx=1.3, dy=1.2)
    solver.initialize_physical_parameters(d=7.3, T_cold=321.0, T_hot=720.0)
    actual_u = solver.set_initial_condition()

    assert_allclose(actual_u, expected_u)
