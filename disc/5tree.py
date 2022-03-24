

class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
         return self.x

    def __str__(self):
         return self.x * 2

class B:
    def __init__(self):
         print('boo!')
         self.a = []

    def add_a(self, a):
         self.a.append(a)

    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret
# >>>A('one') 
#one

# >>>print(A('one')) 
# oneone

# >>>repr(A('two')) 
#'two'

# >>>b = B() 
# boo!

# >>>b.add_a(A('a'))
# >>>b.add_a(A('b'))
# >>>b
# 2 aabb


class Tree:
    def __init__(self, label, branches=[]):
        """
        label	The root label of the tree
        branches	A list of branches (subtrees) of the tree
        (分支树的分支(子树)列表)
        """
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

def count_leaves(t):
    """Returns the number of leaf nodes in T."""
    if t.is_leaf():
        return 1
    else:
        leaves_under = 0
        for b in t.branches:
            leaves_under += count_leaves(b)
        return leaves_under


#另一种基于sum的巧妙方法
def count_leaves1(t):
    """Returns the number of leaf nodes in T."""
    if t.is_leaf():
        return 1
    else:
        branch_counts = [count_leaves(b) for b in t.branches]
        return sum(branch_counts)

def leaves(t):
    """Return a list containing the leaf labels of T.
    >>> t = Tree(20, [Tree(12, [Tree(9, [Tree(7), Tree(2)]), Tree(3)]), Tree(8, [Tree(4), Tree(4)])])
    >>> leaves(t)
    [7, 2, 3, 4, 4]
    """
    if t.is_leaf():
        return [t.label]
    else:
        leaf_labels = [leaves(b) for b in t.branches]
        return sum(leaf_labels, [])  

def count_paths(t, total):
    """返回从根到 t 中任何节点的路径数,前提是从根到该节点所经过的节点的值为 total

    >>> t = Tree(3, [Tree(-1), Tree(1, [Tree(2, [Tree(1)]), Tree(3)]), Tree(1, [Tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if t.label == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - t.label) for b in t.branches])       


def double(t):
    """Returns a tree identical to T, but with all labels doubled."""
    if t.is_leaf():
        return Tree(t.label * 2)
    else:
        return Tree(t.label * 2,
            [double(b) for b in t.branches])

def double1(t):
    """ 改变树t而不是生成一颗新树"""
    """Doubles every label in T, mutating T.
    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> double(t)
    >>> t
    Tree(2, [Tree(6, [Tree(10)]), Tree(14)])
    """
    t.label = t.label * 2
    for b in t.branches:
        double(b)            

#从树中删除子树称为修剪。在递归处理之前总是修剪分支
def prune(t, n):
    """Prune all sub-trees whose label is n.
    >>> t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    >>> prune(t, 1)
    >>> t
    Tree(3, [Tree(2)])
    """
    t.branches = [b for b in t.branches if b.label !=n]
    for b in t.branches:
        prune(b, n)


#树的高度是从根到叶子的最长路径的长度
def height(t):
    """Return the height of a tree.

    >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    >>> height(t)
    2
    >>> t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
    >>> height(t)
    3
    """
    if not t.branches:
         return 0
    list1 = [height(x) for x in t.branches]
    return 1 + max(list1)     




#路径是从树的根到任何叶子
def max_path_sum(t):
    """返回树的最大路径和.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    if not t.branches:
         return t.label
    return max([ (t.label+max_path_sum(x))  for x in t.branches ])     


def find_path(t, x):
    """
    >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    
    if  t.label == x :
        return [t.label]
    for tree in t.branches:
        path = find_path(tree,x)
        if path :
            return  [t.label] +path  


def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest label.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    while len(t.branches) > n:
        largest = max(t.branches, key=lambda x: x.label)
        t.branches.remove(largest)
    for b in t.branches:
        prune_small(b, n)