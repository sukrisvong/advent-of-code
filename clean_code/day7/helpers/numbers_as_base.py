def to_base(number, width, base):
    result = ""
    while number > 0:
        result = str(number % base) + result
        number //= base
    return result.zfill(width)
