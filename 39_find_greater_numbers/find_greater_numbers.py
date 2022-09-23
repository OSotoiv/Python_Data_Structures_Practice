def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    count = 0
    # loop from index 0 through the length of the list - 1(the last index)
    for i in range(len(nums)-1):
        # print(f"i: {nums[i]}")
        # holding val nums[i] check if any value after is greater.
        # x will loop over all index after location i
        for x in range(i+1, len(nums)):
            # print(f"x:{nums[x]}")
            if nums[i] < nums[x]:
                count += 1
    return count
