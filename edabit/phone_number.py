def create_phone_number(numbers: list) -> str:
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*numbers)
