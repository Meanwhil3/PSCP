"""Sequence N"""

def main(num):
    """Sequence N"""
    for row in range(num):
        for col in range(num):
            tar1 = col == 0
            tar2 = col == num-1
            tar3 = col == row
            if tar1 or tar2 or tar3:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
