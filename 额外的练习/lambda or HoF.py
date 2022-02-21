from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))

    return h


#只用return语句实现
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    return lambda x: lambda y: func(x, y)


def count_cond(condition):
    """
    接受一个参数condition(带有两个参数的函数)并返回一个函数(带一个参数的)
    该函数接受一个参数n并计算在[1,n]区间中有多少个数使condition(x)为真(x是该区间上的一个数)
    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def contident(n):
        i = 0
        number = 0
        while i < n:
            i += 1
            if condition(n, i):
                number += 1
        return number

    return contident


def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))


def composite_identity(f, g):
    """
    返回一个带有一个参数 x 的函数, 如果 f(g(x)) 等于 g(f(x)),则返回 True。 
    您可以假设 g(x) 的结果是 f 的有效输入,反之亦然
    以copose1为例子

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    def identity(x):
        return compose1(f, g)(x) == compose1(g, f)(x)

    return identity
    """
    other ans:
    return lambda x: f(g(x)) == g(f(x))
    """


def cycle(f1, f2, f3):
    """
    接受三个函数f1, f2, f3, 作为参数并返回另一个函数,该函数接受一个整数n并返回另一个函数f
    f接受一个参数 x 并循环的用x调用f1、f2 和 f3 ,这取决于 n 是什么
    下面是对于 n 的几个值.,函数f应该对 x 执行的操作

    n = 0, 返回 x
    n = 1,返回f1(x)
    n = 2,返回f2(f1(x))
    n = 3,返回f3(f2(f1(x)))
    n = 4,返回f1(f3(f2(f1(x))))

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def returna(n):
        def lastfunction(x):
            if n == 0:
                return x
            else:
                num = 0
                total = x
                while num < n:
                    num += 1
                    if num % 3 == 1:
                        total = f1(total)
                    elif num % 3 == 2:
                        total = f2(total)
                    elif num % 3 == 0:
                        total = f3(total)
            return total

        return lastfunction

    return returna
    """
    other ans:
    def ret_fn(n):
        def ret(x):
            if n == 0:
                return x
            return cycle(f2, f3, f1)(n - 1)(f1(x))
        return ret
    return ret_fn
    """


"""
Q4: My Last Three Brain Cells
k-memory 函数接受单个输入,打印该输入是否恰好在 k 个函数调用之前看到,并返回一个新的 k-memory 函数。 
例如,一个 2-memory 函数将显示“Found”,如果它的输入恰好在两次函数调用之前被看到,否则将显示“Not found”。

实现three_memory。假设值 None 永远不会作为您的函数的输入
并且在最开始的两个函数调用中,对于给定的任何有效输入,该函数将显示“未找到”。
"""


def three_memory(n):
    """
    >>> f = three_memory('first')
    >>> f = f('first')
    Not found
    >>> f = f('second')
    Not found
    >>> f = f('third')
    Not found
    >>> f = f('second') # 'second' was not input three calls ago
    Not found
    >>> f = f('second') # 'second' was input three calls ago
    Found
    >>> f = f('third') # 'third' was input three calls ago
    Found
    >>> f = f('third') # 'third' was not input three calls ago
    Not found
    """
    def f(x, y, z):
        def g(i):
            if x == None or y == None or i != x:
                print("Not found")
            else:
                print("found")
            return f(y, z, i)

        return g

    return f(None, None, n)
