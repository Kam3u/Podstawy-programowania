###
# Sums numbers entered by user and calculates arithmetic mean
#
total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1

mean = total_sum / count if count > 0 else 0
print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmetic mean of the numbers is: {mean}")
