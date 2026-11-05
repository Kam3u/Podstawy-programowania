###
# A program that enables a user to challenge a computer.
#
import random
# COMPUTER TURN
computer = random.randint(1, 6)
# YOUR TURN
you = int(input('Guess the dice number (1-6): '))
won = (you == computer)
print(f'Computer rolled: {computer}')
print(f'You won: {won}')
