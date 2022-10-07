"""Stair"""

def main():
    """Stair"""
    boll = True
    total = 0
    ans = 0
    tall = int(input())
    floor = int(input())
    for _ in range(1, floor+1):
        jumping = int(input())
        total += jumping
        if jumping > tall:
            boll = False
        elif total == tall:
            ans += 1
            total = 0
        elif total > tall:
            ans += 1
            total = jumping
    if total > 0:
        ans += 1
    if boll:
        print("%d" % ans)
    else:
        print("NO")
main()
