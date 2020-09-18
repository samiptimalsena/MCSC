from sympy import *

class Interpolate:
    def __init__(self,values):
        self.x = [t[0] for t in values]
        self.y = [t[1] for t in values]
    
    def calc(self,x):
        s=0
        for i in range(len(self.x)):
            p=1
            for j in range(len(self.x)):
                if not i==j:
                    p = p*((x-self.x[j])/(self.x[i]-self.x[j]))
            s=s+p*self.y[i]
        return s
    
    def find_eq(self):
        s = 0
        x = symbols('x')
        for i in range(len(self.x)):
            p=1
            for j in range(len(self.x)):
                if not i==j:
                    p = p*((x-self.x[j])/(self.x[i]-self.x[j]))
            s=s+expand(p*self.y[i])
        return s