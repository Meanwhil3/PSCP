"""Inflation"""

def check(num):
    """check"""
    return num*103.81/100

def main(money, year):
    """Inflation"""
    for _ in range(year):
        money = check(money)
    ans = ("%.3f" %money)
    print(ans[:-1:])
main(float(input()), int(input()))
