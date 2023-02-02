numbers = [2, 4, 9, 24, 66, 98, 110, 56, 237, 99, 102]

def even_numbers(numbers):
    for n in numbers:
        if n == 237:
            break
        if n % 2 == 0:
            print(n)
even_numbers(numbers)