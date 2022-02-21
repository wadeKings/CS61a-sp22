from one import is_prime

"""
Q1: 
For example, the number 123444345 has four increasing runs: 
1234, 4, 4 and 345. Each run can be indexed from the end of the number, 
starting with index 0. In the previous example, the 0th run is 345, 
the first run is 4, the second run is 4 and the third run is 1234.

Implement get_k_run_starter, which takes in integers n and k 
and returns the 0th digit of the kth increasing run within n. 
The 0th digit is the leftmost number in the run. 
You may assume that there are at least k+1 increasing runs in n.


"""
def get_k_run_starter(n, k):
    """
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    final = None
    while k>=0:
        while  n>10 and n%10>(n//10%10):
              n=n//10
        final =n%10 
        k-=1 
        n = n//10
    return final


"""
Q2: 
best_k_segmenter function takes in a positive integer k and a  function score.
a score function is a pure function which takes a single number s as input and outputs another number

best_k_segmenter returns a function that takes in a single number n as input and 
returns the best k-segment of n, 
where a k-segment is a set of consecutive digits obtained by segmenting n into pieces of size k 
and the best segment is the segment with the highest score as determined by score. 
The segmentation is right to left.

For example, consider 1234567. Its 2-segments are 1, 23, 45 and 67 
(a segment may be shorter than k if k does not divide the length of the number; 
in this case, 1 is the leftover, since the segmenation is right to left).
Given the score function lambda x: -x, the best 2-segment is 1. With lambda x: x, the best segment is 67.
"""

def best_k_segmenter(k, score):
    """
    >>> largest_digit_getter = best_k_segmenter(1, lambda x: x)
    >>> largest_digit_getter(12345)
    5
    >>> largest_digit_getter(245351)
    5
    >>> largest_pair_getter = best_k_segmenter(2, lambda x: x)
    >>> largest_pair_getter(12345)
    45
    >>> largest_pair_getter(245351)
    53
    >>> best_k_segmenter(1, lambda x: -x)(12345)
    1
    >>> best_k_segmenter(3, lambda x: (x // 10) % 10)(192837465)
    192
    """
    partitioner = lambda x: (x//(10**k) , x%(10**k))
    def best_getter(n):
        assert n > 0
        best_seg = None
        while n/(10**k)>=0.1:
            n,seg = partitioner(n)
            if  best_seg==None or score(seg)>score(best_seg):
                best_seg = seg
        return best_seg
    return best_getter



"""
Q3: 
div_by_primes_under takes in an integer n and returns an checker(n-divisibility). 
checker is a function that takes in an integer k and 
returns whether k is divisible by any integers(2<= i<=n) or it returns whether k is divisible by any primes less than or equal to n.

is_prime() may is uesd

Hint:
checker = (lambda f, i: lambda x: __________)(checker, i)
"""
def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    """
    #lambda版
    checker = lambda x: False
    i = n
    while i<=n:
        if not checker(i):
            checker =(is_prime(k) and n>=k ) or /
                     (k!=1 and  not is_prime(k) and n>=(k**0.5)
        i = i+1
    return checker

    """
    #题目的本质是包含的判断
    # 如果k是素数，那么n>=k，才能返回true
    # 如果k不是素数且k!=1，那么k一定能被2到 k**0.5之间的数整数
    def checker(x):
        return False
    i = n
    while i<=n:
        if not checker(i):
            def outer(k):
                def inner(k=k):
                    return is_prime(k)
                return (inner(k) and n>=k)or ( k != 1 and   not inner(k) and n>=(k**0.5))
            checker = outer
        i = i+1
    return checker



"""
Q4: My Last Three Brain Cells
k-memory 函数接受单个输入，打印该输入是否恰好在 k 个函数调用之前看到，并返回一个新的 k-memory 函数。 
例如，一个 2-memory 函数将显示“Found”，如果它的输入恰好在两次函数调用之前被看到，否则将显示“Not found”。

实现three_memory。假设值 None 永远不会作为您的函数的输入，
并且在最开始的两个函数调用中，对于给定的任何有效输入，该函数将显示“未找到”。
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
            if x==None or y==None  or  i!=x:
                print("Not found")
            else:
                print("found")
            return f(y,z,i)
        return g
    return f(None, None, n)

  