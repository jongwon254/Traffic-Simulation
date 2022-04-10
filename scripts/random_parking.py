# Randomly assigning 42% of households to have a charging station

filepath = "all_cs_home_edit.txt"
with open(filepath) as fp:
    lines = fp.read().splitlines()

i = 1
with open(filepath, "w") as fp:
    for line in lines:
        print(str(i) + line, file=fp)
        i = i+1

# 42% of households have a charging station
import random
list = random.sample(range(1, 809), 340)


with open(filepath, "r") as f:
    lines = f.readlines()
with open(filepath, "w") as f:
    for line in lines:
        if int(line[0:3]) in list:
            f.write(line)

