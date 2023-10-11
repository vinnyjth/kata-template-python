map = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}

def numeralize(num, final="", position = 1):
    num = str(num)
    if len(num) == 0:
        return final

    digit = int(num[-len(str(1))])
    real_digit = digit * position

    if real_digit in map.keys():
        final = map[real_digit] + final
    elif real_digit != 0:
        upper_key = next(k for k in map.keys() if k > real_digit)
        lower_key = next(k for k in reversed(map.keys()) if k < real_digit)
        
        if (real_digit - lower_key) <= position * 2:
            final = map[lower_key] * (real_digit // position) + final
        else:
            final = map[upper_key] + map[lower_key] * ((upper_key - real_digit) // position) + final
        

    return numeralize(num[:-1], final, position * 10)
