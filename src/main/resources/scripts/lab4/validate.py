def try_to_int(number):
    try:
        number_float = float(number)
        if number_float.is_integer():
            return int(number_float)
        else:
            return number_float
    except ValueError:
        return float(number)