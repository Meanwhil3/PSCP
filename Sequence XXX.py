"""Sequence xxx"""

def main():
    """Sequence xxx"""
    row = int(input())
    many = int(input())
    for i in range(row):
        if i == 0 or i == row-1:
            for _ in range(many):
                print("*" * row, end=" ")
            print()
        else:
            for _ in range(many):
                for j in range(row):
                    if i == j or j == 0 or j == row-1 or j == row-1-i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("", end=" ")
            print()
main()
