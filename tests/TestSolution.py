import unittest
from solution import Ocean
from utils.file_readers import read_ocean_file


class TestSolution(unittest.TestCase):

    def test_ocean_constructor(self):
        # test validator for setting ocean parameter
        # valid oceans - it should raise any exceptions
        try:
            _ = Ocean([['1', '0']])
            _ = Ocean([['1', '0'], ['0', '1']])
            _ = Ocean([['1', '0', '1'], ['0', '0', '0']])
        except Exception:
            self.fail("Failed ocean constructor for valid inputs")

        # invalid oceans
        # rows don't have equal length
        self.assertRaises(ValueError, lambda: Ocean([['1', '0', '1'], ['1']]))
        self.assertRaises(ValueError, lambda: Ocean([['1', '0', '1'], ['1']]))
        # invalid character
        self.assertRaises(ValueError, lambda: Ocean(['a', '1', '0']))
        self.assertRaises(ValueError, lambda: Ocean([['-1', '1', '0']]))
        # not 2d list
        self.assertRaises(ValueError, lambda: Ocean([['1', '0'], ['1', '0'], ['1', ['0']]]))
        self.assertRaises(ValueError, lambda: Ocean([[['1', '0'], ['0', '1']]]))

        # test if other properties are properly set
        expected_ocean = [['1', '0', '1'], ['0', '0', '0'], ['1', '1', '1']]
        o = Ocean(expected_ocean)
        self.assertEqual(o.ocean, expected_ocean)
        self.assertEqual(o.rows, 3)
        self.assertEqual(o.cols, 3)
        self.assertEqual(o.island_count, 0)

    def test_ocean_explore_island(self):
        not_explored_ocean = [['1', '0', '1'], ['0', '0', '0'], ['1', '1', '1']]
        o = Ocean(not_explored_ocean)

        self.assertEqual(o.ocean,
                         [['1', '0', '1'],
                          ['0', '0', '0'],
                          ['1', '1', '1']])

        o.explore_island(2, 2)
        self.assertEqual(o.ocean,
                         [['1', '0', '1'],
                          ['0', '0', '0'],
                          ['X', 'X', 'X']])

        o.explore_island(0, 0)
        self.assertEqual(o.ocean,
                         [['X', '0', '1'],
                          ['0', '0', '0'],
                          ['X', 'X', 'X']])

        o.explore_island(0, 2)
        self.assertEqual(o.ocean,
                         [['X', '0', 'X'],
                          ['0', '0', '0'],
                          ['X', 'X', 'X']])

    def test_ocean_count_islands(self):
        # this is more integration test, as it is full pass of program and uses read_ocean_file
        testing_dict = {"islands1.txt": 4,
                        "islands2.txt": 1,
                        "islands3.txt": 4,
                        "islands4.txt": 1,
                        "islands5.txt": 1,
                        "islands6.txt": 8,
                        "islands7.txt": 0,
                        "islands8.txt": 0,
                        "islands9.txt": 1,
                        "islands10.txt": 1,
                        "islands11.txt": 0}

        for k, v in testing_dict.items():
            ocean_map = read_ocean_file("./sample_valid_inputs/{0}".format(k))
            o = Ocean(ocean_map)
            o.count_islands()
            self.assertEqual(o.island_count, v)


if __name__ == '__main__':
    unittest.main()
