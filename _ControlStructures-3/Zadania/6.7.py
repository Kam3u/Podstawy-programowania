###
# Age group checker
#
age = int(input('Enter your age: '))

if age < 13:
    print('Age group: Child')
elif age <= 19:
    print('Age group: Teen')
elif age <= 64:
    print('Age group: Adult')
else:
    print('Age group: Senior')
