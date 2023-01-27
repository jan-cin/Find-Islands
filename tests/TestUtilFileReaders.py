import unittest
from utils.file_readers import read_ocean_file


class TestUtilFileReadersReadOcean(unittest.TestCase):

    def test_file_reading(self):
        actual_ocean = read_ocean_file("./sample_valid_inputs/islands8.txt")
        expected_ocean = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        self.assertEqual(actual_ocean, expected_ocean)

        actual_ocean = read_ocean_file("./sample_invalid_inputs/not_islands3.txt")
        expected_ocean = [['1', '1', '1'], ['0', '1'], ['0', '0', '0']]
        self.assertEqual(actual_ocean, expected_ocean)


if __name__ == '__main__':
    unittest.main()
