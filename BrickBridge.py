"""BrickBridge"""

def main():
    """BrickBridge"""
    small = int(input())
    big = int(input())
    goal = int(input())
    if goal % 5 > small or (small + (big * 5)) < goal:
        print(-1)
    else:
        if big * 5 >= goal:
            small = goal % 5
        else:
            small = goal-(big*5)
        print(small)
main()
