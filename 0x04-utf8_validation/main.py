#!/usr/bin/python3
"""
Main file for testing
"""
validUTF8 = __import__('0-validate_utf8').validUTF8
# validUTF8 = __import__('0-validate_utf8_with_prints').validUTF8
data = None
# print(validUTF8(data))
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))
data = [229, 65, 127, 256]
print(validUTF8(data))
data = [197,130,1]
print(validUTF8(data))
data = [235,140,4]
print(validUTF8(data))
data = [240,162,138,147,145]
print(validUTF8(data))
