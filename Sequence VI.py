"""Sequence VI"""

def main(num):
    """Sequence VI"""
    for k in range(1, num+1):
        for i in range(1, k+1):
            print(i, end=" ")
        print()
main(int(input()))
