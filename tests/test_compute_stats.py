from unittest import TestCase
import numpy as np

from compute_stats import calculate_harmonic_mean, calculate_standard_deviation, calculate_variance


class TestComputeStats(TestCase):

    def setUp(self) -> None:
        self.filename = "tentative_numbers.txt"

    def test_can_calculate_harmonic_mean(self) -> None:
        self.assertEqual(np.round(calculate_harmonic_mean(self.filename), 2), 2.05)

    def test_can_calculate_standard_deviation(self) -> None:
        self.assertEqual(np.round(calculate_standard_deviation(self.filename), 2), 2.87)

    def test_can_calculate_variance(self) -> None:
        self.assertEqual(np.round(calculate_variance(self.filename), 2), 8.24)

