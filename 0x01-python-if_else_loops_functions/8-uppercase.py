#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        ascii_value = ord(c)
        if 97 <= ascii_value <= 122:
            result += chr(ascii_value - 32)
        else:
            result += c
    print("{}".format(result))
