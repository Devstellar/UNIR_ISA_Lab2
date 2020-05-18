# -*- coding: utf-8 -*-

import unittest
from parameterized import parameterized

from calculadora_lib import suma

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

if __name__ == "__main__":
  unittest.main()
