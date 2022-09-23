def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_as_list = list(phrase)
    new_list = []
    for char in phrase_as_list:
        if char == to_swap.upper():
            new_list.append(char.lower())
        elif char == to_swap.lower():
            new_list.append(char.upper())
        else:
            new_list.append(char)
    return "".join(new_list)
