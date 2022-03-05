"""
递归定义:
A tree has a root label(根标签) and a list of branches(分支列表)
Each branch is itself a tree(每个分支本身就是一棵树)
A tree with zero branches is called a leaf(零分支的树称为叶子)
A tree starts at the root(一棵树从根开始)

循环定义:
Each location in a tree is called a node(树中的每个位置称为节点)
Each node has a label that can be any value(每个节点都有一个标签，可以是任何值)
One node can be the parent/child of another(一个节点可以是另一个节点的父/子)
The top node is the root node

A Tree is an object composed of other Tree objects, 
so its constructor must have a way of passing in children Tree
(A Tree是由其他Tree对象组成的对象,所以Tree的构造函数必须有传入children Tree的方式)
"""

#A tree is a recursive structure.
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
def count_leaves(t):
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
        
        print(leaf_labels)
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

def double(t):
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()     