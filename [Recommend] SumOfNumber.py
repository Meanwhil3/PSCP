"""SumOfNumber"""
def main():
    """SumOfNumber"""
    first = int(input())
    ans = 0
    while True:
        num = int(input())
        if num > 0:
            ans += num
        if ans == first or num == -1:
            print(ans)
            return
main()
