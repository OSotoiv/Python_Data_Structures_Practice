def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    count = phrase.count(' ')
    original_as_list = list(phrase.lower())
    # for char in original_as_list:
    #     if char == ' ':
    #         original_as_list.remove(char)
    #         print('space')
    #     else:
    #         print(char)

    for x in range(count):
        original_as_list.remove(' ')
    print(original_as_list)
    copy = original_as_list.copy()
    copy.reverse()
    return original_as_list == copy
