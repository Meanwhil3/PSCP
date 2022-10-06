'''Sequence IV'''
def main():
    '''Sequence IV'''
    num = int(input())
    for i in range(1, (num**2)+1):
        print("%d " %i, end="")
        if i % num == 0:
            print()
main()
