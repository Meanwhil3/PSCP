"""SecondConverter"""

def main():
    """SecondConverter"""
    time = int(input())
    all_second = int(input())
    all_mins = int(input())
    all_hours = int(input())
    mins = time // all_second
    seconds = time % all_second
    hours = mins // all_mins
    mins = mins % all_mins
    hours = hours % all_hours
    print("%d:%d:%d" % (hours, mins, seconds))
main()
