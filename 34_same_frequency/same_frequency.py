def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    num_string1 = str(num1)
    num_string2 = str(num2)
    num_dict1 = {num: num_string1.count(num) for num in num_string1}
    num_dict2 = {num: num_string2.count(num) for num in num_string2}
    return num_dict1 == num_dict2
