'''Sequence V'''
def main():
    '''Sequence V'''
    total = 0
    num = int(input())
    for i in range(num, 0, -1):
        print("%d " %i, end="")
        total += 1
        if total % 7 == 0:
            print()
main()
