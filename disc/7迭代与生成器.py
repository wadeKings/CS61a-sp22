from pydoc import Helper


s = [[1, 2, 3, 4]]
i = iter(s)
j = iter(next(i))
#print(next(j))
#1

#s.append(5)
#print(next(i))
#5
#print(next(j))
#2
#print(list(j))
#[3,4]
#print(next(i))
#StopIteration

"""
函数仅产生errable的erifure的元素为true。
"""
def filter_iter(iterable, f):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for x in iterable:
        if f(x):
            yield x


def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    while n >= 0 :
        yield n  
        if n == 1 :
            pass
        elif n % 2 == 0:
            n= n//2
        elif n % 2 != 0:
            n = n*3+1  
    #递归写法
    yield n
    if n == 1:
        yield from hailstone(n)
    elif n % 2 == 0:
        yield from hailstone(n // 2)
    else:
        yield from hailstone(n * 3 + 1)        
      
    
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1 :
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()            