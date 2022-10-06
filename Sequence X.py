"""Sequence X"""

def main():
    """Sequence X"""
    n_m = int(input())
    for i in range(1, n_m+1):
        for _ in range(n_m-i, 0, -1):
            print("   ", end="")
        for k in range(1, i):
            print("%02d" %k, end=" ")
        for j in range(i, 0, -1):
            print("%02d" %j, end=" ")
        print()
    for i in range(n_m-1, 0, -1):
        for _ in range(n_m-i, 0, -1):
            print("   ", end="")
        for k in range(1, i):
            print("%02d" %k, end=" ")
        for j in range(i, 0, -1):
            print("%02d" %j, end=" ")
        print()
main()
