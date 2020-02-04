def create_phone_number(n: list) -> str:
    """Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those 
    numbers in the form of a phone number. """
    number = ''
    for num in n:
        number += str(num)
    return f'({number[0:3]}) {number[3:6]}-{number[6:]}'
