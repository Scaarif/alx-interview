#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """
import sys


def readStdinAndPrint(status_dict, f_size):
    """ WWPrints information """
    print("File size: {:d}".format(f_size))
    for i in sorted(status_dict.keys()):
        if status_dict[i] != 0:
            print("{}: {:d}".format(i, status_dict[i]))


if __name__ == '__main__':
    statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                   "404": 0, "405": 0, "500": 0}

    # track the number of lines since last print and total file size
    count = 0
    totalSize = 0

    try:
        # read stdin lines, one at a time
        for line in sys.stdin:
            if count != 0 and count % 10 == 0:
                readStdinAndPrint(statusCodes, totalSize)

            # get the line's file size and status code
            lineList = line.split()
            # check that line is as long as expected (confirm-ish format)
            if len(lineList) != 9:
                continue
            count += 1

            try:
                totalSize += int(lineList[-1])
            except ValueError as e:
                pass
                # print('exception: ', e)
            try:
                if lineList[-2] in statusCodes:
                    statusCodes[lineList[-2]] += 1
            except Exception as e:
                pass
        # lines exhausted, print last batch's statistics...
        readStdinAndPrint(statusCodes, totalSize)

    except KeyboardInterrupt:
        # on cntrl + C, print statistics at that point
        readStdinAndPrint(statusCodes, totalSize)
        raise
