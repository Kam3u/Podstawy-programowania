###
# Countdown timer printing the last five seconds in words
#
import time

countdown = int(input("Enter the number of seconds to count down: "))
words = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}

while countdown > 0:
    if countdown in words:
        print(words[countdown])
    else:
        print(countdown)
    countdown -= 1
    time.sleep(1)

print("Time's up!")
