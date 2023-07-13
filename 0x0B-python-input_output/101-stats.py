#!/usr/bin/python3
"""
module to parse log
"""
import sys


def parse_log(size, codes):
    """
    Print accumulated metrics

    Args:
        size (int):
        codes (dict):
    """
    print("File size: {:d}".format(size))
    for key in sorted(codes):
        if codes[key] == 0:
            continue
        print("{}: {}".format(key, codes[key]))


if __name__ == "__main__":
    count = 1
    total_file_size = 0
    status_codes = {'200': 0, '301': 0,
                    '400': 0, '401': 0,
                    '403': 0, '404': 0,
                    '405': 0, '500': 0}

    try:
        # Read stdin line by line
        for line in sys.stdin:
            *_, code, file_size = line.split()
            total_file_size += int(file_size)
            # increment status code
            status_codes[code] += 1

            # Log metrics after 10 lines
            if count == 10:
                parse_log(total_file_size, status_codes)
                count = 1  # reset count
            else:
                count += 1  # increment count
    except KeyboardInterrupt:
        parse_log(total_file_size, status_codes)
        raise
