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


def my_map(fn, seq):
    """将 fn 应用于 seq 中的每个元素并返回一个列表.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    return [fn(x) for x in seq]


def my_filter(pred, seq):
    """仅当满足 pred 时才将元素保留在 seq 中.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    return [x for x in seq if pred(x)]


def my_reduce(combiner, seq):
    """使用组合器组合 seq 中的元素。 seq 至少有一个元素.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    total = seq[0]
    for x in range(1, len(seq)):
        total = combiner(total, seq[x])
    return total


#q1
s1 = [1, 2, 3]
s2 = s1
print(s1 is s2)  #ans :true

#q2
s2.extend([5, 6])
print(s1[4])  #ans: 6

#q3
s1.append([-1, 0, 1])
print(s2[5])  #ans: [-1, 0, 1]

#q4
s3 = s2[:]
s3.insert(3, s2.pop(3))
print(len(s1))  #ans: 5

#q5
print(s1[4] is s3[6])  #False
#ans:True,序列的元素相当于一个指针(),指向了同个对象

#q6
print(s3[s2[4][1]])  #ans:1

#q7
print(s1[:3] is s2[:3])  #ans:False

#q8
print(s1[:3] == s2[:3])  #ans:True

#q9
s1[4].append(2)
print(s3[6][3])  #ans:2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
