"""[Recommend] Restaurant"""

def main(buy, promotion, dis, must_buy):
    """[Recommend] Restaurant"""
    total = buy + must_buy
    if total >= promotion:
        total -= total*(dis/100)
    if buy >= promotion:
        buy -= buy*(dis/100)
    if total > buy:
        print("No %.03f" %(total - buy))
    elif total < buy:
        print("Yes %.03f" %(buy - total))
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()))
