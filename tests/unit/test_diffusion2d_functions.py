"""
Tests for functions in class SolveDiffusion2D
"""

from unittest import TestCase

from pytest import approx
from numpy import array
from numpy.testing import assert_allclose

from diffusion2d import SolveDiffusion2D


class TestDiffusion2D(TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        expected_nx = 6
        expected_ny = 2

        # nx = int(w / dx)
        # ny = int(h / dy)

        self.solver.initialize_domain(w=9.1, h=6.2, dx=1.4, dy=2.6)

        self.assertEqual(
            self.solver.nx, expected_nx, "initialize_domain produced wrong nx value"
        )
        self.assertEqual(
            self.solver.ny, expected_ny, "initialize_domain produced wrong ny value"
        )

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.w = 9.1
        self.solver.h = 6.2
        self.solver.dx = 1.3
        self.solver.dy = 2.6
        self.solver.nx = 6
        self.solver.ny = 2

        # dx2, dy2 = self.dx * self.dx, self.dy * self.dy
        # dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))

        expected_dt = approx(0.25037037037037035)

        self.solver.initialize_physical_parameters(d=2.7, T_cold=321.3, T_hot=657.4)

        self.assertEqual(self.solver.dt, expected_dt, "dt is not calculated correctly")

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.w = 9.8
        self.solver.h = 10.2
        self.solver.dx = 0.3
        self.solver.dy = 0.4
        self.solver.nx = 32
        self.solver.ny = 25
        self.solver.D = 6.7
        self.solver.T_cold = 321.3
        self.solver.T_hot = 657.4
        self.solver.dt = 0.004298507462686568

        expected_u = array(
            [
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    657.4,
                    657.4,
                    657.4,
                    657.4,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
                [
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                    321.3,
                ],
            ]
        )

        actual_u = self.solver.set_initial_condition()
        assert_allclose(actual_u, expected_u)
