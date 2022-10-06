'''Circular II'''
import math
def main():
    '''Circular II'''
    me_x = float(input())
    me_y = float(input())
    radius = float(input())
    friend_x = float(input())
    friend_y = float(input())
    radius_f = float(input())
    num = math.sqrt(((me_x - friend_x) ** 2) + ((me_y - friend_y) ** 2))
    distance = radius + radius_f
    total = num - distance
    if total < 0:
        print("Yes")
    else:
        print("No")
main()
