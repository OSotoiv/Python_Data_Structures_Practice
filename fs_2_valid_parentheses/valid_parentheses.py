def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # not (-1)
    if len(parens) % 2 != 0:
        # print('odd')
        return False
    parens_as_list = list(parens)
    # print(parens_as_list)
    reversed_parens_as_list = list(parens)
    reversed_parens_as_list.reverse()
    # print(reversed_parens_as_list)
    i = 0
    for x in range(len(parens)-1):
        if i >= len(parens) - 1:
            return True
        if ord(parens_as_list[i]) - ord(parens_as_list[i+1]) == -1:
            i += 2
            # print(f'{i}')
        elif ord(parens_as_list[i]) - ord(reversed_parens_as_list[i]) == -1:
            i += 1
            # print(f'{i}')
        else:
            return False
    return True
    # just looked at the solution.... :( i did too much...
