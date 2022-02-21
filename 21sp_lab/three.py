#递归与树递归
#hw2
"""
Q1:数字八
编写一个递归函数num_eights，
它接受一个正整数x并返回数字 8 在 中出现的次数x。 
如果您使用任何赋值语句，测试将失败。
"""

def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    if pos==0:
        return 0
    elif pos%10==8:
        return 1+num_eights(pos//10)
    else:
        return num_eights(pos//10)



"""
Q2:乒乓球
乒乓序列从 1 开始计数，并且总是向上计数或向下计数。
在 element k，如果k是 8 的倍数或包含数字 8 ，则方向切换
您可以使用在上一个问题中定义的函数num_eights。
如果您使用任何赋值语句，测试将失败
"""

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """

    def solve(num,bool):#线性递归
        if  num==n:
            return 1*bool
        elif num_eights(num)>0 or num%8==0 :
             return 1*bool+solve(num+1,-1*bool)
        else:
            return 1*bool+solve(num+1,bool)    
    print(solve(1,1))

    '''
    ans1:
    def helper(result, i, step):wei di gui
        if i == n:
            return result
        elif i % 8 == 0 or num_eights(i) > 0:
            return helper(result - step, i + 1, -step)
        else:
            return helper(result + step, i + 1, step)
    return helper(1, 1, 1)
    
    ans2:
    def pingpong_next(x, i, step):
        if i == n:
           return x
    return pingpong_next(x + step, i + 1, next_dir(step, i+1))

    def next_dir(step, i):
        if i % 8 == 0 or num_eights(i) > 0:
            return -step
    return step

    ans3:
    def pingpong_alt(n):
        if n <= 8:
            return n
    return direction(n) + pingpong_alt(n-1)

    def direction(n):
        if n < 8:
            return 1
        if (n-1) % 8 == 0 or num_eights(n-1) > 0:
            return -1 * direction(n-1)
    return direction(n-1)
    '''

"""
Q3:缺失数字
写递归函数missing_digits(接受一个正整数n)并返回一个数
该函数采用按递增顺序排序的数字n(例如，12289是有效的，但15362并98764没有)
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
    
    if n//10==0: #    n//10==n<10
        return 0
    else:
        max1,min1=n%10,n//10%10
        if max1>min1:
           return max1-min1-1+missing_digits(n//10)
        else:
            return missing_digits(n//10)
    """
    ans1:
    if n < 10:
        return 0
    last, rest = n % 10, n // 10
    return max(last - rest % 10 - 1, 0) + missing_digits(rest)
    
    ans2:
    def helper(n, digit):
        if n == 0:
            return 0
        last, rest = n % 10, n // 10
        if last == digit or last + 1 == digit:
            return helper(rest, last)
        return 1 + helper(n, digit - 1)
    return helper(n // 10, n % 10)
    """

"""
编写一个递归函数 count_coins，
它接受一个正整数change并返回change使用硬币进行找零的方法数
硬币值只有1，5，10，25
"""
def ascending_coin(coin):
    """Returns the next ascending coin in order.
    >>> ascending_coin(1)
    5
    >>> ascending_coin(5)
    10
    >>> ascending_coin(10)
    25
    >>> ascending_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def descending_coin(coin):
    """Returns the next descending coin in order.
    >>> descending_coin(25)
    10
    >>> descending_coin(10)
    5
    >>> descending_coin(5)
    1
    >>> descending_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    """
    ans:
    def constrained_count(change, smallest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if smallest_coin == None:
            return 0
        without_coin = constrained_count(change, ascending_coin(smallest_coin))
        with_coin = constrained_count(change - smallest_coin, smallest_coin)
        return without_coin + with_coin
    return constrained_count(change, 1)
    """
    def ways(chagne,k):
        if change<0:
           return 0
        elif change==0:
           return 1
        elif k==None:
               return 0
        without_coin= ways(change,descending_coin(k))
        with_coin=   ways(change-k,k)  
        return without_coin+with_coin
    return ways(change,25) 

         

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
    if n==1:
        print_move(start,end)
    else:
        move_stack(n-1,start,abs(end-start))
        print_move(start,end)
        move_stack(n-1,abs(end-start),end)    

#lab3


"""
1.
递归实现summation，它接受一个正整数n和一个函数term。
它适用term于从1 到n包括的每个数字n并返回总和。
"""
def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n==1:
        return term(n)
    return  term(n)+summation(n-1,term)    

"""
2.
这是帕斯卡缠结的一部分
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

帕斯卡三角形中的每个数字都定义为其上方元素与其上方左侧一个元素之和。
定义一个过程pascal(row, column)，它接受一行和一列，
并返回在帕斯卡三角形中的那个位置的元素的值。如果元素不存在，返回0
行和列是零索引的；也就是说，第一行是第 0 行而不是第 1 行，第一列是第 0 列而不是第 1 列。

"""
def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle 
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    if row==column==0:
        return 1
    elif row==0 and column!=0:
        return 0    
    else:
        return pascal(row-1,column-1)+pascal(row-1,column)    


"""
3.
在hw2，你遇到的repeated函数，该函数的参数f和n返回等同于第n个重复应用的功能f。
递归实现repeated,可以用函数compose1

"""

def repeated(f, n):
    """Returns a function that takes in an integer and computes 
    the nth application of f on that integer.Implement using recursion!

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
    def fun1(x,n=n):
        if n==0:
            return x
        if n==1:
           return f(x)    
        return fun1(f(x),n-1)
    return fun1


def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h       



#disc3
"""
Q1:递归乘法

编写一个函数，接受两个数字 m 和 n 并返回它们的乘积。假设 m 和 n 是正整数。
"""

def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)

def skip_mul(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

"""
Q2:是Prime?

函数is_prime接受一个参数n(n>1)，如果 n 是素数，则返回 True，否则返回 False。递归实现

提示:如果您需要跟踪比给定参数更多的变量，或者您需要更改输入的值，辅助函数很有用。
"""

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

"""
Q3:递归冰雹

首先，选择一个正整数 n 作为开始。 如果 n 是偶数，则除以 2。
如果 n 是奇数，则乘以 3 并加 1。重复此过程直到 n 为 1。
编写 hailstone 的递归版本，打印出序列的值并返回 次数

提示:在进行递归的信念飞跃时，请同时考虑此函数的返回值和副作用。
"""

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)

"""
Q4:合并号码

编写一个函数`merge(n1, n2) ，它以降序获取数字，并以降序返回一个包含两个数字的所有数字的数字。
任何与 0 合并的数字都将是该数字（将 0 视为没有数字）。 使用递归。

提示:如果你能找出两个数字中哪个数字最小，那么我们知道结果数字将具有最小数字，
然后将两个数字合并并删除最小数字。
"""

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

"""
Q6:数楼梯
您要上一段有台阶的楼梯n(n是正整数)。您可以每次走 1 步或 2 步
编写一个函数count_stair_ways统计上有n个台阶的楼梯的方法数(每次上楼都不一样)

"""
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"

"""
Q7:计数 K
count_stair_ways问题的一个特殊版本
我们可以一次走k个台阶(k>0)
编写一个函数count_k来计算此场景的路径数
"""
def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs 
    when taking up to and including k steps at a time. 
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"    