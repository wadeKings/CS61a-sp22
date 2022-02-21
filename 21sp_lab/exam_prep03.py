"""
重要提示：除了索引len和切片之外，您不得使用任何字符串操作。
具体来说，您不能reversed以负步长调用或索引。
"""


"""
Q1：

给定一个 string s，is_palindrome返回s是否是回文。
"""

def is_palindrome(s):
    """
    >>> is_palindrome("tenet")
    True
    >>> is_palindrome("tenets")
    False
    >>> is_palindrome("raincar")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    >>> is_palindrome("ab")
    False
    """
    if len([1 for x in range(0, len(s))
            if s[x] == s[len(s) - x - 1]]) == len(s):
        return True
    return False


"""
Q2：

给定一个字符串 s，greatest_pal 应该返回 s 的最长回文子串。 
如果有多个最大长度的回文子串，则返回最左边的一个
"""

def greatest_pal(s):
    """
    >>> greatest_pal("tenet")
    'tenet'
    >>> greatest_pal("tenets")
    'tenet'
    >>> greatest_pal("stennet")
    'tennet'
    >>> greatest_pal("25 racecars")
    'racecar'
    >>> greatest_pal("abc")
    'a'
    >>> greatest_pal("")
    ''
    """
    if is_palindrome(s):
        return s
    left, right = 0, len(s)
    if len(greatest_pal(s[1:])) > len(greatest_pal(s[:len(s) - 1])):
        return greatest_pal(s[1:])
    return greatest_pal(s[:len(s) - 1])

"""
Q3：

不使用is_palindrome版本的问题.
提示：当a==b时，max(a, b)=a 
"""


def greatest_pal_two(s):
    """
    >>> greatest_pal_two("tenet")
    'tenet'
    >>> greatest_pal_two("tenets")
    'tenet'
    >>> greatest_pal_two("stennet")
    'tennet'
    >>> greatest_pal_two("abc")
    'a'
    >>> greatest_pal_two("")
    ''
    """ 
    for x in range(0,len(s)):
        if len([1 for x in range(0, len(s))
            if s[x] == s[len(s) - x - 1]]) != len(s):
            return (greatest_pal_two(s[:-1])if len(greatest_pal_two(s[:-1]))==len(greatest_pal_two(s[1:]))
            else max(greatest_pal_two(s[:-1]),greatest_pal_two(s[1:])))
    return s



if __name__ == "__main__":
    import doctest
    doctest.testmod()