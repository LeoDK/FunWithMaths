# -*- coding:utf-8 -*-

MOINS_INFINI = -340282366920938463463374607431768211456L
PLUS_INFINI = 340282366920938463463374607431768211456L

from copy import deepcopy

class Polynome (object):

    @staticmethod
    def deg (P):
        for i in range(len(P.coefs)-1, -1, -1):
            if P.coefs[i]!=0:
                return i
        return MOINS_INFINI

    @staticmethod
    def val (P):
        for i in range(len(P.coefs)):
            if P.coefs[i]!=0:
                return i
        return PLUS_INFINI

    def update (self, coefs):
        self.coefs = list(coefs)
        self.deg = Polynome.deg(self)
        self.val = Polynome.val(self)
        while len(self.coefs) < self.deg + 1:
            self.coefs.pop(-1)
        
    def __init__ (self, coefs):
        self.update(coefs)

    def __add__ (self, Q):
        coefs = []
        deg = max(Q.deg, self.deg)
        val = min(Q.val, self.val)
        coefs += [0]*val
        for i in range(val, deg+1):
            if i > Q.deg:
                coefs.append(self.coefs[i])
            elif i > self.deg:
                coefs.append(Q.coefs[i])
            else:
                coefs.append(Q.coefs[i] + self.coefs[i])
        return Polynome(coefs)

    def __neg__ (self):
        ret = deepcopy(self)
        for i in range(ret.deg + 1):
            ret.coefs[i] = -ret.coefs[i]
        return ret

    def __sub__ (self, Q):
        return self + (-Q)

    def __mul__ (self, Q):
        coefs = [0]*(self.deg+Q.deg+1)
        for i in range(self.deg+1):
            for j in range(Q.deg+1):
                coefs[i+j] += self.coefs[i]*Q.coefs[j]
        return Polynome(coefs)

    def __rmul__ (self, n):
        return self * Polynome((n,))

    def __pow__ (self, n):
        ret = Polynome([1])
        for i in range(n):
            ret *= self
        return ret

    def __str__ (self):
        ret = ""
        for i in range(self.deg-self.val+1):
            if self.coefs[self.deg-i] != 0:
                ret += str(self.coefs[self.deg-i]) + "X^" + str(self.deg-i) + " + "
        return ret[:-3]

    def __call__ (self, x):
        """ Evaluer le polynôme en une valeur """
        ret = 0
        for i in range(self.deg-self.val+1):
            ret += self.coefs[self.val+i] * (x**(self.val+i))
        return ret
