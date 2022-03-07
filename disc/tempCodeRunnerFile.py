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