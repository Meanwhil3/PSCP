'''[Recommend] BTSMRT'''
def main():
    '''free or pay'''
    day = input()
    age = float(input())
    height = float(input())
    if (day == "Children Day" and age < 14 and height <= 140) \
        or (age < 14 and height < 90):
        print('FREE')
    elif day == "Senior Day" and age >= 60:
        print('FREE')
    else:
        print('PAY')
main()
