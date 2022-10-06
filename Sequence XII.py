"""Sequence XII"""

def main():
    """Sequence XII"""
    num = int(input())
    for i in range(-num + 1, num, 1):
        for j in range(-num + 1, num, 1):
            print("%02d"%(num - abs(abs(i) - abs(j))), end=" ")
        print()
main()
