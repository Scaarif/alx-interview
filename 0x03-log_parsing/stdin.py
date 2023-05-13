#!/usr/bin/python3
""" Test/practice using sys.stdin to read input """
import sys



if __name__ == '__main__':
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        lineArr = (line.rstrip()).split()
        print(f'Processing **** {lineArr} **** where size = {int(lineArr[-1])} and statusCode: {int(lineArr[-2])} ')
    print('Done')
