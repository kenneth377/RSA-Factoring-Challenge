#!/usr/bin/python3
import math
from sys import argv


if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            n = int(line.split('\n')[0])

            for i in range(2,int(math.sqrt(n))):
                if n%i==0:
                    print(f"{n}={int(n/i)}*{i}")
                    break


            line = file.readline()
except FileNotFoundError:
    print(f'File not found: {argv}')
except ValueError:
    print(f'Invalid input in the file: {argv}')
except Exception as e:
    print(f'An error occurred: {str(e)}')
    pass
