"""TheFunctionWithin"""

def fun_b(num1, num2):
    """fun b"""
    ansa = (num1 - num2)*2
    funb1 = 3*(ansa**4) - ansa**3 + 2*(ansa**2) + 10
    return funb1

def fun_c(num1, num2, num3, num4):
    """fun c"""
    ansx = 2*(num1 + num2)
    ansy = 2*(num1 + num3)
    ansz = 2*(num4**2)
    ansz1 = 3*(ansz**4) - ansz**3 + 2*(ansz**2) + 10
    func1 = ((ansz1 + ansx)**2) - ansx*ansy + ansy**2
    return func1

def fun_d(num1, num2, num3, num4):
    """fun d"""
    ansx = 2*(num1 + num2)
    ansy = 2*(num1 - num3)
    ansz = 2*(num4**2)
    ansz1 = 3*(ansz**4) - ansz**3 + 2*(ansz**2) + 10
    ansa = ((ansz1 + ansx)**2) - ansx*ansy + ansy**2
    ansb = fun_b(num1, num2)
    ansc = num3*(2**5)
    ansd = num4**8
    fund1 = ((ansa**2 + ansb**2 - ansc**2)/(ansd**2 - (2*ansa*ansd) + 2*ansa))
    return fund1

def main():
    """main"""
    num1, num2, num3, num4 = float(input()), float(input()), float(input()), float(input())
    funa = 2*(2*num1)
    funb = fun_b(num1, num2)
    func = fun_c(num1, num2, num3, num4)
    fund = fun_d(num1, num2, num3, num4)
    print(funa)
    print(funb)
    print(func)
    print(fund)
main()
