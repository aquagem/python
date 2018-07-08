import random

lucky_num = []
final_luckynum = []

total_set = random.randint(1, 12)  # Total Number of Tickets
# total_set = 5
print("Total: {}".format(total_set))

# Generate Numbers for the total number of Tickets and add them to a list
for j in range(1, total_set + 1):  # For loop fro the total_set
    for i in range(1, 8):  # every ticket needs 7 numbers to be selected
        num = random.randint(1, 35)  # the number should be between 1 and 35
        while num in lucky_num:  # Check if the number selected is not already in the list
            num = random.randint(1, 35)
        lucky_num.append(num)
    final_luckynum.append(lucky_num)  # Add the first set of numbers into a new list.
    lucky_num = []  # reset the list

# For every set of numbeer selected - get a PowenBall Number
power_list = []

for k in range(1, total_set + 1):
    power_num = random.randint(1, 20)
    power_list.append(power_num)

# print all the number
m = 0
for l in final_luckynum:
    print("Ticket {} : {} \t {} PowerBall: {}".format(m, l, '--' * 5, power_list[m]))
    m += 1

# print("Lucky Numbers: {}".format(l for l in final_luckynum))
# print("Power Ball: {}" .format(power_list))

# print(lucky_num)
# print(final_luckynum)
# size = 7
# a = ([lucky_num[k:k+size] for k in range(0, len(lucky_num), size)])
# print(a)
