def large_power(base, exponent):
    """
    This function checks if base raised to the exponent is greater than 5000.
    :param base: The base number
    :param exponent: The exponent
    :return: True if base ** exponent > 5000, otherwise False
    """
    result = base ** exponent
    return result > 5000

# Example usage
print(large_power(10, 3))  # True (10^3 = 1000, which is not greater than 5000)
print(large_power(5, 5))   # True (5^5 = 3125, which is not greater than 5000)
print(large_power(20, 3))  # True (20^3 = 8000, which is greater than 5000)
