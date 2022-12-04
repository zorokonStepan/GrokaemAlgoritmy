def gcd_rem_division(num1, num2):
    """поиск НОД двух чисел"""
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def gcd(a, b):
    """поиск НОД двух чисел"""
    if a == b:
        return a
    return gcd(max(a, b) - min(a, b), min(a, b))
