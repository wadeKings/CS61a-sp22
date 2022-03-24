"""
Q2:夹克天气
阿方索只有在低于 60 度或下雨的情况下才会在外面穿夹克。

编写一个函数,接收当前温度和一个布尔值来判断是否下雨。 
如果 阿方索 将穿夹克,此函数应返回 True,否则返回 False。




"""


def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False


"""
Q3:if函数与语句
现在我们已经了解了 if 语句的工作原理,
让我们看看是否可以编写一个与 if 语句行为相同的函数。
"""


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result


#上面的if_function 并不总是和if语句效果相同

def if_function1(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()


#与 with_if_statement不同，一种if_functon 与if不同的情况
def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())


def cond():
    return False


def true_func():
    print("Welcome to")


def false_func():
    print("61A")


"""
Q5:是Prime吗
编写一个函数,True如果正整数n是素数则返回,False否则返回。
"""


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


"""
Q6:嘶嘶声
实现 fizzbuzz 序列,它为从 1 到 n 的每个数字打印一条语句。对于一个数字i

如果i只能被 3 整除,那么我们打印“fizz”。
如果i只能被 5 整除,那么我们打印“buzz”。
如果i能被 3 和 5 整除,则打印“fizzbuzz”。
否则,我们打印数字i。
"""


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        i += 1
