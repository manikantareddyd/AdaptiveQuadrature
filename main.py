from equation import *
import matplotlib.pyplot as plt
class AdaptiveQuadrature:
    def __init__(self):
        self.e = Equation()
        self.a = float(input())
        self.b = float(input())
        self.err = float(input())
        print(self.a,self.b,self.err)
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
    def plot(self):
        y_t = [self.e.f(t) for t  in self.points]
        x_t = self.points
        x = [self.a + 0.1*t for t in range(int((self.b-self.a)/0.1))]
        y = [self.e.f(t) for t in x]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title("Adaptive Quadrature")
        ax.set_ylabel("Y")
        ax.set_xlabel("X")
        ax.axhline(0)
        ax.plot(x,y, "-", label='Funtion')
        for i in range(len(x_t)):
            ax.plot([x_t[i],x_t[i]],[0,y_t[i]], "-", c='r')
        # ax.scatter(x_t,y_t, s=30, c='r', marker="s", label='Quadrature Points')
        plt.legend(loc='best')
        plt.show()
        fig.savefig("Plot.png")



a = AdaptiveQuadrature()
print(a.points)
a.plot()