def line_stepper(start, k):
    """
    完成函数 line_stepper,在数轴从start开始走k步到0的路径数
    每一步,您必须向左或向右移动
    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """
    if start == 0 and k == 0:
        return 1
    elif k == 0:
        return 0
    else:
        left = line_stepper(start-1, k-1)
        right = line_stepper(start+1, k-1)
        return left + right


