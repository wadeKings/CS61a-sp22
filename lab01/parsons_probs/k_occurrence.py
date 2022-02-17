def k_occurrence(k, num):
    """
    >>> k_occurrence(5, 10)  # .Case 1
    0
    >>> k_occurrence(5, 5115)  # .Case 2
    2
    >>> k_occurrence(0, 100)  # .Case 3
    2
    >>> k_occurrence(0, 0)  # .Case 4
    0
    """
    numbuer = 0
    while num > 10:
        if num % 10 == k:
            numbuer += 1
        num = num // 10
    if num == k:
        return numbuer + 1
    return numbuer
