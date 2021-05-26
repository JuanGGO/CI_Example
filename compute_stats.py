from math import sqrt


def read_file(filename: str, make_int: bool):
    """
    Given a filename returns each row of the file as an entry in a list
    :param filename: File to read contents from
    :param make_int: If entries in the file should be treated as int
    :return: List with each row in the file as an element
    """
    output = []
    with open(filename, 'r') as file:
        for inpt in file:
            if make_int:
                output.append(int(inpt))
            else:
                output.append(inpt)
    return output


def calculate_average(filename: str):
    """
    Given a file with integers, calculates the average of it
    :param filename: Filename to read numbers from
    :return: Average of the read numbers in the file
    """
    numbers = read_file(filename, True)
    return sum(numbers)/len(numbers)


def calculate_harmonic_mean(filename: str):
    data = read_file(filename, True)
    n = len(data)
    return n/sum(map(lambda x: 1/x, data))


def calculate_standard_deviation(filename: str):
    data = read_file(filename, True)
    n = len(data)
    mean = calculate_average(filename)
    return sqrt(sum(map(lambda x: (x - mean)**2, data))/n)


def calculate_variance(filename: str):
    return calculate_standard_deviation(filename)**2


if __name__ == '__main__':
    fname = 'randm_nums.txt'
    print(read_file(fname, True))
    print(calculate_average(fname))
    print(calculate_harmonic_mean(fname))
    print(calculate_standard_deviation(fname))