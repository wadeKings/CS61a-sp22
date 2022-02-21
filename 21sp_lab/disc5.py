"""
Q1：（教程）最大乘积
编写一个函数，该函数接受一个列表并返回使用该列表的非连续元素可以形成的最大乘积。
输入列表将只包含大于或等于 1 的数字

"""


def max_product(s):
    """返回用s中非连续的元素通过相乘组成的最大数

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not s:
        return 1
    return max(max_product(s[1:]), s[0] * max_product(s[2:]))


"""
Q5:（教程）添加这么多
编写一个函数，它接收一个值 x、一个值 el 和一个列表 s，
并将与 x 一样多的 el 添加到列表的末尾。
确保使用列表变异技术修改原始列表。
"""


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
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
