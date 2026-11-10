###
# Shows an amount in PLN using as few 5, 2, and 1 PLN coins as possible
#
amount = int(input('Enter the amount in PLN: '))
remaining = amount

coins_5 = remaining // 5
remaining %= 5

coins_2 = remaining // 2
remaining %= 2

coins_1 = remaining

print(f'The amount of PLN {amount} in coins:')
print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')
