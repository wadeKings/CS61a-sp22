def tree(root, subtrees=[]):
    return [root] + list(subtrees)

def root(t):
    return t[0]

def subtrees(t):
    return t[1:]

def is_leaf(t):
    return not subtrees(t)

"""
Q1
实现一个函数 contains,它接受一个树 t 和一个元素 e。 
如果 t 包含元素 e,contains 将返回 True,否则返回 False。
"""   
def contains(t, e):
    if e == root(t):
        return True
    elif is_leaf(t):
        return False
    else:
        for b in subtrees(t):
            if contains(b, e):
                return True
        return False
#any 函数接受一个布尔值列表，如果这些布尔值中的任何一个为 True，则返回 True：        
def contains(t, e):
    if e == root(t):
        return True
    elif is_leaf(t):
        return False
    else:
        return any([contains(b, e) for b in subtrees(t)])        

"""
Q2
实现一个函数 all_paths,它接受一个树t并返回从根到每个叶子的路径列表
"""

def all_paths(t):
    if is_leaf(t):
        return [t]
    return [ [ [root(t)] + all_paths(branch)] for branch in t]    
