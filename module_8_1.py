def add_everything_up(a, b):
    try:
        result = a + b
    except (TypeError):
            if isinstance(a, str) and isinstance(b, (int, float)):
                return str(a) + str(b)
            elif isinstance(a, (int, float)) and isinstance(b, str):
                return str(a) + str(b)
            else:
                return result
    return result


print(add_everything_up(3, 5))
print(add_everything_up(111, 'строка'))
print(add_everything_up('яблоко', 'персик'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
