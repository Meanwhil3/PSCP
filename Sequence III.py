'''sequence'''
def main():
    '''sequence'''
    n_m = int(input())
    count = 2
    for i in range(2, n_m+2):
        count = i
        for _ in range(n_m):
            print(count, end=" ")
            count += 1
        print()
main()
