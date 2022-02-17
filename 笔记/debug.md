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
