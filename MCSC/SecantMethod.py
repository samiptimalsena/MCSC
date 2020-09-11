from prettytable import PrettyTable

class SecantMethod:
    def __init__(self,initial_approx,b,function_secant,steps=20,tolerance=0.00005):
        self.a=initial_approx
        self.b=b
        self.function=function_secant
        self.tolerance=tolerance
        self.steps=steps
        self.table=PrettyTable(['n','a','b','x'])

    def __repr__(self):
        return "SecantMethod(a:{},b:{},tolerance:{})".format(self.a,self.b,self.tolerance)

    def calc(self):
        a,b=self.a,self.b
        for i in range(self.steps):
            x=(a*self.function(b)-b*self.function(a))/(self.function(b)-self.function(a))
            self.table.add_row([i+1,a,b,round(x,4)])
            a=b
            b=round(x,4)
            if round(abs(self.function(x)),5)<self.tolerance:
                break

        return self.table