"""Sequence I"""

def main(num):
    """Sequence I"""
    for _ in range(num):
        for k in range(1, num+1):
            print(k, end=" ")
        print()
main(int(input()))
