# Randomly assigning the 15% EV diffusion level for each household

filepath = "ev_diffusion.txt"
with open(filepath) as fp:
        lines = fp.read().splitlines()

i = 1
with open(filepath, "w") as fp:
        for line in lines:
                print(str(i) + "   "+ line, file=fp)
                i = i+1

import random
list = random.sample(range(1, 123), 80)


with open(filepath, "r") as f:
        lines = f.readlines()
with open(filepath, "w") as f:
        for line in lines:
                if int(line[0:3]) in list:
                        f.write(line)

# 15% from each household
list1 = random.sample(range(1, 76), 11)
list2 = random.sample(range(1, 69), 10)
list3 = random.sample(range(1, 146), 22)
list4 = random.sample(range(1, 71), 11)
list5 = random.sample(range(1, 11), 2)
list6 = random.sample(range(1, 30), 5)
list7 = random.sample(range(1, 42), 6)
list8 = random.sample(range(1, 73), 11)
list9 = random.sample(range(1, 11), 2)
list10 = random.sample(range(1, 34), 5)
list11 = random.sample(range(1, 33), 5)
list12 = random.sample(range(1, 41), 6)
list13 = random.sample(range(1, 2), 1)
list14 = random.sample(range(1, 12), 2)
list15 = random.sample(range(1, 22), 3)
list16 = random.sample(range(1, 136), 20)

list1.sort()
list2.sort()
list3.sort()
list4.sort()
list5.sort()
list6.sort()
list7.sort()
list8.sort()
list9.sort()
list10.sort()
list11.sort()
list12.sort()
list13.sort()
list14.sort()
list15.sort()
list16.sort()

with open(filepath, "w") as f:

        f.write('household_1: ')
        for element in list1:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_2: ')
        for element in list2:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_3: ')
        for element in list3:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_4: ')
        for element in list4:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_5: ')
        for element in list5:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_6: ')
        for element in list6:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_7: ')
        for element in list7:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_8: ')
        for element in list8:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_9: ')
        for element in list9:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_10: ')
        for element in list10:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_11: ')
        for element in list11:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_12: ')
        for element in list12:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_13: ')
        for element in list13:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_14: ')
        for element in list14:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_15: ')
        for element in list15:
                f.write(str(element) + " ")
        f.write("\n")

        f.write('household_16: ')
        for element in list16:
                f.write(str(element) + " ")
        f.write("\n")
