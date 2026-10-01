def calculate(first_number, second_number):
    if second_number == 0:
        division = None
    else:
        division = first_number / second_number

    return (
        first_number + second_number,
        first_number - second_number,
        first_number * second_number,
        division,
    )


print(calculate(10, 2))
