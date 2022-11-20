import unittest

from NewBoxCalculator import (calculate_big_boxes, calculate_medium_boxes,
                              calculate_small_boxes)


class TestBoxCalculator(unittest.TestCase):

    def test_small(self):
        """Test that `count_small_boxes` returns the same as the number passed.
        (Small boxes can hold only one item each.) """
        test_value = 2
        expected = 2
        result = calculate_small_boxes(test_value)
        self.assertEqual(result, expected, "Each small box holds 1 item")

    def test_small_more_than_3(self):
        """Test that `count_small_boxes` returns None if given input of 3 or more"""
        test_value = 0
        result = calculate_small_boxes(test_value)
        self.assertIsNone(result,
                          "Use medium boxes for 3 or more items!")

    def test_medium(self):
        """Test that `count_medium_boxes` returns one box for every 3 items."""
        test_value = 12
        expected = 4
        result = calculate_medium_boxes(test_value)
        self.assertEqual(result, expected, "Each medium box holds 3 items")

    def test_big(self):
        """Test that `count_big_boxes` returns one box for every 5 items."""
        test_value = 15
        expected = 3
        result = calculate_big_boxes(test_value)
        self.assertEqual(result, expected, "Each big box holds 5 items")


if __name__ == "__main__":
    unittest.main()
