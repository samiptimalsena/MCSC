class ThomasAlgorithm:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def calc(self):
        alpha=calc_alpha(self.a,self.b,self.c)
        beta=calc_beta(self.a,self.b,self.d,alpha)
        X=list()
        c=self.c
        for i in range(len(alpha)-1,-1,-1):
            if i==len(alpha)-1:
                X.append(beta[i])
            else:
                X.append(beta[i]-(c[i]*X[-1])/alpha[i])

        return alpha,beta,X[::-1]

def calc_alpha(a,b,c):
    alpha=list()
    for i in range(len(b)):
        if i==0:
            alpha.append(b[i])
        else:
            alpha.append(b[i]-(a[i-1]*c[i-1])/alpha[i-1])
    return alpha

def calc_beta(a,b,d,alpha):
    beta=list()
    for i in range(len(b)):
        if i==0:
            beta.append(d[i]/b[i])
        else:
            beta.append((d[i]-a[i-1]*beta[i-1])/alpha[i])
    return beta