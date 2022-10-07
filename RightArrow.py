"""RightArrow"""

def main():
    """RightArrow"""
    row = int(input())
    col = int(input())
    space = col // 2
    total_space = 0
    for _ in range(space+1):
        print((" ")*total_space+("*")*row)
        total_space += 1
    total_space -= 2
    for _ in range(space):
        print((" ")*total_space+("*")*row)
        total_space -= 1
main()
