# -*- coding:utf-8 -*-

class Permutation (object):

    def __init__ (self, n, l):
        """
        [n] est le nombre d'éléments, de 1 à n.
        [l] est la liste d'arrivée, contenant n éléments qui sont l'image de l'indice +1.
        """
        self.n = n
        self.l = l

    def getOrbits (self):
        ret = []
        not_met = 1
        while not_met <= self.n:
            # On ajoute une orbite
            new = [not_met]
            i = not_met
            while self(i) != not_met:
                i = self(i)
                new.append(i)
            ret.append(new)

            # On cherche le prochain indice à tester
            cont = True
            while cont:
                cont = False
                not_met += 1
                for orbit in ret:
                    if not_met in orbit:
                        not_met += 1
                        cont = True
                        break

        return ret

    def getCycles (self):
        ret = []
        for o in self.getOrbits():
            if len(o) != 1: # Identité sinon
                ret.append( Cycle(self.n, o) )
        return ret

    def getDecomposition (self):
        """ Décomposition en transpositions élémentaires """
        ret = []
        for cycle in self.getCycles():
            for trans in cycle.getTrans():
                for elem in trans.getElemTrans():
                    ret.append(elem)

        simple = False
        while not simple:
            simple = True
            for i in range(len(ret)-1):
                if ret[i] == ret[i+1]:
                    ret.pop(i)
                    ret.pop(i)
                    simple = False
                    break
        return ret

    def __call__ (self, x):
        return self.l[x-1]

    def __mul__ (self, s):
        """ Produit de composition dans le groupe (Sn, o) """
        new = []
        for elem in s.l:
            new.append(self(elem))
        return Permutation(self.n, new)

    def __eq__ (self, s):
        return (self.l == s.l)

    def __str__ (self):
        ret = []
        for i in range(len(self.l)):
            ret.append(str(i+1) + " |---> " + str(self(i+1)) + "\n")
        return "".join(ret)


class Id (Permutation):

    def __init__ (self, n):
        Permutation.__init__(self, n, range(1, n+1))


class Cycle (Permutation):

    def __init__ (self, n, l):
        """
        [n] est le nombre d'éléments, de 1 à n. Cela correspond au n de Sn.
        [l] est la liste correspondant à la notation d'une permutation circulaire.
        Par ex., (1,4,2) change 1 en 4, 4 en 2 et 2 en 1.
        """
        self.n = n
        self.k = len(l) # Ordre du cycle
        self.cycle = l
        self.l = range(1, self.n+1)
        for i in range(self.k):
            self.l[self.cycle[i]-1] = self.cycle[ (i+1)%self.k ]

    def getTrans (self):
        """
        Retourne la décomposition du cycle en transpositions.
        """
        ret = []
        for i in range(self.k-1, 0, -1):
            ret.append( Transposition(self.n, 1, self.cycle[i]) )
        return ret

    def __str__ (self):
        ret = ["("]
        for i in range(self.k):
            ret.append( str(self.cycle[i]) + "  " )
        ret[-1] = ret[-1][:-2]
        ret.append(")")
        return "".join(ret)


class Transposition (Cycle):

    def __init__ (self, n, i, j):
        l = range(1, n+1)
        l[i-1] = j
        l[j-1] = i
        self.i = min(i,j)
        self.j = max(i,j)
        Cycle.__init__( self, n, (i,j) )

    def getElemTrans (self):
        ret = []
        for k in range(self.i, self.j):
            ret.append(Transposition(self.n, k, k+1))
        ret += ret[:-1][::-1]
        return ret
