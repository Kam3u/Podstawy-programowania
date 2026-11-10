###
# Payment card PIN verification (Task 41 in _ControlStructures.md)
#
correct_pin = '0805'
attempts = 0

while attempts < 3:
    entered_pin = input('Enter the PIN code: ')
    if entered_pin == correct_pin:
        print('PIN code is correct.')
        break
    else:
        print('Incorrect...')
        attempts += 1
else:
    print('Sorry, your payment card has been blocked.')
