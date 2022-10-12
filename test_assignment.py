import unittest
import main
from main import convert_input_file_to_list, generate_node_list, get_sum_metadata


class AssignmentTestCases(unittest.TestCase):

    def test_generate_list_of_nodes_metadata(self):
        main.child_node_values = []
        test = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
        generate_node_list(test)
        self.assertEqual(([[10, 11, 12], [99], [2], [1, 1, 2]]), main.child_node_values)

    def test_metadata_sum(self):
        main.child_node_values = [[10, 11, 12], [99], [2], [1, 1, 2]]
        self.assertEqual(138, get_sum_metadata())

    def test_conversion_input_file_to_list(self):
        test = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
        self.assertEqual([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2], convert_input_file_to_list(test))

    def test_conversion_file_minimum_length(self):
        test = '0 1 1'
        self.assertEqual([0, 1, 1], convert_input_file_to_list(test))

    def test_conversion_file_too_short(self):
        test = '1'
        self.assertRaises(SystemExit, convert_input_file_to_list, test)

    def test_conversion_file_with_letters(self):
        test = 'r h 4'
        self.assertRaises(SystemExit, convert_input_file_to_list, test)


if __name__ == '__main__':
    unittest.main()
