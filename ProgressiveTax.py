"""Progressivetotal"""

def main():
    """Progressivetotal"""
    num = int(input())
    total = 0
    if num > 4000000:
        ans = num - 4000000
        num -= ans
        total += ans * 0.35
    if num > 2000000:
        ans = num - 2000000
        num -= ans
        total += ans * 0.30
    if num > 1000000:
        ans = num - 1000000
        num -= ans
        total += ans * 0.25
    if num > 750000:
        ans = num - 750000
        num -= ans
        total += ans * 0.20
    if num > 500000:
        ans = num - 500000
        num -= ans
        total += ans * 0.15
    if num > 300000:
        ans = num - 300000
        num -= ans
        total += ans * 0.10
    if num > 150000:
        ans = num - 150000
        num -= ans
        total += ans * 0.05
    if num > 0:
        pass
    print(int(total))
main()
