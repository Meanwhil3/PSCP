"""Day I"""

def main():
    """Day I"""
    year = int(input())
    if year % 4 == 0 and year % 100 != 0:
        print("Yes")
    elif year % 400 == 0:
        print("Yes")
    else:
        print("No")
main()
