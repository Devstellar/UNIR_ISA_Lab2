# -*- coding: utf-8 -*-

import unittest
from parameterized import parameterized

from calculadora_lib import suma, resta

class Tests_Calculadora(unittest.TestCase):
  # Arrange
  @parameterized.expand([
    [12, 27, 39],
    [9, -14, -5],
    [-32, -95, -127],
    [-27, 27, 0],
  ])
  def test_suma(self, a, b, res_correcto):
    # Act
    res_suma = suma(a, b)
    # Assert
    self.assertEqual(res_suma, res_correcto)

  # Arrange
  @parameterized.expand([
    [16, 9, 7],
    [23, 34, -11],
    [-41, -17, -24],
    [-18, -26, 8],
  ])
  def test_resta(self, a, b, res_correcto):
    # Act
    res_resta = resta(a, b)
    # Assert
    self.assertEqual(res_resta, res_correcto)

if __name__ == "__main__":
  unittest.main()
