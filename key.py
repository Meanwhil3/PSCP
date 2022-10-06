"""[Recommend] Key"""
 
def main():
    """[Recommend] Key"""
    num = input()
    sult = 0
    for i in num:
        sult += int(i)
    last = int(num[10:14]) * 10
    key = sult + last
    if key < 1000:
        key += 1000
    elif key > 9999:
        key %= 10000
    print("%04d" %key)
main()
