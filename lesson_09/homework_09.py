import unittest
from lesson_07.homework_07 import find_substring, sum_func, avg_numb, str_reverse, longest_word

class TestFindSubstring(unittest.TestCase):
    def test_contains_value(self):
        result: int = find_substring("Hello, world!","world")
        expected: int = 7
        self.assertEqual(expected, result,msg=f"{result} is not equal to {expected}")

    def test_not_contain_value(self):
        result: int = find_substring("The quick brown fox jumps over the lazy dog", "cat")
        expected: int = -1
        self.assertEqual(expected, result, msg=f"{result} is not equal to {expected}")


class TestSumFunc(unittest.TestCase):
    def test_sum_int(self):
        result: int | float = sum_func(3, 4)
        expected: int = 7
        self.assertEqual(expected, result, msg=f"{result} is not equal to {expected}")

    def test_sum_float(self):
        result: int | float = sum_func(5.23, 3.11)
        expected: float = 8.34
        self.assertEqual(expected, result, msg=f"{result} is not equal to {expected}")

    def test_not_equal_none(self):
        result: int | float = sum_func(0, 0)
        expected = None
        self.assertNotEqual(expected, result, msg=f"{result} equals to {expected}")

    def test_almost_equal(self):
        result: int | float = sum_func(0.1, 0.2)
        expected: float = 0.3
        self.assertAlmostEqual(expected, result, places=6, msg=f"{result} is not equal to {expected}")


class TestAvgNumb(unittest.TestCase):
    def test_average_from_int(self):
        result: int | float = avg_numb([1,2,3,4,5])
        expected: int = 3
        self.assertEqual(expected, result, msg=f"{result} is not equal to {expected}")

    def test_average_from_zero(self):
        result: int | float = avg_numb([0,0,0])
        expected = None
        self.assertNotEqual(expected, result, msg=f"{result} equals to {expected}")


class TestStringReverse(unittest.TestCase):
    def test_string_contains(self):
        result: str = str_reverse("Random")
        expected: str = "mod"
        self.assertIn(expected, result, msg=f"{result} does not contain in {expected}")

    def test_string_not_contain(self):
        result: str = str_reverse("Random")
        expected: str = "Rand"
        self.assertNotIn(expected, result, msg=f"{result} contains in {expected}")


class TestLongestWord(unittest.TestCase):
    def test_word_present(self):
        result: str = longest_word(['Kateryna', 'Andrii', 'Mariya', 'Yevhen', 'Valentyn', 'Vlad'])
        expected: str = "Kateryna"
        assert result in expected, f"{result} does not contain in {expected}"

    def test_word_not_present(self):
        result: str = longest_word(['Kateryna', 'Andrii', 'Mariya', 'Yevhen', 'Valentyn', 'Vlad'])
        expected: str = "Vlad"
        assert result not in expected, f"{result} contains in {expected}"


if __name__=='__main__':
    unittest.main(verbosity=2)

