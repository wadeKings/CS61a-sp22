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


tmp = Y_tester()
print(tmp(5))
