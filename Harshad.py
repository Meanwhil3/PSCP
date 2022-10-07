"""Harshad"""

def main():
    """Harshad"""
    num = [input() for _ in range(10)]
    for i in num:
        i = i.replace('-', '')
        if float(i) == 0:
            print('No')
            continue
        sum_harshad = 0
        for j in i:
            sum_harshad += int(j)
        i = float(i)
        if i % sum_harshad == 0:
            print('Yes')
        else:
            print('No')
main()
