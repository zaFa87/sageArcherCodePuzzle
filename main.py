"""
Assignment from Advent of Code.
"""

# initialise global variable
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


def generate_node_list(number):
    """Generate the list of nodes with their metadata ."""
    global child_node_values

    # read the number of children and number of metadata
    n_child, n_meta = number[:2]

    # remove header
    remaining = number[2:]

    # if node has children then iterate
    for _ in range(n_child):
        remaining = generate_node_list(remaining)

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


def main():
    """Main function."""
    input_file = input('Enter a valid navigation system license file\n'
                       'For example 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2 should return 138\n')

    converted_list = convert_input_file_to_list(input_file)

    generate_node_list(converted_list)

    print(get_sum_metadata())


if __name__ == '__main__':
    main()
