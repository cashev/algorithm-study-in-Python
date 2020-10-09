for i in range(1, 51):
    if i % 15 == 0:
        print('fizzbuzz', end=' ')
    elif i % 3 == 0:
        print('Fizz', end=' ')
    elif i % 5 == 0:
        print('buzz', end=' ')
    else:
        print(i, end=' ')
