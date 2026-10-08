import sys
import random

csv_filename = sys.argv[1]

with open(csv_filename, "r") as file:
    for line in file:
        if random.random() < 0.01:
            print(line, end="")
