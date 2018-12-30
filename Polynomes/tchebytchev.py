# -*- coding:utf-8 -*-

from math import cos, pi
from polynome import Polynome

# Calcul des 100 premiers termes de Tn

Tn = Polynome((1,))
Tn_1 = Polynome((0,1))
for i in range(10):
    Tn_2 = Polynome((0,2))*Tn_1 - Tn
    Tn = Tn_1
    Tn_1 = Tn_2
    print(Tn(cos( (pi/(i+1))*0.5 )))
    print("T{} = {}".format(i+2, Tn_2))
