"""Sequence VII"""

def main(num):
    """Sequence VII"""
    for k in range(1, num+1):
        for i in range(1, k+1):
            print(i, end=" ")
        print()
    for line in range(num-1, 0, -1):
        for row in range(line):
            print(row+1, end=" ")
        print()
main(int(input()))
