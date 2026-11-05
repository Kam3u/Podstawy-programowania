###
# Module 2: Types, Variables and Operators
# Section 2, Task 2: Operators, arguments and expression values
#
# a) 3 * 2 + 1          -> 2 operators (*, +), 3 arguments (3, 2, 1) -> 7
# b) 5 + 10 * 5         -> 2 operators (+, *), 3 arguments (5, 10, 5) -> 55
# c) 4 + 4 / 2 ** 2     -> 3 operators (+, /, **), 4 arguments (4, 4, 2, 2) -> 5.0
# d) 4 % 3 % 2 % 1      -> 3 operators (%, %, %), 4 arguments (4, 3, 2, 1) -> 0
# e) 1 + 2 % 3 ** 4 * 5 -> 4 operators (+, %, **, *), 5 arguments (1, 2, 3, 4, 5) -> 11
# f) True != False      -> 1 operator (!=), 2 arguments (True, False) -> True

print("a)", 3 * 2 + 1)
print("b)", 5 + 10 * 5)
print("c)", 4 + 4 / 2 ** 2)
print("d)", 4 % 3 % 2 % 1)
print("e)", 1 + 2 % 3 ** 4 * 5)
print("f)", True != False)
