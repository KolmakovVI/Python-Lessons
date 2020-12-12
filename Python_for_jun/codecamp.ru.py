# ================================урок по map, filter, reduce===========================
from functools import reduce

# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# round_list = [2 for n in range(len(my_floats))]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
# my_floats_square = list(map(lambda x: x * x, my_floats))
# map_result = list(map(round, my_floats_square, round_list))

# или намного проще:
map_result = list(map(lambda x: round(x ** 2, 2), my_floats))

filter_result = list(filter(lambda name: len(name) >= 7, my_names))

reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
