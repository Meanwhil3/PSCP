"""Stamps"""

def main():
    """Stamps"""
    num = int(input())
    promotion = int(input())
    stamp = int(input())
    total_stamp = int(input())
    discount = int(input())
    total = 0
    ans = 0
    for _ in range(num):
        price = int(input())
        while price > 0 and ans >= total_stamp:
            ans -= total_stamp
            price = max(price - discount, 0)
        total += price
        ans += stamp * (price // promotion)
    print(str(total) + '\n' + str(ans))
main()
