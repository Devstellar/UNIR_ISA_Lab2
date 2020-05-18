# -*- coding: utf-8 -*-

import unittest
from parameterized import parameterized

from calculadora_lib import suma, resta, multiplicacion, division

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

  # Arrange
  @parameterized.expand([
    [64, 14, 896],
    [21, -52, -1092],
    [-36, -14, 504],
    [-37, 83, -3071],
  ])
  def test_multiplicacion(self, a, b, res_correcto):
    # Act
    res_multiplicacion = multiplicacion(a, b)
    # Assert
    self.assertEqual(res_multiplicacion, res_correcto)

  # Arrange
  @parameterized.expand([
    [61, 7, 8.714285714285714],
    [-31, 17, -1.8235294117647058],
    [51, -9, -5.666666666666667],
    [-27, -11, 2.4545454545454546],
  ])
  def test_division(self, a, b, res_correcto):
    # Act
    res_division = division(a, b)
    # Assert
    self.assertEqual(res_division, res_correcto)

if __name__ == "__main__":
  unittest.main()
