str1 = '123'
str2=123
print(str1.__str__())
print(str2.__str__())
print(list.__str__([1,2,3]))
if __name__ == "__main__":
    import doctest
    doctest.testmod()