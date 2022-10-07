"""[Recommend] Diginity"""

def check(num):
    """check"""
    total = 0
    for i in num:
        total += int(i)
    if len(str(total)) != 1:
        total = check(str(total))
    return total

def main():
    """[Recommend] Diginity"""
    while True:
        num = input()
        ans = 0
        if num == "0":
            break
        else:
            ans = check(num)
            print(ans)
main()
