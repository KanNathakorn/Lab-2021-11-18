def summ():

    while True:
        try:
            num_1 = float(input('Enter a number: '))
            num_2 = float(input('Enter another number: '))
            print('The sum is', num_1 + num_2)
        except:
            print('ERROR: Invalid input')


summ()
