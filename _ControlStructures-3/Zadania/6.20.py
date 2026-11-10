###
# Converts a decimal number into a binary number
#
decimal = int(input('Enter decimal number: '))
n = decimal
binary = ''

if n == 0:
    binary = '0'
else:
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

print(f'{decimal}(10) = {binary}(2)')
