# tests/test_main.py

import unittest
from hanuman.main import get_category_by_wind

class TestHanuman(unittest.TestCase):
    def test_get_category_by_wind(self):
        self.assertEqual(get_category_by_wind(20), "TD")
        self.assertEqual(get_category_by_wind(50), "TS")
        self.assertEqual(get_category_by_wind(70), "C1")
        self.assertEqual(get_category_by_wind(85), "C2")
        self.assertEqual(get_category_by_wind(100), "C2")
        self.assertEqual(get_category_by_wind(120), "C4")
        self.assertEqual(get_category_by_wind(150), "C5")

if __name__ == '__main__':
    unittest.main()
