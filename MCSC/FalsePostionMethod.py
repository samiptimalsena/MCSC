from prettytable import PrettyTable

class FalsePostionMethod:
    def __init__(self,a,b,function_fpmethod,range=20,tolerance=0.00005):
        self.a=a
        self.b=b
        self.function=function_fpmethod
        self.tolerance=tolerance
        self.range=range
        self.table=PrettyTable(['n','a','b','x','f(x)'])

    def __repr__(self):
        return "FalsePositionMethod(a:{},b:{},tolerance:{})".format(self.a,self.b,self.tolerance)

    def calc(self):
        a,b=self.a,self.b  
        for i in range(self.range):    
            x=(a*self.function(b)-b*self.function(a))/(self.function(b)-self.function(a))
            self.table.add_row([i+1,a,b,round(x,4),round(self.function(x),4)])
            if self.function(x)*self.function(a)<0:
                b=round(x,4)
            else:
                a=round(x,4)
            if round(abs(self.function(x)),5)<self.tolerance:
                break
        
        return self.table