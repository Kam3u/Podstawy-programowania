###
# Finds N leading prime numbers (Task 44 in _ControlStructures.md)
#
n = int(input('Enter N: '))
count = 0
candidate = 2

print('Prime numbers:', end=' ')
while count < n:
    is_prime = True
    for d in range(2, candidate):
        if candidate % d == 0:
            is_prime = False
            break
    if is_prime:
        print(candidate, end=' ')
        count += 1
    candidate += 1
print()
