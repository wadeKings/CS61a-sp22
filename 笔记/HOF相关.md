###  高阶函数

- **高阶函数：**操作函数的函数，满足以下两个条件中的一个

1.  函数作为参数

2.  作为返回值      //用于组合函数
3. 函数里定义函数



### 柯里化

- 柯里化：通过高阶函数(HOF)将带有多个参数的函数转换为每个带有一个参数的函数链

   例如：通过定义高阶函数 g，使得 g(x)(y) == f(x, y)

```python
# 柯里化
>>> def curried_pow(x):
        def h(y):
            return pow(x, y)
        return h
>>> curried_pow(2)(3)
8
```
```python
#柯里化
>>> def curry2(f):
        """Return a curried version of the given two-argument function."""
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g
    
#逆柯里化    
>>> def uncurry2(g):
        """Return a two-argument version of the given curried function."""
        def f(x, y):
            return g(x)(y)
        return f
```


### Lambda Expressions

- 一个lambda表达式的计算结果为一个未命名的函数(称为lambda函数)

- 语法：lambda [参数] : [return语句]   不允许赋值和控制语句。
- 简洁但是复合 lambda 表达式难以辨认
- 一般在需要简单函数作为参数或返回值的情况下才使用它们

```python
>>> s = lambda x: x * x #将s与lambda函数绑定
>>> s
<function <lambda> at 0xf3f490>
>>> s(12)
144
```




### 函数装饰器

- 以有用的方式利用高阶函数

  

 最常见的例子是trace(在查看函数什么时候递归调用时很有用)
```python
>>> def trace(fn):
        def wrapped(x):
            print('-> ', fn, '(', x, ')')
            return fn(x)
        return wrapped
>>> @trace #@+函数名=装饰器
    #影响def的执行规则
    def triple(x):
        return 3 * x
>>> triple(12)
->  <function triple at 0x102a39848> ( 12 )
36
```
函数triple被创建且名称triple绑定到用triple作为参数去调用函数trace 的返回值。 这个装饰器相当于：
```python
>>> def triple(x):
        return 3 * x
>>> triple = trace(triple) #只不过这个不能追踪递归
```


- 装饰符@ 跟在调用表达式之后：

  先对@后面的达式求值（就像上面对名称trace求值一样），然后是def语句，最后将装饰器表达式的求值结果应用到新定义的函数上，结果绑定到 def 语句声明的函数名。 





