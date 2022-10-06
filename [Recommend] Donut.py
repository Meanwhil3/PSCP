"""[Recommend] Donut"""

def main():
    """[Recommend] Donut"""
    price = int(input())
    buy = int(input())
    free = int(input())
    want = int(input())
    in_want = want // (buy + free)
    if want == 0:
        print("0 0")
    elif want > 0:
        donut = in_want*(buy + free)
        total_left = want - donut
        if total_left > buy:
            total_left = buy
        if total_left >= buy:
            donut = donut + (buy + free)
        else:
            donut = donut + total_left
        total_price = (price*in_want*buy) + (total_left*price)
        print("%d %d" % (total_price, donut))
main()
