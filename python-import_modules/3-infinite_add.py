#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    total = 0

    for i in range(num_args):
        total += int(sys.argv[i + 1])

print(f"{total}")
