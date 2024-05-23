import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='first file to compare')
    parser.add_argument('second_file', type=str, help='second file to compare')
    args = parser.parse_args()
    return parser.main()


if __name__ == '__main__':
    main()
