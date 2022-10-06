"""Stepper II"""

def main(first, last):
    """Stepper II"""
    if first < last:
        for i in range(first, last+1):
            print(i)
    else:
        for k in range(first, last-1, -1):
            print(k)
main(int(input()), int(input()))
