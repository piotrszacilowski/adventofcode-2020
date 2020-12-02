from itertools import combinations


def read_file_to_array(file):
    with open(file, 'r') as file:
        report = [line.strip() for line in file]
        return report


def find_the_sum_of_two_numbers(report):
    for x, y in combinations(report, 2):
        if int(x) + int(y) == 2020:
            return int(x) * int(y)


def find_the_sum_of_three_numbers(report):
    for x, y, z in combinations(report, 3):
        if int(x) + int(y) + int(z) == 2020:
            return int(x) * int(y) * int(z)


print(find_the_sum_of_two_numbers(read_file_to_array("input.txt")))
print(find_the_sum_of_three_numbers(read_file_to_array("input.txt")))
