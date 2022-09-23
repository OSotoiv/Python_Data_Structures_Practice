def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    return {x: phrase.lower().count(x) for x in "aeiou" if x in phrase.lower()}
    # my test failed becasue the order of the return dict{} is different.
    # the values are the same though
    # also my version is pretty cool!
