def divisible_by_ten(num):
    """
    This function checks if a number is divisible by 10.
    :param num: The number to check
    :return: True if num is divisible by 10, otherwise False
    """
    return num % 10 == 0

# Example usage
print(divisible_by_ten(50))  # True
print(divisible_by_ten(33))  # False
print(divisible_by_ten(100)) # True
