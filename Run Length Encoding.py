"""Run Length Encoding"""

def main(name):
    """Run Length Encoding"""
    ans = name[0]
    count = 0
    total = ""
    for i in range(0, len(name)):
        if ans == name[i]:
            count += 1
        else:
            total += str(count) + name[i-1]
            ans = name[i]
            count = 1
    total += str(count) + name[-1]
    print(total)

main(input())
