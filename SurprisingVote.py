"""SurprisingVote"""

def main():
    """SurprisingVote"""
    total = float(input())
    mak = float(input())
    last = 0
    if (mak * 2) < total:
        last = total - (mak * 2)
    if (mak - last) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
