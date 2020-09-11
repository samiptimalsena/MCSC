from prettytable import PrettyTable
import math

class BisectionMethod:
    def __init__(self,a,b,function_bisection,tolerance=0.00005):
        self.a=a
        self.b=b
        self.tolerance=tolerance
        self.function=function_bisection
        self.table=PrettyTable(['n','a','b','x','f(x)'])

    def __repr__(self):
        return "BisectionMethod(a:{},b:{},tolerance:{})".format(self.a,self.b,self.tolerance)
    
    def calc(self): 
        a,b=self.a,self.b
        steps=math.ceil(math.log(abs(b-a)/self.tolerance)/math.log(2))
        for i in range(steps):
            x=round((a+b)/2,4)
            self.table.add_row([i+1,a,b,x,round(self.function(x),4)])
            if self.function(x)*self.function(a)<0:
                b=x
            else:
                a=x
        
        return steps,self.table

