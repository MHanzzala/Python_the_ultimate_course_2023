def calcFormula1(x, y):
    return x*y+x/2 + 2


def calcFormula2(x, y):
    return x*x*x + y*y*y + x+y+10


def printOutputReport(func):
    def f(x, y):
        z = func(x, y)
        print("----------This is a report for your formula------------")
        print("You X variable is:", x)
        print("You Y variable is:", y)
        print("The result of your formula is ", z)
    return f


calcFormula2 = printOutputReport(calcFormula2)


calcFormula2(2, 3)
