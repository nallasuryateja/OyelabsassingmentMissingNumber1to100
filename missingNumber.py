# random_array=[it consists random numbers from 1 to 100 with one missing number]

summation = 0
for i in range(1, 101):
    summation += int(i)

random_summation = 0
for each in random_array:
    random_summation += int(each)

if summation == random_summation:
    print("No missing number")
else:
    print(summation-random_summation)
