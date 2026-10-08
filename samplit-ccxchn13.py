import sys
import random

input_filename = sys.argv[1]

with open(input_filename, "r") as input_file:
    for line in input_file:
        if random.random() < 0.01:
            print(line, end="")
