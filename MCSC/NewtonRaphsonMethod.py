from prettytable import PrettyTable
import math

class NewtonRaphsonMethod:
    def __init__(self,initial_approx,function,derivative_function,steps=20,tolerance=0.00005):
        self.a=initial_approx
        self.function=function
        self.derivative_function=derivative_function
        self.tolerance=tolerance
        self.steps.steps
        self.table=PrettyTable(['n','a','x'])

    def __repr__(self):
        return "NewtonRaphsonMethod(a:{},tolerance:{})".format(self.a,self.tolerance)

    def calc(self):
        a=self.a
        for i in range(self.steps):   
            x=a-(self.function(a)/self.derivative_function(a))
            self.table.add_row([i+1,a,round(x,4)])
            a=round(x,4)
            if round(abs(self.function(x)),5)<self.tolerance:
                break
        
        return self.table


class GeneralizedNewtonRaphsonMethod(NewtonRaphsonMethod):
    def __init__(self,initial_approx,function,derivative_function,repeated_roots,range=20,tolerance=0.00005):
        super().__init__(initial_approx,function,derivative_function)
        self.repeated_roots=repeated_roots
    
    def __repr__(self):
        return "GeneralizedNewtonRaphsonMethod(a:{},tolerance:{})".format(self.a,self.tolerance)

    def calc(self):
        a=self.a
        for i in range(self.steps):        
            x=a-self.repeated_roots*(self.function(a)/self.derivative_function(a))
            self.table.add_row([i+1,a,round(x,4)])
            a=round(x,4)
            if round(abs(self.function(x)),5)<self.tolerance:
                break

        return self.table

class NewtonMethodForSystem:
    def __init__(self,initial_approx,functions,steps=40,tolerance=0.0005):
        self.a=initial_approx
        self.main_functions=functions[:math.floor(len(functions)**(1/2))]
        self.functions=functions[math.floor(len(functions)**(1/2)):]
        self.steps=steps
        self.tolerance=tolerance
        self.table=PrettyTable(['x','y','f','g','a','b','c','d','ad-bc','-fd+gb','-ga+fc','h','k'])

    def __repr__(self):
        return "NewtonRaphsonForSystem(initial_approx:{},tolerance:{})".format(self.a,self.tolerance)

    def calc(self):
        x,y=self.a[0],self.a[1]
        for i in range(self.steps):
            a=self.functions[0](x,y)
            b=self.functions[1](x,y)
            c=self.functions[2](x,y)
            d=self.functions[3](x,y)
            D=a*d-b*c
            D_1=-self.main_functions[0](x,y)*d+self.main_functions[1](x,y)*b
            D_2=-self.main_functions[1](x,y)*a+self.main_functions[0](x,y)*c
            h=D_1/D
            k=D_2/D  
            self.table.add_row([round(x,4),round(y,4),
                                round(self.main_functions[0](x,y),4),
                                round(self.main_functions[1](x,y),4),
                                round(a,4),round(b,4),round(c,4),
                                round(d,4),round(D,4),round(D_1,4),
                                round(D_2,4),round(h,4),round(k,3)])
            x=x+h
            y=y+k
            if round(abs(self.main_functions[0](x,y)),5)<0.00005 and round(abs(self.main_functions[1](x,y)))<0.00005:
                break

        return self.table



