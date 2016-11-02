from equation import *

class AdaptiveQuadrature:
    def __init__(self):
        self.e = Equation()
        self.a = float(input())
        self.b = float(input())
        self.err = float(input())
        self.points = []
        print(self.Q(self.a,self.b))
        self.points = sorted(list(set(self.points)))
        print(len(self.points)+1) 

    def I(self,a,b):
        f = self.e.f
        c = (a+b)/2
        self.points = self.points + [c]
        return (b-a)*(f(a)+4*f(c)+f(b))/6
    
    def I2(self,a,b):
        f = self.e.f
        c1 = a + (b-a)/4
        c2 = a + 2*(b-a)/4
        c3 = a + 3*(b-a)/4
        self.points = self.points + [c1,c2,c3]
        return (b-a)*(f(a)+4*f(c1)+2*f(c2)+4*f(c3)+f(b))/12
    
    def Q(self,a,b):
        c = (a+b)/2
        i = self.I(a,b)
        i2 = self.I2(a,b)
        e = i2 - i

        if e < self.err:
            I = 16*i2/15 - i/15
            return I
        else:
            I = self.Q(a,c) + self.Q(c,b)
            return I


a = AdaptiveQuadrature()
