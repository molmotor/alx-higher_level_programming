#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 1
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1:", sys.argv[1])
    else:
        print(len(sys.argv) - 1, "arguments:")
        for i in range (1, len(sys.argv)):
            print(i,":", sys.argv[i])
