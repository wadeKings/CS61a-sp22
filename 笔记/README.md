## 对象： python中，名称是对对象的引用

###  

### debug

- only debug

`print('DEBUG: result is', result)`

//在print语句中使用前缀"DEBUG: " 来确保该语句不会干扰到`ok`

//用于快速调试一次性错误——在找出错误后，您将删除所有`print`语句。

- 定期调试

//如果每次我们运行文件时都会弹出调试消息，这会有点烦人。避免这种情况的一种方法是使用全局`debug`变量：

```python
debug = True

def foo(n):
i = 0
while i < n:
    i += func(i)
    if debug:
        print('DEBUG: i is', i)
```



- 创建一个环境图为问题q

`python ok -q name --trace` //name 是函数名

- 使用assert

`assert  isinstance(x, int), "The input to double(x) must be an integer"`

// if x 不是 int  则打印The input to double(x) must be an integer



###  help



```python
dir(module) #查看包、模块的结构或方法的属性等; 如

dir(math)  #查看math包中的所有方法, 
dir(__builtins__)   #查看Python所有内置函数和内置对象, 
dir(’’)             #查看字符串对象的所有属性和方法; 

module.__all__  
#列出导入包或模块时(from module import*, 这里其实并不会加载模块中所有的函数和属性), 
#可调用的方法和属性(有些包不提供该属性); 

help([module].method)  #查看方法的使用说明, 通常还会包含参数使用说明;

print([module].method.__doc__)   #查看方法的文档信息(与help方法类似); 

print(module.__file__) #查看模块所在的位置, 以方便我们查看模块源代码。
```



