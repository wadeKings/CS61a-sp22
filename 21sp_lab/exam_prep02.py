from operator import add



def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
 
def multiadder(n):
    """Return a function that takes N arguments, one at a time, and adds them.
    >>> f = multiadder(3)
    >>> f(5)(6)(7) # 5 + 6 + 7
    18
    >>> multiadder(1)(5)
    5
    >>> multiadder(2)(5)(6) # 5 + 6
    11
    >>> multiadder(4)(5)(6)(7)(8) # 5 + 6 + 7 + 8
    26
    """
    assert n > 0
    if n==1:
        return lambda x:x
    else:
        def fun(x,n=n-1):
            def fun1(y):
                if n==1:
                    return add(x,y)
                return fun(add(x,y),n-1)
            return fun1
        return fun  

#result is 2016
#compose1(multiadder(4)(1000),multiadder(3)(10)(1000))(1)(2)(3)    
#compose函数是个组合器，好像给删掉了

"""
Q1：媒人
难度：⭐

实现match_k，它接受一个整数k并返回一个函数，该函数接受一个变量x，如果 x 中相隔 k 的所有数字都相同，则返回 True

例如，match_k(2)返回一个单参数函数，该函数接受x并检查距离 2 的数字x是否相同。

match_k(2)(1010)具有x = 1010从左到右的数字 1, 0, 1, 0的值。1 == 1并且0 == 0，所以match_k(2)(1010)结果为True。

match_k(2)(2010)具有x = 2010从左到右的数字 2, 0, 1, 0的值。2 != 1并且0 == 0，所以match_k(2)(2010)结果为False。

限制：您不能使用字符串或索引来解决此问题。

重要提示：您不必使用所有行，一个解决方案是不使用 while 循环正上方的行。
"""
def match_k(k):
    """ 
    Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def ismatch(x):
      
        while x>=10**k:
            if x%10!=x//(10**k)%10:
                return False
            x=x//10
        return True
    return ismatch



"""
Q2：自然链
难度：⭐⭐

chain_function 是一个高阶函数(返回一个函数g)它重复接受正整数并传递给g第一个数字初始化了一个自然链，
下一个输入是该链的递增(+1)，否则链就会中断，每次链中断时，链都会在最近输入的数字处重新启动

实现 chain_function 它打印出每次断链时预期数字的值以及迄今为止看到的断链次数，包括当前的断链。

假设高阶函数永远不会给定 ≤ 0 的数字。
"""
def chain_function():
    """
    >>> tester = chain_function()
    >>> x = tester(1)(2)(4)(5) # Expected 3 but got 4, so print 3. 1st chain break, so print 1 too.
    3 1
    >>> x = x(2) # 6 should've followed 5 from above, so print 6. 2nd chain break, so print 2
    6 2
    >>> x = x(8) # The chain restarted at 2 from the previous line, but we got 8. 3rd chain break.
    3 3
    >>> x = x(3)(4)(5) # Chain restarted at 8 in the previous line, but we got 3 instead. 4th break
    9 4
    >>> x = x(9) # Similar logic to the above line
    6 5
    >>> x = x(10) # Nothing is printed because 10 follows 9.
    >>> y = tester(4)(5)(8) # New chain, starting at 4, break at 6, first chain break
    6 1
    >>> y = y(2)(3)(10) # Chain expected 9 next, and 4 after 10. Break 2 and 3.
    9 2
    4 3
    """
    def g(x, y=0):
        def h(n):
            if n-x==1:
                return g(n,y)
            else:
                print(x+1,y+1)
                return g(n,y+1)
        return h
    return g       



"""
Q3：CS61 - NAY
难度：⭐⭐⭐
它接受一个combiner(combiner接受两个整数并返回一个整数)和正整数 n 并返回一个函数

返回的函数然后接受 n 个参数，一次一个，并计算combiner(...(combiner(combiner(arg1, arg2), arg3)...), arg_n)
lambda x:combiner(cocs61nay(combiner,n-1),x)
例如，第一个 doctest 具有返回函数 f = cs61nay(lambda x, y: x * y, 3)。 
现在，当 f 应用于三个参数时，如 f(2)(3)(4)，它将它们相乘，2*3*4 得到 24。

重要提示：可以编写自己的完全不使用入门代码的解决方案

提示：对于 n = 1 的情况，返回的函数不使用组合器。
"""
def cs61nay(combiner, n):
    """ Return a function that takes n arguments,
    one at a time, and combines them using combiner.

    >>> f = cs61nay(lambda x, y: x * y, 3)
    >>> f(3)(2)(4) # 2 * 3 * 4
    24
    >>> f(-1)(2)(3) # -1 * 2 * 3
    -6
    >>> f = cs61nay(lambda x, y: x - y, 4)
    >>> f(1)(2)(-2)(-1) # 1 - 2 - -2 - -1
    2
    >>> f = cs61nay(lambda x, y: x + y, 1)
    >>> f(61)
    61
    >>> f(2021)
    2021
    """
    if n==1:
        return lambda x:x
    else:    
        def fun1(x,n=n-1):
            def fun2(y,n=n):
                if n==1:
                   return combiner(x,y)   
                return fun1(combiner(x,y),n-1)
            return fun2             
        return fun1  




#断言： assert type(n) is int and n>=0
# 判断n是不是正整数

#文档测试
#如果编写的doctest运行都正确，什么也不显示
if __name__=="__main__":
    import doctest
    doctest.testmod()