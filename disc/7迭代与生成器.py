s = [[1, 2, 3, 4]]
i = iter(s)
j = iter(next(i))
print(next(j))
#1

s.append(5)
print(next(i))
#5
print(next(j))
#2
print(list(j))
#[3,4]
print(next(i))
#StopIteration