"""
现在我们将使用 2 个有用的事实来近似正弦三角函数。
一个是随着 x 变小,sin(x) 大约等于 x(对于这个问题,低于 0.0001)。
另一个事实是三角恒等式 sin(x) = 3sin(x/3) - 4sin³(x/3)
使用这两个事实,编写一个函数 sine,它返回一个以弧度为单位的值的正弦值。
"""


def sine(x):
    if x < 0.0001:
        return x
    return 3 * sine(x / 3) - 4 * pow(sine(x / 3), 3)


def countdown_up(n):
    """从 n 开始,同时打印从 n 到 0 以及从 n 到 2*n(含)的计数。

    >>> countdown_up(0)
    0

    >>> countdown_up(5)
    5
    4
    6
    3
    7
    2
    8
    1
    9
    0
    10
    """
    m = n
    print(n)

    def func(n, m):
        print(n)
        print(m)
        if n > 0:
            return func(n - 1, m + 1)

    if n > 0:
        func(n - 1, m + 1)


"""
def helper(i):
        if i == 0:
            print(n)
        elif i > n:
            return
        else:
            print(n-i)
            print(n+i)
        helper(i + 1)

    helper(0)
"""


def mario_number(level):
    """返回马里奥通过走一步或走两步以到达关卡末端而无需降落在食人鱼植物中的方法数量。
     假设每个level都以空格开头和结尾。

    >>> mario_number(' P P ')   # jump, jump
    1
    >>> mario_number(' P P  ')   # jump, jump, step
    1
    >>> mario_number('  P P ')  # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ')  # Mario cannot jump two plants
    0
    >>> mario_number('    ')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    lenght = len(level)

    def func(i):
        if i >= lenght:
            return 0
        elif level[i] == 'P':
            return 0
        elif i == lenght - 1:
            return 1
        return func(i + 1) + func(i + 2)

    return func(0)


"""
困难级:最简单的背包问题,没写出来
Q5: Knapsack
你是个小,你的工作是从 n 个重量和价值不同的物品中挑选。
你有一个可以支撑 c 磅的背包,你想挑选一些物品的子集,以便最大化你偷的价值

定义knapsack,它接受两个列表weights、values和一个容量 c,并返回该最大值。 
您可以假设项目 0 重 weights[0] 磅,并且价值为 values[0]; 
"""


def knapsack(weights, values, c):
    """
    >>> w = [2, 6, 3, 3]
    >>> v = [1, 5, 3, 3]
    >>> knapsack(w, v, 6)
    6
    """
    if weights == []:
        return 0
    else:
        first_weight, rest_weights = weights[0], weights[1:]
        first_value, rest_values = values[0], values[1:]
        with_first = first_value + knapsack(rest_weights, rest_values,
                                            c - first_weight)
        without_first = knapsack(rest_weights, rest_values, c)
        if first_weight <= c:
            return max(with_first, without_first)
        return without_first


"""    
Q6: Y combinator
递归阶乘函数可以写成单个表达式通过使用条件表达式。

>>> fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
>>> fact(5)
120
然而,这个实现依赖于fact,fact有一个名称,我们在fact主体中引用它。 
要编写递归函数,我们总是使用 def 或赋值语句为其命名,
以便我们可以在其自身的主体中引用该函数。 
在这个问题中,你的工作是在不给它命名的情况下递归地定义fact

实际上有一种通用的方法去实现它——使用函数 Y

def Y(f):
    return f(lambda: Y(f))

使用此函数,您可以使用如下赋值语句定义fact: fact = Y(?)


?是一个仅包含 lambda 表达式、条件表达式、函数调用以及函数 mul 和 sub 的表达式。
?不包含任何语句(特别是没有赋值或 def 语句)
也没有提及在 ? 之外定义的fact或任何其他标识符 除了mul 或 sub。
您还可以使用相等 (==) 运算符。 找到这样一个表达式来代替 ?。
"""
from operator import sub, mul


def Y(f):
    """The Y ("paradoxical") combinator."""
    return f(lambda: Y(f))


def Y_tester():
    """
    >>> tmp = Y_tester()
    >>> tmp(1)
    1
    >>> tmp(5)
    120
    >>> tmp(2)
    2
    """
    return Y(lambda x: lambda n: 1
             if n == 1 else mul(n,
                                x()(sub(n, 1))))  # Replace


"""
Q3:缺失数字
写递归函数missing_digits(接受一个正整数n)并返回一个数
该函数采用按递增顺序排序的数字n(例如,12289是有效的,但15362并98764没有)
它返回 n 中缺失数字的数量。 
缺失数字是 a 中 n 的第一个和最后一个数字之间的一个不在 n 中的数字
"""


def missing_digits(n):
    """Given a number a that is in sorted, non-decreasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """

    if n // 10 == 0:  #    n//10==n<10
        return 0
    else:
        max1, min1 = n % 10, n // 10 % 10
        if max1 > min1:
            return max1 - min1 - 1 + missing_digits(n // 10)
        else:
            return missing_digits(n // 10)
    """
    ans1:
    if n < 10:
        return 0
    last, rest = n % 10, n // 10
    return max(last - rest % 10 - 1, 0) + missing_digits(rest)
    
    """


# Q5河内塔
def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n - 1, start, abs(end - start))
        print_move(start, end)
        move_stack(n - 1, abs(end - start), end)


def repeated(f, n):
    """返回一个接受整数并计算 f 在该整数上的第 n 次调用的函数。使用递归实现

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    def fun1(x, n=n):
        if n == 0:
            return x
        if n == 1:
            return f(x)
        return fun1(f(x), n - 1)

    return fun1


"""
重要提示:除了索引len和切片之外,您不得使用任何字符串操作。
具体来说,您不能reversed以负步长调用或索引。
"""


def is_palindrome(s):
    """
    给定一个 string s,返回s是否是回文。
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


def greatest_pal(s):
    """
    给定一个字符串 s,返回 s 的最长回文子串。 
    如果有多个最大长度的回文子串,则返回最左边的一个
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()