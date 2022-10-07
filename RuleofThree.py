"""RuleofThree"""

def check(price, size):
    """check"""
    return size/price

def main():
    """RuleofThree"""
    num = int(input())
    price_1 = float(input())
    size_1 = float(input())
    total_1 = check(price_1, size_1)
    for _ in range(num-1):
        price = float(input())
        size = float(input())
        total_2 = check(price, size)
        if total_1 < total_2:
            total_1 = total_2
            price_1 = price
            size_1 = size
        elif total_1 == total_2 and price < price_1:
            total_1 = total_2
            price_1 = price
            size_1 = size
    print("%.2f %.2f" %(price_1, size_1))
main()
