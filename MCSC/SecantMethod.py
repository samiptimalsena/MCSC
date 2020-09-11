from prettytable import PrettyTable

class SecantMethod:
    def __init__(self,a,b,function_secant,range=20,tolerance=0.00005):
        self.a=a
        self.b=b
        self.function=function_secant
        self.tolerance=tolerance
        self.range=range
        self.table=PrettyTable(['n','a','b','x'])

    def __repr__(self):
        return "SecantMethod(a:{},b:{},tolerance:{})".format(self.a,self.b,self.tolerance)

    def calc(self):
        a,b=self.a,self.b
        for i in range(self.range):
            x=(a*self.function(b)-b*self.function(a))/(self.function(b)-self.function(a))
            self.table.add_row([i+1,a,b,round(x,4)])
            a=b
            b=round(x,4)
            if round(abs(self.function(x)),5)<self.tolerance:
                break

        return self.table