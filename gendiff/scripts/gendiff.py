import argparse
import json


def read_file(file):
    with open(file) as f:
        data = json.load(f)
        return data


def match_data(file1, file2):
    data1, data2 = read_file(file1), read_file(file2)
    new_data = {}
    symbols = ['+', '-']
    for x, y in data1.items():
        if x in data2.keys() and data2[x] == y:
            new_data[x] = y
        elif x in data2.keys() and data2[x] != y:
            new_data[symbols[1] + ' ' + x] = y
            new_data[symbols[0] + ' ' + x] = data2[x]
        elif x not in data2.keys() and y == True:
            new_data[symbols[0] + ' ' + x] = y
        else:
            new_data[symbols[1] + ' ' + x] = y
    for x, y in data2.items():
        if x not in data1.keys() and y == True:
            new_data[symbols[0] + ' ' + x] = y
        elif x not in data1.keys() and y == False:
            new_data[symbols[1] + ' ' + x] = y

    return new_data


def generate_diff(file1, file2):
    return match_data(file1, file2)


def parse():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('filename1', metavar='first_file')
    parser.add_argument('filename2', metavar='second_file')
    parser.add_argument('-f', metavar='--format', help='set format of output')

    args = parser.parse_args()

    return args.filename1, args.filename2


def main():
    file1, file2 = parse()
    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == '__main__':
    main()
