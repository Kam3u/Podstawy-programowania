###
# First twenty terms of the Fibonacci sequence (Task 43 in _ControlStructures.md)
#
a = 0
b = 1
for _ in range(20):
    print(a, end=' ')
    a, b = b, a + b
print()
