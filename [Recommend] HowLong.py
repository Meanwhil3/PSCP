"""[Recommend] HowLong"""
def main():
    """[Recommend] HowLong"""
    text = input()
    ans = 0
    for _ in text:
        ans += 1
    if int(text) < 0:
        ans -= 1
    print(ans)
main()
