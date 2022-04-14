a = [0, 2, 4, 6, 8, 10, 12, 14]
b = [0, 3, 6, 9, 12, 15]

iter_a, iter_b = iter(a), iter(b)
next_a, next_b = next(iter_a, None), next(iter_b, None)

print(next_a, next_b)
print(next(iter_a))