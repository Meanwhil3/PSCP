"""[Recommend] Milk"""

def main():
    "[Recommend] Milk"
    bottle = int(input())
    far = int(input())
    free = int(input())
    money = int(input())
    ans = money // bottle
    milk = ans
    if far == 0:
        print(milk)
    else:
        while True:
            more = (ans // far) * free
            milk += more
            mod = (ans % far)
            ans = 0
            ans += mod
            ans += more
            more = 0
            if ans < far:
                break
        print(milk)
main()
