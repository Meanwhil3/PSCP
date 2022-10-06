"""[Recommend] Key"""

def main():
    """[Recommend] Key"""
    text = input()
    ans = 0
    for i in text:
        ans += int(i)
    ans += int(text[-1:-3])
main()