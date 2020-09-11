from prettytable import PrettyTable
import numpy as np

class IterationMethod:
    def __init__(self,initial_approx,functions,steps=40,tolerance=0.00005):
        self.a=initial_approx
        self.main_functions=functions[:len(functions)//2]
        self.functions=functions[len(functions)//2:]
        self.steps=steps
        self.tolerance=tolerance
        self.table=PrettyTable(['n']+['x_'+str(i+1) for i in range(len(self.a))])

    def __repr__(self):
        return "IterationMethod(initial_approx:{},tolerance:{})".format(self.a,self.tolerance)
    
    def calc(self):
        a=self.a
        for i in range(self.steps):
            x=[function(*a) for function in self.functions]
            self.table.add_row([i+1]+[round(x_i,4) for x_i in x])
            a=x
            check=np.array([function(*x) for function in self.main_functions])
            if np.all(np.abs(check.round(5))<self.tolerance):
                break
        
        return self.table

class JacobiMethod(IterationMethod):
    def __init__(self,initial_approx,functions,steps=40,tolerance=0.00005):
        super().__init__(initial_approx,functions,steps,tolerance)

    def __repr__(self):
        return "JacobiMethod(initial_approx:{},tolerance:{})".format(self.a,self.tolerance)

class GaussSeidelMethod(IterationMethod):
    def __init__(self,initial_approx,functions,steps=40,tolerance=0.00005):
        super().__init__(initial_approx,functions,steps,tolerance)

    def __repr__(self):
        return "GaussSeidelMethod(initial_approx:{},tolerance:{})".format(self.a,self.tolerance)

    def calc(self):
        x=self.a
        for i in range(self.steps):
            for j in range(len(x)):
                x[j]=self.functions[j](*x)
            self.table.add_row([i+1]+[round(x_i,4) for x_i in x])
            check=np.array([function(*x) for function in self.main_functions])
            if np.all(np.abs(check.round(5))<self.tolerance):
                break

        return self.table
