#!/usr/bin/python3
"""This is defines print_stats module
"""


def print_stats(size, status_codes):
    """Method to reads stdin and computes metrics.
    """
    print("File size: {}".format(size))
    for t in sorted(status_codes):
        print("{}: {}".format(t, status_codes[t]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for line in sys.stdin:
            if c == 10:
                print_stats(size, status_codes)
                c = 1
            else:
                c += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise