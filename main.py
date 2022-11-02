from scipy.special import comb
import math
from math import e
class Binomial:
    def __init__(self, n, p,x):
        self.n = n
        self.p = p
        self.x = x

    def Bin(self):
        pe = round(comb(self.n, self.x)*(self.p**self.x)*(1-self.p)**(self.n-self.x),5)
        print("A probabilidade de sucesso, para x = {}, é: {}".format(self.x,pe))

    def media(self):
        u = self.n*self.p
        print("A media é {} ".format(u))

    def v_d(self):
        v = self.n*self.p*(1-self.p)
        d = round(math.sqrt(v),2)
        print("A variancia é {} e o desvio padra é {}".format(v,d))

class Hipergeometrica:
    def __init__(self, N, n, M,x):
        self.n = n
        self.M = M
        self.N = N
        self.x = x
    def H(self):
        p = (comb(self.M,self.x)*comb(self.N-self.M, self.n-self.x))/comb(self.N,self.n)
        print("A probalidade de sucesso para x = {} é : {}".format(self.x, p))


    def media(self):
        u = self.n*self.M/self.N
        print("O valor esperado ou a media é {}".format(u))

    def v_d(self):
        a = self.n*self.M/self.N
        b= (self.N -self.M)
        c = (self.N-self.n)/(self.N - 1)
        v = a*b*c
        d = round(math.sqrt(v),2)
        print("A variancia é {} e o desvio padrão é {}".format(v, d))

class Poisson:
    def __init__(self, lamb, x):
        self.lamb = lamb
        self.x = x

    def P(self):
        p = round((e**(-self.lamb)*self.lamb**self.x)/math.factorial(self.x),3)
        print("A probabilidade é = {}".format(p))
#a = Binomial(14,0.26,0)
#a.Bin()
#b =Binomial(14,0.26,1)
#b.Bin()
#c = Binomial(14,0.26,2)
#c.Bin()
##
#soma = 0.01477+0.07263+0.16587
#print(soma)
#pelo_menos_dois = 1 - (0.01477+0.07263)
#print(pelo_menos_dois)
##
#a.media()

h = Hipergeometrica(24,18, )
h.H()
