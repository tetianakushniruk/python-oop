import random
import os
import timeit

with open('text.txt', 'a') as file:
    # divide size by 1024**2 to convert to Mb
    while os.path.getsize('text.txt') <= 50:
        file.write(str(random.randint(0, 100))+'\n')

print('File created!')


s = """
with open('text.txt', 'r') as file:
    list_of_nums = [x.strip() for x in file.readlines()]
    if all(x.isdigit() for x in list_of_nums):
        summ = sum(int(x) for x in list_of_nums)
"""
print(timeit.timeit(s, number=1000))
s = """
with open('text.txt', 'r') as file:
    list_of_nums = []
    for line in file:
        list_of_nums.append(line.strip())
    if all(x.isdigit() for x in list_of_nums):
        summ = sum(int(x) for x in list_of_nums)
"""
print(timeit.timeit(s, number=1000))
s = """
with open('text.txt', 'r') as file:
    list_of_nums = (int(x.strip()) for x in file if x.strip().isdigit())
    summ = sum(list_of_nums)
"""
print(timeit.timeit(s, number=1000))

