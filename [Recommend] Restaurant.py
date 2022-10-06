"""[Recommend] Restaurant"""

def main():
    """[Recommend] Restaurant"""
    price = float(input())
    promotion = float(input())
    coupon = float(input())
    must_buy = float(input())
    total_price = price + must_buy
    total = total_price*(coupon/100)
    ans = total_price-total
    if price == promotion:
        print("Yes")
    elif price > promotion:
        print("Yes %.3f" %(price-ans))
    elif promotion > price:
        if ans < price:
            print("Yes %.3f" %(price-ans))
        elif ans > price:
            print("No %.3f" %(ans-price))
main()
