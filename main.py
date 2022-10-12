"""
Assignment from Advent of Code.
"""


child_node_values = []


def convert_input_file_to_list(file):
    """Convert the input file string into a list of integer."""
    try:
        converted_file = list(map(int, file.split()))
        # check if the length of the list
        if len(converted_file) <= 2:
            raise SystemExit('An error has occurred, file too short. Please check your input file')
    except ValueError:
        raise SystemExit('An error has occurred, please check your input file')

    return converted_file


def map_number_list(number):
    """Create a list with the ."""
    global child_node_values

    # read the number of children and number of metadata
    n_child, n_meta = number[:2]

    # remove header
    remaining = number[2:]

    # if node has children then iterate
    for _ in range(n_child):
        remaining = map_number_list(remaining)

    # append metadata values
    child_node_values.append(remaining[:n_meta])

    return remaining[n_meta:]


def get_sum_metadata():
    """Calculate the sum of all the metadata."""
    total_metadata = 0

    for myList in child_node_values:
        for item in myList:
            total_metadata += item

    return total_metadata


def get_number_of_nodes():
    """Return the total number of nodes in the given file."""
    return len(child_node_values)


def main():
    """Main function."""
    input_file = input('Enter a valid navigation system license file\n')

    converted_list = convert_input_file_to_list(input_file)

    map_number_list(converted_list)

    selection = input('Select:\n1) For the sum of all metadata\n2) For the number of nodes in the file\n')

    if selection == '1':
        print(get_sum_metadata())

    if selection == '2':
        print(get_number_of_nodes())


if __name__ == '__main__':
    # 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    main()
