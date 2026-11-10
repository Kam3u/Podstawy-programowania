###
# Prints a lottery coupon (numbers from 1 to 49) in 7x7 format (Task 45 in _ControlStructures.md)
#
for row in range(1, 8):
    for col in range(7):
        print(row + col * 7, end=' ')
    print()
