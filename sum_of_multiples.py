def sum_of_multiples(number):

    sum = 0

    for x in range(1, number):
        if x % 3 == 0 or x % 5 == 0:
            sum = x + sum
        print(f'{x}')

    return sum


sum_of_multiples(10)
