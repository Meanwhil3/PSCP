"""Parallelogram"""

def main():
    """Parallelogram"""
    name = input()
    suck = ""
    total_space = len(name)
    for k in name:
        print(" "*(total_space-1), end="")
        total_space -= 1
        suck += k
        print(suck)
    total_y = len(suck)
    for ttt in range(total_y):
        print(suck[ttt+1:])
main()
