import random

def minmax(numbers):
    # Minimum Value
    minval = min(numbers)
    # Maximum Value
    maxval = max(numbers)
    
    ########################################
    # Do not delete the return statement
    ########################################
    
    # Simply returns the values (Minimum and Maximum)
    return minval, maxval


def main():

    numbers = [1, 2, 3, 4, 5]
    minval, maxval = minmax(numbers)
    print('List values', *numbers)
    print(f'Max value: {maxval} \t Min value:{minval}')

    numbers = [random.randint(0, 100) for i in range(10)]
    minval, maxval = minmax(numbers)
    print('List values', *numbers)
    print(f'Max value: {maxval} \t Min value: {minval}')


if __name__ == '__main__':
    main()
