###
# Online store discount: 25% discount for each product purchased over two
#
count = int(input('Number of products purchased: '))
price = float(input('Product price: '))

if count <= 2:
    total = count * price
else:
    total = 2 * price + (count - 2) * price * 0.75

print(f'Amount to pay: {total:.2f}')
