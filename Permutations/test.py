# -*- coding:utf-8 -*-

from permutation import Permutation, Cycle, Transposition, Id

s = Permutation(5, (5,4,3,1,2))
for elem in s.getDecomposition():
    print(elem)

print("\n\n")

c = Cycle(5, (1,4,2))
test = Id(5)
for elem in c.getDecomposition():
    print(elem)
    test *= elem

print(c==s)
print(c==test)

# TOUT OK !
