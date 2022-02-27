def matches(a, b):
    """Return the number of values k such that A[k] == B[k].
    >>> matches([1, 2, 3, 4, 5], [3, 2, 3, 0, 5])
    3
    >>> matches("abdomens", "indolence")  4
    >>> matches("abcd", "dcba")   0
    >>> matches("abcde", "edcba")   1
    """
    return [a[x] for x in range(0, len(a)) if (a[x] == b[x])]


def triangle(n):
    """Assuming N >= 0, 
    return the list consisting of N lists:  [1], [1, 2], [1, 2, 3], ... [1, 2, ... N].
    >>> triangle(0)  []
    >>> triangle(1)  [[1]]
    >>> triangle(5)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]  """
    assert n >= 0
    if n == 0:
        return []
    return [[i for i in range(1, x + 1)] for x in range(1, n + 1)]


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.s is a list
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(2, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    for x in range(x):
        s.append(el)
