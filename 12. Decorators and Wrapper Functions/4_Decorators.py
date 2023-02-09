def printOutputReport(func):
    def f(*args, **kwargs):
        z = func(*args, **kwargs)
        print("----------This is a report for your formula------------")
        for i, ar in enumerate(args):
            print("Your"+str(i)+" variable is:", ar)
        print("The result of your formula is ", z)
    return f


@printOutputReport
def calcFormula1(x,y,w,z):
    return x*y+x/2 + 2+w+z


@printOutputReport
def calcFormula2(x, y,t,u):
    return x*x*x + y*y*y + x+y+10+y*u


calcFormula2(2,6,7,7)
