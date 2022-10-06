"""Grade III"""

def check(num):
    """Check"""
    total = 0
    if num >= 95 and num <= 100:
        total = 4
    elif num >= 90 and num < 95:
        total = 3.5
    elif num >= 85 and num < 90:
        total = 3
    elif num >= 80 and num < 85:
        total = 2.5
    elif num >= 75 and num < 80:
        total = 2
    elif num >= 70 and num < 75:
        total = 1.5
    elif num >= 65 and num < 70:
        total = 1
    elif num >= 60 and num < 65:
        total = 0.5
    elif num < 60 and num >= 0:
        total = 0
    return total

def main():
    """Grade III"""
    total = 0
    many = int(input())
    if many >= 0:
        for _ in range(many):
            num = float(input())
            ans = check(num)
            total += ans
    total = ((int((total / many)*100))/100)
    print("%.2f" %total)
main()
