"""Run Length Decoding"""

def main(name):
    """Run Length Decoding"""
    ans = ""
    for word in name:
        if word.isnumeric():
            ans += word
        else:
            print(word * int(ans), end="")
            ans = ""
main(input())
