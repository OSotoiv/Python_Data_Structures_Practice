def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """
    copy = lst.copy()
    if len(copy):
        return copy.pop()
    else:
        return None
