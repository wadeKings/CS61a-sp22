HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(n)
    return term(n) + summation(n - 1, term)


"""
提示:如果我们碰到顶部或最右边的边缘会发生什么
昆虫只能向右或向上移动
考虑一个M * N网格中的昆虫。昆虫从左下角(1, 1)开始,并希望在右上角(M, N)结束
求路径数
"""


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1:
        return 1
    if n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)


"""
帕斯卡三角

这是帕斯卡三角的一部分

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
帕斯卡三角形中的每个数字都定义为它上面的项目和它上面和左边的项目的总和。行和列是零索引的;
也就是说,第一行是第 0 行而不是 1,第一列是第 0 列而不是第 1 列。例如,帕斯卡三角形中第 2 行第 1 列的项是 2。

现在,定义一个函数pascal(row, column),它接受一行和一列,并在帕斯卡三角形中的那个位置找到项目的值。请注意,帕斯卡三角形仅在某些区域定义；0如果项目不存在则使用。出于本问题的目的，您还可以假设row >= 0和column >= 0。
"""


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    if row == column == 0:
        return 1
    elif row == 0 and column != 0:
        return 0
    else:
        return pascal(row - 1, column - 1) + pascal(row - 1, column)


if __name__ == "__main__":
    import doctest
    doctest.testmod()