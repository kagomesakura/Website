grades = int (input('What grade percentage did student receive? \n:'))
grades = int(grades)


if grades <= 100 and grades >= 90:
    print('You received an A!')
elif grades <= 89 and grades >= 80 :
    print('You received an B.')
elif grades <= 79 and grades >= 70:
    print('You received an C.')
elif grades <= 69 and grades >= 60:
    print('You received an D!')
elif grades <= 59 and grades >= 0:
    print('You have FAILED!')
