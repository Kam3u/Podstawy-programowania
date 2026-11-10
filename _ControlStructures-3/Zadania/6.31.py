###
# Prints 20 integer random numbers in the range of 5 to 10 (Task 46 in _ControlStructures.md)
#
import random

for _ in range(20):
    print(random.randint(5, 10), end=' ')
print()
