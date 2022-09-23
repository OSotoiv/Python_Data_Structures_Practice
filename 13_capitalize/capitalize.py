def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # return phrase.capitalize()
    copy = list(phrase)
    copy[0] = copy[0].upper()
    return ''.join(copy)
