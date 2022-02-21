def even_weighted(s):
    """
    接受一个列表 s 并返回一个新列表
    该列表仅保留 s 的偶数索引元素并将它们乘以它们的相应索引。
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [x * s[x] for x in range(len(s)) if x % 2 == 0]


def max_product(s):
    """返回用s中非连续的元素通过相乘组成的最大数
    输入列表将仅包含大于或等于 1 的数字

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