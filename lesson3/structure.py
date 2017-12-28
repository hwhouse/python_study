ls = []
ls.append(1)
ls.append(2)
print(ls)
print(ls[0])
for i in ls:
    print(i)
del ls[0]
print(ls)

set([1,2,3])
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1-s2)
print(s1&s2)
