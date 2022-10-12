import unittest

from main import convert_input_file_to_list, map_number_list, get_sum_metadata, get_number_of_nodes


class AssignmentTestCases(unittest.TestCase):
    def test_correct_file(self):
        test = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
        self.assertEqual(([], [[10, 11, 12], [99], [2], [1, 1, 2]]), map_number_list(test))

    def test_metadata_sum(self):
        test = (0, [[10, 11, 12], [99], [2], [1, 1, 2]])
        self.assertEqual(138, get_sum_metadata(test))

    def test_number_of_nodes_in_file(self):
        test = (0, [[10, 11, 12], [99], [2], [1, 1, 2]])
        self.assertEqual(4, get_number_of_nodes(test))

    def test_conversion(self):
        test = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
        self.assertEqual([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2], convert_input_file_to_list(test))

    def test_conversion_file_minimum_length(self):
        test = '0 1 1'
        self.assertEqual([0, 1, 1], convert_input_file_to_list(test))

    def test_file_too_short(self):
        test = '1'
        self.assertRaises(SystemExit, convert_input_file_to_list, test)

    def test_file_with_letters(self):
        test = 'r h 4'
        self.assertRaises(SystemExit, convert_input_file_to_list, test)


if __name__ == '__main__':
    unittest.main()
