"""[Recommend] Donut"""

def main():
    """[Recommend] Donut"""
    price = int(input())
    buy = int(input())
    free = int(input())
    want_get = int(input())
    total = buy+free
    sett = want_get // total
    if (total*sett) == want_get:
        print(price*(sett*buy), total*sett)
    elif (total*sett) < want_get:
        print(price*((sett+1)*buy), total*(sett+1))
main()
