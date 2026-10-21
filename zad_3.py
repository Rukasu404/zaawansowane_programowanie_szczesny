def even_numbers(numbers):
    for a in numbers:
        if a % 2 == 0:
            print(a)

even_numbers(list(range(1, 11)))